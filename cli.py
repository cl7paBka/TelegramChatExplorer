import argparse


def parse_arguments():
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(description='Анализ чатов Telegram.')
    parser.add_argument('file', help='Путь к JSON файлу с данными чата')
    parser.add_argument('--top_words', type=int, default=None,
                        help='Количество слов для отображения в топе популярных слов (по умолчанию отключено)')
    parser.add_argument('--exclude', nargs='*', default=[],
                        help='Список слов для исключения из анализа (например, предлоги)')

    return parser.parse_args()
