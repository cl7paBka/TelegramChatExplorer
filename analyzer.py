from collections import Counter
from message_processor import MessageProcessor


class TelegramChatAnalyzer:
    """Класс для анализа чатов Telegram."""

    def __init__(self, chat_data, excluded_words=None, top_n_words=None):
        self.chat_data = chat_data
        self.excluded_words = excluded_words or []
        self.top_n_words = top_n_words
        self.user_stats = {}
        self.users = set()  # Множество для хранения уникальных пользователей
        self.total_messages = 0  # Для общего количества сообщений
        self.total_unique_words = set()  # Для подсчета уникальных слов в общем
        self.total_voice_messages_count = 0
        self.total_video_messages_count = 0
        self.total_stickers_count = 0
        self.total_audio_file_count = 0
        self.total_gif_count = 0 #animation
        self.media_types = ["animation", "audio_file", "sticker", "video_message", "voice_message"]
        self._process_chat_data()

    def _process_chat_data(self):
        """Обрабатывает все сообщения и собирает статистику."""
        for message in self.chat_data.get('messages', []):
            user = message.get('from')
            if not user:  # Игнорируем сообщения от Unknown
                continue

            self.users.add(user)
            text = MessageProcessor.extract_text(message)
            if not text:
                continue  # Пропуск медиа-сообщений

            self.total_messages += 1  # Увеличиваем счётчик сообщений

            if user not in self.user_stats:
                self.user_stats[user] = {
                    'messages': 0,
                    'characters': 0,
                    'words': Counter(),
                    'unique_words': set(),
                    'media_count': 0,
                    'photo_count': 0
                }

            self.user_stats[user]['messages'] += 1
            self.user_stats[user]['characters'] += MessageProcessor.count_characters(text)
            words = MessageProcessor.filter_words(text, self.excluded_words)
            self.user_stats[user]['words'].update(words)
            self.user_stats[user]['unique_words'].update(words)
            self.total_unique_words.update(words)  # Обновляем уникальные слова в общем



    def count_messages_by_user(self):
        """Выводит количество сообщений от каждого пользователя."""
        for user, stats in self.user_stats.items():
            print(f"{user}: {stats['messages']} сообщений")

    def count_characters_by_user(self):
        """Выводит количество символов в сообщениях от каждого пользователя."""
        for user, stats in self.user_stats.items():
            print(f"{user}: {stats['characters']} символов")

    def count_total_characters(self):
        """Подсчитывает общее количество символов во всех сообщениях."""
        total_characters = sum(stats['characters'] for stats in self.user_stats.values())
        print(f"Общее количество символов: {total_characters}")

    def average_message_length(self):
        """Выводит среднее количество символов на сообщение для каждого участника."""
        for user, stats in self.user_stats.items():
            if stats['messages'] > 0:
                avg_length = stats['characters'] / stats['messages']
                print(f"{user}: средняя длина сообщения {round(avg_length)} символов")

    def count_unique_words(self):
        """Подсчитывает количество уникальных слов в общем и по каждому пользователю."""
        print(f"Общее количество уникальных слов: {len(self.total_unique_words)}")
        for user, stats in self.user_stats.items():
            print(f"{user}: {len(stats['unique_words'])} уникальных слов")

    def average_words_per_message(self):
        """Подсчитывает среднее количество слов на сообщение."""
        for user, stats in self.user_stats.items():
            if stats['messages'] > 0:
                avg_words = sum(stats['words'].values()) / stats['messages']
                print(f"{user}: среднее количество слов на сообщение {round(avg_words)}")
    # def count_voice_messages(self):


    def count_media_messages(self):
        """Подсчитывает количество медиа-сообщений по типам в общем и по каждому пользователю."""
        print(
            f"Общее количество медиа-сообщений (animation, audio_file, sticker, video_message, voice_message): {self.total_media_count}")
        for user, stats in self.user_stats.items():
            print(f"{user}: {stats['media_count']} медиа-сообщений")

    def count_photo_messages(self):
        """Подсчитывает количество фото-сообщений в общем и по каждому пользователю."""
        print(f"Общее количество фото: {self.total_photo_count}")
        for user, stats in self.user_stats.items():
            print(f"{user}: {stats['photo_count']} фото")

    def top_words(self):
        """Выводит топ популярных слов с учётом фильтрации."""
        if self.top_n_words is None:
            return  # Пользователь отключил функцию топа слов

        for user, stats in self.user_stats.items():
            most_common_words = stats['words'].most_common(self.top_n_words)
            print(f"\nТоп {self.top_n_words} слов для {user}:")
            for word, count in most_common_words:
                print(f"  {word.capitalize()}: {count} раз(а)")

    def print_summary(self):
        """Выводит всю собранную статистику."""
        print(f"Количество пользователей в чате: {len(self.users)}")
        print(f"Общее количество сообщений: {self.total_messages}")
        print("\nКоличество сообщений от каждого пользователя:")
        self.count_messages_by_user()
        self.count_total_characters()  # Общее количество символов
        print("\nКоличество символов от каждого пользователя:")
        self.count_characters_by_user()
        print("\nСредняя длина сообщений:")
        self.average_message_length()
        print("\nКоличество уникальных слов:")
        self.count_unique_words()
        print("\nСреднее количество слов на сообщение:")
        self.average_words_per_message()
        # print("\nМедиа-сообщения (animation, audio_file, sticker, video_message, voice_message):")
        #self.count_media_messages()
        # print("\nКоличество фото:")
        #self.count_photo_messages()
        self.top_words()

