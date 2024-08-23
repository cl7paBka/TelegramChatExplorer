import argparse


class Config:
    def __init__(self):
        self.file = None
        self.language = 'en'
        self.top = None
        self.exclude = []
        self.print_chat_type = True
        self.print_total_users = True
        self.print_total_messages = True
        self.print_messages_by_user = True
        self.print_total_characters = True
        self.print_characters_by_user = True
        self.print_total_words = True
        self.print_words_by_user = True
        self.print_average_message_length_by_user = True
        self.print_total_unique_words_count = True
        self.print_unique_words = True
        self.print_average_words_per_message_by_user = True
        self.print_total_media_messages = True
        self.print_media_messages_by_user = True
        self.print_voice_messages_duration = True
        self.print_video_messages_duration = True


    def load_from_args(self):
        parser = argparse.ArgumentParser(description="Telegram Chat Analyzer Configuration")
        parser.add_argument('file', help='Path to the JSON file with chat data')
        parser.add_argument('--language', choices=['en', 'ru'], default='en', help='Choose language (default: en)')

        parser.add_argument('--top', type=int, default=None)
        parser.add_argument('--exclude', nargs='*', default=[],
                            help='Список слов для исключения из анализа (например, предлоги)')

        parser.add_argument('--print_chat_type', action='store_true', help='Print chat type')
        parser.add_argument('--print_total_users', action='store_true', help='Print total users')
        parser.add_argument('--print_total_messages', action='store_true', help='Print total messages')
        parser.add_argument('--print_messages_by_user', action='store_true', help='Print messages by user')
        parser.add_argument('--print_total_characters', action='store_true', help='Print total characters')
        parser.add_argument('--print_characters_by_user', action='store_true', help='Print characters by user')
        parser.add_argument('--print_total_words', action='store_true', help='Print total words')
        parser.add_argument('--print_words_by_user', action='store_true', help='Print words by user')
        parser.add_argument('--print_average_message_length_by_user', action='store_true',
                            help='Print average message length by user')
        parser.add_argument('--print_total_unique_words_count', action='store_true',
                            help='Print total unique words count')
        parser.add_argument('--print_unique_words', action='store_true', help='Print unique words by user')
        parser.add_argument('--print_average_words_per_message_by_user', action='store_true',
                            help='Print average words per message by user')
        parser.add_argument('--print_total_media_messages', action='store_true', help='Print total media messages')
        parser.add_argument('--print_media_messages_by_user', action='store_true', help='Print media messages by user')
        parser.add_argument('--print_voice_messages_duration', action='store_true',
                            help='Print voice messages duration')
        parser.add_argument('--print_video_messages_duration', action='store_true',
                            help='Print video messages duration')

        args = parser.parse_args()
        self.file = args.file
        self.language = args.language
        self.print_chat_type = args.print_chat_type
        self.print_total_users = args.print_total_users
        self.print_total_messages = args.print_total_messages
        self.print_messages_by_user = args.print_messages_by_user
        self.print_total_characters = args.print_total_characters
        self.print_characters_by_user = args.print_characters_by_user
        self.print_total_words = args.print_total_words
        self.print_words_by_user = args.print_words_by_user
        self.print_average_message_length_by_user = args.print_average_message_length_by_user
        self.print_total_unique_words_count = args.print_total_unique_words_count
        self.print_unique_words = args.print_unique_words
        self.print_average_words_per_message_by_user = args.print_average_words_per_message_by_user
        self.print_total_media_messages = args.print_total_media_messages
        self.print_media_messages_by_user = args.print_media_messages_by_user
        self.print_voice_messages_duration = args.print_voice_messages_duration
        self.print_video_messages_duration = args.print_video_messages_duration


config = Config()
