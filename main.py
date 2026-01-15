import streamlit as st

from services.get_models_list import get_ollama_models_list
from services.get_title import get_chat_title
from services.chat_utilities import get_answer
from db.conversations import(
    create_new_conservation,
    add_message,
    get_conversation,
    get_all_conversations,
)

st.set_page_config(page_title="ConvoPro", page_icon="💬",layout="centered")
st.title("💬 ConvoPro - AI Chat Application")


if "OLLAMA_MODELS" not in st.session_state:
    st.session_state.OLLAMA_MODELS = get_ollama_models_list()

selected_model = st.selectbox("Select LLM Model", st.session_state.OLLAMA_MODELS)


st.session_state.setdefault("conversation_id", None)
st.session_state.setdefault("conversation_title", None)
st.session_state.setdefault("chat_history", [])


with st.sidebar:
    st.header("💬 Chat History")
    conversations = get_all_conversations()

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.conversation_id = None
        st.session_state.conversation_title = None
        st.session_state.chat_history = []

    for cid, title in conversations.items():
        is_current = cid == st.session_state.conversation_id
        label = f"{title}" if is_current else title
        if st.button(label, key=f"conv_{cid}"):
            doc = get_conversation(cid) or {}
            st.session_state.conversation_id = cid
            st.session_state.conversation_title = doc.get("title", "New Conversation")
            st.session_state.chat_history = [
                {"role": msg["role"], "content": msg["content"]}
                for msg in doc.get("messages", [])
            ]

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_query = st.chat_input("Type your message here...")

if user_query:
    st.chat_message("user").markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    if st.session_state.conversation_id is None:
        try:
            title = get_chat_title(selected_model, user_query) or "New Conversation"
        except Exception:
            title = "New Conversation"
        
        conv_id = create_new_conservation(title=title, role="user", content=user_query)
        st.session_state.conversation_id = conv_id
        st.session_state.conversation_title = title
    else:
        add_message(st.session_state.conversation_id, "user", user_query)
    try:
        assistant_text = get_answer(selected_model, st.session_state.chat_history)
    except Exception as e:
        assistant_text = "Error: Unable to get response from the model."
        st.error(f"LLM Error: {e}")

    with st.chat_message("assistant"):
        st.markdown(assistant_text)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_text})



    if st.session_state.conversation_id:
        add_message(
            st.session_state.conversation_id, "assistant", assistant_text
        )
