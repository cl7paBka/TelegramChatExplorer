import argparse


class Config:
    def __init__(self):
        self.input_file_path = 'input.txt'
        self.use_default_config = True

        self.language = 'en'
        self.top_words_amount = 10  # Переместить к word статс?
        self.exclude_words = ['the', 'and', 'a', 'of']

        self.show_chat_type = True
        self.show_total_participants = True

        self.show_total_messages_stats = True
        self.show_total_words_stats = True
        self.show_total_media_stats = True # voice_message, voice_message_duration, video_message, video_message_duration, stickers, audio file, animation

        self.show_participant_messages_stats = True
        self.show_participant_words_stats = True
        self.show_participant_media_stats = True

        self.args = self._parse_args()

        self._merge_with_cli_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser(description="Telegram Chat Explorer - Описание тут ")

        parser.add_argument('-c', '--use_config', action='store_true',
                            help='Использовать значения из config.py, игнорируя CLI')

        parser.add_argument('-f', '--file', help='Path to the JSON file with chat data')
        # parser.add_argument('-o', '--output', help='Path to the .txt output file')
        parser.add_argument('-l', '--language', choices=['en', 'ru'], default='en',
                            help='Choose language (default: en, available: ru)')

        parser.add_argument('-e', '--exclude', nargs='*', default=[],
                            help='Список слов для исключения из анализа (например, предлоги)')

        parser.add_argument('-t', '--top', type=int, default=None, help='Количество слов')

        parser.add_argument('-p', '--participants', action='store_true',
                            help='Не показывать статистику по количеству участников чата')
        parser.add_argument('-m', '--messages', action='store_true', help='Не показывать статистику по сообщениям')
        parser.add_argument('-w', '--words', action='store_true', help='Не показывать статистику по словам')
        parser.add_argument('-mc', '--media_content', action='store_true',
                            help='Не показывать статистику по медиаконтенту')

        args = parser.parse_args()

        return args

    def _merge_with_cli_args(self):
        """Объединяем значения из CLI с конфигурацией."""
        if self.args.use_config:
            print("Используем значения из config.py")
        else:
            # Если указаны аргументы, то они перезаписывают значения по умолчанию
            if self.args.file:
                self.input_file_path = self.args.file
            # if self.args.output:
            #     self.output_file_path = self.args.output
            if self.args.language:
                self.language = self.args.language

            if self.args.exclude:
                self.exclude_words = self.args.exclude
            if self.args.top:  # Переместить к word статс?
                self.top_words_amount = self.args.top

            if self.args.participants:
                self.show_total_participants = self.args.participants

            if self.args.messages:
                self.show_total_messages_stats = self.args.messages
                self.show_participant_messages_stats = self.args.messages
            if self.args.words:
                self.show_total_words_stats = self.args.words
                self.show_participant_words_stats = self.args.words
            if self.args.media_content:
                self.show_total_media_stats = self.args.media_content
                self.show_participant_media_stats = self.args.media_content


config = Config()
