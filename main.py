from utils import load_chat_data
from analyzer import TelegramChatAnalyzer
from config import config

def main():
    """Главная функция программы, запускающая анализ данных."""
    config.load_from_args()

    try:
        chat_data = load_chat_data(config.file)

        analyzer = TelegramChatAnalyzer(
            chat_data=chat_data,
            excluded_words=config.exclude,
            top_n_words=config.top,
            language=config.language
        )

        analyzer.print_summary()

    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")

if __name__ == "__main__":
    main()
