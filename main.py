from utils import load_chat_data
from analyzer import TelegramChatAnalyzer
from cli import parse_arguments


def main():
    """Главная функция программы, запускающая анализ данных."""
    args = parse_arguments()  # Парсинг аргументов командной строки

    try:
        # Загрузка данных из JSON
        chat_data = load_chat_data(args.file)

        # Создание экземпляра анализатора с переданными опциями
        analyzer = TelegramChatAnalyzer(
            chat_data=chat_data,
            excluded_words=args.exclude,
            top_n_words=args.top_words
        )

        # Выводим собранную статистику
        analyzer.print_summary()

    except KeyboardInterrupt:
        print("\nПрограмма завершена. Было нажато Ctrl+C")


if __name__ == "__main__":
    main()
