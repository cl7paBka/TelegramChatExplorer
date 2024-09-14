import pandas as pd
import src.utils as utils
from collections import Counter
from datetime import timedelta


class TelegramChatAnalyzer:
    """Класс для анализа чатов Telegram."""

    def __init__(self, chat_data, language, excluded_words, top_words_amount, show_chat_type, show_total_participants,
                 show_total_messages_stats, show_total_words_stats, show_total_media_stats,
                 show_participant_messages_stats, show_participant_words_stats, show_participant_media_stats):
        self.chat_data = chat_data
        self.excluded_words = excluded_words or []
        self.top_n_words = top_words_amount
        self.language = language

        self.user_stats = {}
        self.users = set()  # Множество для хранения уникальных пользователей

        self.total_messages = 0  # Общее количество сообщений
        self.total_unique_words = set()  # Общее количество уникальных слов
        self.total_characters = 0  # Общее количество символов
        self.total_words = 0  # Общее количество слов
        self.total_voice_messages_count = 0  # Общее количество голосовых сообщений
        self.total_voice_messages_duration = 0  # Общая продолжительность аудио сообщений
        self.total_video_messages_count = 0  # Общее количество видео сообщений
        self.total_video_messages_duration = 0  # Общая продолжительность видео сообщений
        self.total_stickers_count = 0  # Общее количество стикеров
        self.total_audio_file_count = 0  # Общее количество аудио файлов
        self.total_animation_count = 0  # Общее количество GIF
        self.chat_type = None  # Тип чата (персональный или групповой)

        self._process_chat_data()

        self.show_chat_type = show_chat_type
        self.show_total_participants = show_total_participants
        self.show_total_messages_stats = show_total_messages_stats
        self.show_total_words_stats = show_total_words_stats
        self.show_total_media_stats = show_total_media_stats
        self.show_participant_messages_stats = show_participant_messages_stats
        self.show_participant_words_stats = show_participant_words_stats
        self.show_participant_media_stats = show_participant_media_stats

    def _process_chat_data(self):
        """Обрабатывает все сообщения и собирает статистику."""
        self.chat_type = self.chat_data["type"]

        for message in self.chat_data.get('messages', []):
            user = message.get('from')
            if not user:  # Игнорируем сообщения от неизвестных отправителей
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
                        "voice_message_duration": 0,
                        "video_message": 0,
                        "video_message_duration": 0,
                        "sticker": 0,
                        "audio_file": 0,
                        "animation": 0
                    }
                }

            text = utils.extract_text(message)
            self.total_messages += 1
            self.user_stats[user]['messages'] += 1

            if text:
                self.user_stats[user]['characters'] += len(text)
                words = utils.filter_words(text, self.excluded_words)
                self.user_stats[user]['words'].update(words)
                self.user_stats[user]['unique_words'].update(words)
                self.total_unique_words.update(words)

                word_count = len(words)
                self.user_stats[user]['total_words'] += word_count
                self.total_words += word_count

            elif "media_type" in message:  # Проверяем, есть ли медиа-сообщение
                media_type = message["media_type"]
                duration = message.get("duration_seconds", 0)
                if media_type == "voice_message":
                    self.user_stats[user]["media"][media_type] += 1
                    self.user_stats[user]["media"]["voice_message_duration"] += duration
                    self.total_voice_messages_duration += duration
                elif media_type == "video_message":
                    self.user_stats[user]["media"][media_type] += 1
                    self.user_stats[user]["media"]["video_message_duration"] += duration
                    self.total_video_messages_duration += duration
                elif media_type in self.user_stats[user]["media"]:
                    self.user_stats[user]["media"][media_type] += 1

        self.count_total()

    def _format_duration(self, total_seconds):
        """Форматирует продолжительность в недели, дни, часы, минуты и секунды."""
        duration = timedelta(seconds=total_seconds)
        weeks, days = divmod(duration.days, 7)
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        formatted = []
        if weeks > 0:
            formatted.append(f"{weeks} weeks" if self.language == 'en' else f"{weeks} недель")
        if days > 0:
            formatted.append(f"{days} days" if self.language == 'en' else f"{days} дней")
        if hours > 0:
            formatted.append(f"{hours} hours" if self.language == 'en' else f"{hours} часов")
        if minutes > 0:
            formatted.append(f"{minutes} minutes" if self.language == 'en' else f"{minutes} минут")
        if seconds > 0:
            formatted.append(f"{seconds} seconds" if self.language == 'en' else f"{seconds} секунд")

        return ' '.join(formatted)

    def count_total(self):
        """Считает все total счётчики."""
        self.total_characters = sum(stats['characters'] for stats in self.user_stats.values())
        self.total_voice_messages_count = sum(stats['media']['voice_message'] for stats in self.user_stats.values())
        self.total_video_messages_count = sum(stats['media']['video_message'] for stats in self.user_stats.values())
        self.total_animation_count = sum(stats['media']['animation'] for stats in self.user_stats.values())
        self.total_audio_file_count = sum(stats['media']['audio_file'] for stats in self.user_stats.values())
        self.total_stickers_count = sum(stats['media']['sticker'] for stats in self.user_stats.values())

    # Prints

    def print_chat_type(self):
        """Выводит тип чата (персональный или групповой)."""
        if self.show_chat_type:
            if self.language == 'ru':
                print(f"Тип чата: {self.chat_type}")
            else:
                print(f"Chat type: {self.chat_type}")

    def print_total_users(self):
        """Выводит количество пользователей в чате."""
        if self.show_total_participants:
            if self.language == 'ru':
                print(f"Количество пользователей в чате: {len(self.users)}")
            else:
                print(f"Total users in chat: {len(self.users)}")

    def print_total_messages(self):
        """Выводит общее количество сообщений."""
        if self.show_total_messages_stats:
            if self.language == 'ru':
                print(f"\nОбщее количество сообщений: {self.total_messages}")
            else:
                print(f"\nTotal messages: {self.total_messages}")

    def print_messages_by_user(self):
        """Выводит количество сообщений от каждого пользователя."""
        if self.show_participant_messages_stats:
            if self.language == 'ru':
                print("\nКоличество сообщений по пользователям:")
            else:
                print("\nMessages by user:")
            for user, stats in self.user_stats.items():
                print(f"  {user}: {stats['messages']}")

    def print_total_characters(self):
        """Выводит общее количество символов."""
        if self.show_total_words_stats:
            if self.language == 'ru':
                print(f"\nОбщее количество символов: {self.total_characters}")
            else:
                print(f"\nTotal characters: {self.total_characters}")

    def print_characters_by_user(self):
        """Выводит количество символов в сообщениях от каждого пользователя."""
        if self.show_participant_words_stats:
            if self.language == 'ru':
                print("\nКоличество символов по пользователям:")
            else:
                print("\nCharacters by user:")
            for user, stats in self.user_stats.items():
                print(f"  {user}: {stats['characters']}")

    def print_total_words(self):
        """Выводит общее количество слов."""
        if self.show_total_words_stats:
            if self.language == 'ru':
                print(f"\nОбщее количество слов: {self.total_words}")
            else:
                print(f"\nTotal words: {self.total_words}")

    def print_words_by_user(self):
        """Выводит количество слов от каждого пользователя."""
        if self.show_participant_words_stats:
            if self.language == 'ru':
                print("\nКоличество слов по пользователям:")
            else:
                print("\nWords by user:")
            for user, stats in self.user_stats.items():
                print(
                    f"  {user}: {stats['total_words']} слов" if self.language == 'ru' else f"  {user}: {stats['total_words']} words")

    def print_average_message_length_by_user(self):
        """Выводит среднее количество символов на сообщение для каждого участника."""
        if self.show_participant_messages_stats:
            if self.language == 'ru':
                print(f"\nСредняя длина сообщений:")
            else:
                print(f"\nAverage message length:")
            for user, stats in self.user_stats.items():
                if stats['messages'] > 0:
                    avg_length = stats['characters'] / stats['messages']
                    print(
                        f"  {user}: {round(avg_length)} символов" if self.language == 'ru' else f"  {user}: {round(avg_length)} characters")

    def print_total_unique_words_count(self):
        """Выводит общее количество уникальных слов."""
        if self.show_total_words_stats:
            if self.language == 'ru':
                print(f"\nОбщее количество уникальных слов: {len(self.total_unique_words)}")
            else:
                print(f"\nTotal unique words: {len(self.total_unique_words)}")

    def print_unique_words(self):
        """Выводит количество уникальных слов по каждому пользователю."""
        if self.show_participant_words_stats:
            if self.language == 'ru':
                print("Уникальные слова по пользователям:")
            else:
                print("Unique words by user:")
            for user, stats in self.user_stats.items():
                print(f"  {user}: {len(stats['unique_words'])}")

    def print_average_words_per_message_by_user(self):
        """Выводит среднее количество слов на сообщение."""
        if self.show_participant_words_stats:
            if self.language == 'ru':
                print(f"\nСреднее количество слов на сообщение:")
            else:
                print(f"\nAverage words per message:")
            for user, stats in self.user_stats.items():
                if stats['messages'] > 0:
                    avg_words = sum(stats['words'].values()) / stats['messages']
                    print(f"  {user}: {round(avg_words)}")

    def print_total_media_messages(self):
        """Выводит общее количество медиа-сообщений по типам."""
        if self.show_total_media_stats:
            if self.language == 'ru':
                print("\nОбщее количество медиа-сообщений:")
                print(f"  Аудио сообщения: {self.total_voice_messages_count}")
                print(f"  Видео сообщения: {self.total_video_messages_count}")
                print(f"  Стикеры: {self.total_stickers_count}")
                print(f"  Аудио файлы: {self.total_audio_file_count}")
                print(f"  Гифки: {self.total_animation_count}")
            else:
                print("\nTotal media messages:")
                print(f"  Voice messages: {self.total_voice_messages_count}")
                print(f"  Video messages: {self.total_video_messages_count}")
                print(f"  Stickers: {self.total_stickers_count}")
                print(f"  Audio files: {self.total_audio_file_count}")
                print(f"  GIFs: {self.total_animation_count}")

    def print_media_messages_by_user(self):
        """Выводит количество медиа-сообщений для каждого пользователя."""
        if self.show_participant_media_stats:
            for user, stats in self.user_stats.items():
                media_stats = stats['media']
                if self.language == 'ru':
                    print(f"\nМедиа-сообщения от {user}:")
                    print(f"  Аудио сообщения: {media_stats['voice_message']}")
                    print(f"  Видео сообщения: {media_stats['video_message']}")
                    print(f"  Стикеры: {media_stats['sticker']}")
                    print(f"  Аудио файлы: {media_stats['audio_file']}")
                    print(f"  Гифки: {media_stats['animation']}")
                else:
                    print(f"\nMedia messages from {user}:")
                    print(f"  Voice messages: {media_stats['voice_message']}")
                    print(f"  Video messages: {media_stats['video_message']}")
                    print(f"  Stickers: {media_stats['sticker']}")
                    print(f"  Audio files: {media_stats['audio_file']}")
                    print(f"  GIFs: {media_stats['animation']}")

    def print_voice_messages_duration(self):
        """Выводит общую и пользовательскую продолжительность аудио сообщений."""
        if self.show_total_media_stats:
            if self.language == 'ru':
                print(
                    f"\nОбщая продолжительность аудиосообщений: {self._format_duration(self.total_voice_messages_duration)}")
            else:
                print(f"\nTotal voice message duration: {self._format_duration(self.total_voice_messages_duration)}")
        if self.show_participant_media_stats:
            for user, stats in self.user_stats.items():
                duration = stats["media"]["voice_message_duration"]
                if duration > 0:
                    if self.language == 'ru':
                        print(f"  {user}: {self._format_duration(duration)}")
                    else:
                        print(f"  {user}: {self._format_duration(duration)}")

    def print_video_messages_duration(self):
        """Выводит общую и пользовательскую продолжительность видео сообщений."""
        if self.show_total_media_stats:
            if self.language == 'ru':
                print(
                    f"\nОбщая продолжительность видеосообщений: {self._format_duration(self.total_video_messages_duration)}")
            else:
                print(f"\nTotal video message duration: {self._format_duration(self.total_video_messages_duration)}")
        if self.show_participant_media_stats:
            for user, stats in self.user_stats.items():
                duration = stats["media"]["video_message_duration"]
                if duration > 0:
                    if self.language == 'ru':
                        print(f"  {user}: {self._format_duration(duration)}")
                    else:
                        print(f"  {user}: {self._format_duration(duration)}")

    def top_words(self):
        """Выводит топ популярных слов с учётом фильтрации."""

        if self.top_n_words is None or self.show_participant_words_stats is False:
            return  # Пользователь отключил функцию топа слов

        for user, stats in self.user_stats.items():
            most_common_words = stats['words'].most_common(self.top_n_words)
            if self.language == 'ru':
                print(f"\nТоп {self.top_n_words} слов для {user}:")
            else:
                print(f"\nTop {self.top_n_words} words for {user}:")
            for word, count in most_common_words:
                if self.language == 'ru':
                    print(f"  {word.capitalize()}: {count} раз(а)")
                else:
                    print(f"  {word.capitalize()}: {count} times")

    # Saving for excel file


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
        self.print_voice_messages_duration()
        self.print_video_messages_duration()
        self.top_words()
