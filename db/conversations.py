from typing import Any, Dict, Optional

from pymongo import DESCENDING
from db.mongo import get_collection


conversations = get_collection("conversations")
conversations.create_index([("last_interacted", DESCENDING)])



def now_utc():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc)

def create_new_conversation_id()-> str:
    import uuid
    return str(uuid.uuid4())

def create_new_conservation(title: Optional[str] = None, role: Optional[str] = None , content: Optional[str] = None) -> str:
   conv_id = create_new_conversation_id()
   ts= now_utc()

   doc={
       "_id": conv_id,
       "title": title or "New Conversation",
         "messages": [],
         "last_interacted": ts,
   }

   if role and content:
        doc["messages"].append({
            "role": role,
            "content": content,
            "timestamp": ts,
        })
        conversations.insert_one(doc)
        return conv_id
   

def add_message(conv_id: str, role: str, content: str) -> bool:
    ts = now_utc()
    result = conversations.update_one(
        {"_id": conv_id},
        {
            "$push": {
                "messages": {
                    "role": role,
                    "content": content,
                    "timestamp": ts,
                }
            },
            "$set": {
                "last_interacted": ts,
            },
        },
    )
    return result.matched_count == 1

def get_conversation(conv_id: str) -> Optional[Dict[str, Any]]:
    ts= now_utc()
    doc = conversations.find_one_and_update(
        {"_id": conv_id},
        {
            "$set": {
                "last_interacted": ts,
            }
        },
        return_document=True
    )
    return doc

def get_all_conversations()->Dict[str,str]:
    cursor = conversations.find({}, {"title": 1}).sort("last_interacted", DESCENDING)
    return {doc["_id"]: doc.get("title", "New Conversation") for doc in cursor}