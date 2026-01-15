from config.settings import Settings

settings = Settings()


def get_ollama_models_list():
    models_list =settings.OLLAMA_MODELS
    ollama_models = [model.strip() for model in models_list.split(",") if model.strip()]
    return ollama_models