from src.utils import load_chat_data
from src.analyzer import TelegramChatAnalyzer
from src.config import Config

def main():
    """Главная функция программы, запускающая анализ данных."""
    config = Config()


    try:
        chat_data = load_chat_data(config.input_file_path)

        analyzer = TelegramChatAnalyzer(
            chat_data=chat_data,
            language=config.language,
            excluded_words=config.exclude_words,
            top_words_amount=config.top_words_amount,
            show_chat_type=config.show_chat_type,
            show_total_participants=config.show_total_participants,
            show_total_messages_stats=config.show_total_messages_stats,
            show_total_words_stats=config.show_total_words_stats,
            show_total_media_stats=config.show_total_media_stats,
            show_participant_messages_stats=config.show_participant_messages_stats,
            show_participant_words_stats=config.show_participant_words_stats,
            show_participant_media_stats=config.show_participant_media_stats
        )

        analyzer.print_summary()

    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")

if __name__ == "__main__":
    main()
