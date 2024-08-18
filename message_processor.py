import re

class MessageProcessor:
    """Класс для обработки отдельных сообщений."""

    @staticmethod
    def extract_text(message):
        """Извлекает текст сообщения, если оно не является медиа-сообщением."""
        if 'text' in message and not message.get('media_type'):
            text = message['text']
            if isinstance(text, list):
                # Если текст представлен в виде списка, объединим элементы в строку
                text = ''.join([str(item) for item in text])
            return text
        return ''

    @staticmethod
    def count_characters(text):
        """Подсчитывает количество символов в тексте сообщения."""
        return len(text)

    @staticmethod
    def filter_words(text, excluded_words):
        """Фильтрует слова из текста, исключая заданные группы."""
        words = re.findall(r'\b\w+\b', text.lower())
        if not excluded_words:
            return words  # Если нет слов для исключения, возвращаем все слова
        return [word for word in words if word not in excluded_words]
