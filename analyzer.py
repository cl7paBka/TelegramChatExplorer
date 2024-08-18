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
        self.total_unique_words = set()  # Для общего количества уникальных слов
        self.total_characters = 0
        self.total_words = 0  # Для общего количества слов
        self.total_voice_messages_count = 0  # Для голосовых сообщений
        self.total_video_messages_count = 0  # Для видео сообщений
        self.total_stickers_count = 0  # Стикеры
        self.total_audio_file_count = 0  # Музыка/аудиофайлы
        self.total_animation_count = 0  # Гифки
        self.chat_type = None  # Тип чата (персональный или групповой)
        self._process_chat_data()

    def _process_chat_data(self):
        """Обрабатывает все сообщения и собирает статистику."""
        self.chat_type = self.chat_data["type"]

        for message in self.chat_data.get('messages', []):
            user = message.get('from')
            if not user:  # Игнорируем сообщения от Unknown
                continue

            self.users.add(user)
            if user not in self.user_stats:
                self.user_stats[user] = {
                    'messages': 0,
                    'characters': 0,
                    'words': Counter(),
                    'total_words': 0,  # Количество слов для каждого пользователя
                    'unique_words': set(),
                    'media_count': 0,
                    'photo_count': 0,
                    'media': {
                        "voice_message": 0,
                        "video_message": 0,
                        "sticker": 0,
                        "audio_file": 0,
                        "animation": 0
                    }
                }

            text = MessageProcessor.extract_text(message)
            self.total_messages += 1
            self.user_stats[user]['messages'] += 1

            if text:
                self.user_stats[user]['characters'] += MessageProcessor.count_characters(text)
                words = MessageProcessor.filter_words(text, self.excluded_words)
                self.user_stats[user]['words'].update(words)
                self.user_stats[user]['unique_words'].update(words)
                self.total_unique_words.update(words)  # Обновляем уникальные слова в общем

                word_count = len(words)
                self.user_stats[user]['total_words'] += word_count  # Увеличиваем количество слов для пользователя
                self.total_words += word_count  # Увеличиваем общее количество слов
            elif "media_type" in message:  # Проверяем, есть ли медиа-сообщение
                media_type = message["media_type"]
                if media_type in self.user_stats[user]["media"]:
                    self.user_stats[user]["media"][media_type] += 1

        self.count_total()

    def count_total(self):
        """Считает все total счётчики"""
        self.total_characters = sum(stats['characters'] for stats in self.user_stats.values())
        self.total_voice_messages_count = sum(stats['media']['voice_message'] for stats in self.user_stats.values())
        self.total_video_messages_count = sum(stats['media']['video_message'] for stats in self.user_stats.values())
        self.total_animation_count = sum(stats['media']['animation'] for stats in self.user_stats.values())
        self.total_audio_file_count = sum(stats['media']['audio_file'] for stats in self.user_stats.values())
        self.total_stickers_count = sum(stats['media']['sticker'] for stats in self.user_stats.values())

    #################################### Prints
    def print_chat_type(self):
        print(f"Тип чата: {self.chat_type}")

    def print_total_users(self):
        print(f"Количество пользователей в чате: {len(self.users)}")

    def print_total_messages(self):
        print(f"\nОбщее количество сообщений: {self.total_messages}")

    def print_messages_by_user(self):
        """Выводит количество сообщений от каждого пользователя."""
        for user, stats in self.user_stats.items():
            print(f"  {user}: {stats['messages']}")

    def print_total_characters(self):
        print(f"\nОбщее количество символов: {self.total_characters}")

    def print_characters_by_user(self):
        """Выводит количество символов в сообщениях от каждого пользователя."""
        for user, stats in self.user_stats.items():
            print(f"  {user}: {stats['characters']}")

    def print_total_words(self):
        """Выводит общее количество слов."""
        print(f"\nОбщее количество слов: {self.total_words}")

    def print_words_by_user(self):
        """Выводит количество слов от каждого пользователя."""
        for user, stats in self.user_stats.items():
            print(f"  {user}: {stats['total_words']} слов")

    # Добавить def print_avarage_message_length() нужно ли???

    def print_average_message_length_by_user(self):
        """Выводит среднее количество символов на сообщение для каждого участника."""
        print(f"\nСредняя длина сообщений:")
        for user, stats in self.user_stats.items():
            if stats['messages'] > 0:
                avg_length = stats['characters'] / stats['messages']
                print(f"  {user}: {round(avg_length)} символов")

    def print_total_unique_words_count(self):
        print(f"\nОбщее количество уникальных слов: {len(self.total_unique_words)}")

    def print_unique_words(self):
        """Подсчитывает количество уникальных слов по каждому пользователю."""
        for user, stats in self.user_stats.items():
            print(f"  {user}: {len(stats['unique_words'])}")

    # добавить def среднее количество слов на сообщение. Нужно ли???
    def print_average_words_per_message_by_user(self):
        """Подсчитывает среднее количество слов на сообщение."""
        print(f"\nСреднее количество слов на сообщение:")
        for user, stats in self.user_stats.items():
            if stats['messages'] > 0:
                avg_words = sum(stats['words'].values()) / stats['messages']
                print(f"  {user}: {round(avg_words)}")

    def print_total_media_messages(self):
        """Выводит общее количество медиа-сообщений по типам."""
        print("\nОбщее количество медиа-сообщений:")
        print(f"  Аудио сообщения: {self.total_voice_messages_count}")
        print(f"  Видео сообщения: {self.total_video_messages_count}")
        print(f"  Стикеры: {self.total_stickers_count}")
        print(f"  Аудио файлы: {self.total_audio_file_count}")
        print(f"  Гифки: {self.total_animation_count}")

    def print_media_messages_by_user(self):
        """Выводит количество медиа-сообщений для каждого пользователя."""
        for user, stats in self.user_stats.items():
            media_stats = stats['media']
            print(f"\nМедиа-сообщения от {user}:")
            print(f"  Аудио сообщения: {media_stats['voice_message']}")
            print(f"  Видео сообщения: {media_stats['video_message']}")
            print(f"  Стикеры: {media_stats['sticker']}")
            print(f"  Аудио файлы: {media_stats['audio_file']}")
            print(f"  Гифки: {media_stats['animation']}")

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
        self.print_chat_type()
        self.print_total_users()
        self.print_total_messages()
        self.print_messages_by_user()
        self.print_total_characters()
        self.print_characters_by_user()
        self.print_total_words()
        self.print_words_by_user()
        self.print_average_message_length_by_user()
        self.print_total_unique_words_count()
        self.print_unique_words()
        self.print_average_words_per_message_by_user()
        self.print_total_media_messages()
        self.print_media_messages_by_user()
        self.top_words()
