import json

def load_chat_data(file_path):
    """Загружает данные чата из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
