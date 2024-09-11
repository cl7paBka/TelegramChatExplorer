import json
import re


def load_chat_data(file_path):
    """Загружает данные чата из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_text(message):
    """Извлекает текст сообщения, если оно не является медиа-сообщением."""
    if 'text' in message and not message.get('media_type'):
        text = message['text']
        if isinstance(text, list):
            # Если текст представлен в виде списка, объединим элементы в строку
            text = ''.join([str(item) for item in text])
        return text
    return ''


def filter_words(text, excluded_words):
    """Фильтрует слова из текста, исключая заданные группы."""
    words = re.findall(r'\b\w+\b', text.lower())
    if not excluded_words:
        return words  # Если нет слов для исключения, возвращаем все слова
    return [word for word in words if word not in excluded_words]
