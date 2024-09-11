from colorama import Fore, Style, init
import json
import re


def load_chat_data(file_path):
    """Загружает данные чата из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_text(message):
    """Извлекает текст сообщения, если оно не является медиа-сообщением."""
    if 'text' in message and not message.get('media_type'):
        text = message['text']
        if isinstance(text, list):
            # Если текст представлен в виде списка, объединим элементы в строку
            text = ''.join([str(item) for item in text])
        return text
    return ''


def filter_words(text, excluded_words):
    """Фильтрует слова из текста, исключая заданные группы."""
    words = re.findall(r'\b\w+\b', text.lower())
    if not excluded_words:
        return words  # Если нет слов для исключения, возвращаем все слова
    return [word for word in words if word not in excluded_words]

init(autoreset=True)

def print_logo():

    logo = f"""
 {Fore.MAGENTA}/\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
 /\_/\                                     /\_/\ 
( o.o )                                   ( o.o )
 {Fore.MAGENTA}> ^ <{Fore.MAGENTA}    {Fore.LIGHTWHITE_EX}/$$$$$$$$  /$$$$$$  /$$$$$$$${Fore.LIGHTWHITE_EX}    {Fore.MAGENTA}> ^ < {Fore.MAGENTA}
 {Fore.MAGENTA}/\_/\{Fore.MAGENTA}   {Fore.LIGHTWHITE_EX}|__  $$__/ /$$__  $$| $$_____/{Fore.LIGHTWHITE_EX}    {Fore.MAGENTA}/\_/\ {Fore.MAGENTA}
{Fore.MAGENTA}( o.o ){Fore.MAGENTA}     {Fore.LIGHTWHITE_EX}| $$   | $$  \__/| $${Fore.LIGHTWHITE_EX}         {Fore.MAGENTA}( o.o ){Fore.MAGENTA}
 {Fore.MAGENTA}> ^ <{Fore.MAGENTA}      {Fore.LIGHTWHITE_EX}| $$   | $$      | $$$$${Fore.LIGHTWHITE_EX}       {Fore.MAGENTA}> ^ < {Fore.MAGENTA}
 {Fore.MAGENTA}/\_/\{Fore.MAGENTA}      {Fore.LIGHTWHITE_EX}| $$   | $$      | $$__/{Fore.LIGHTWHITE_EX}       {Fore.MAGENTA}/\_/\ {Fore.MAGENTA}
{Fore.MAGENTA}( o.o ){Fore.MAGENTA}     {Fore.LIGHTWHITE_EX}| $$   | $$    $$| $${Fore.LIGHTWHITE_EX}         {Fore.MAGENTA}( o.o ){Fore.MAGENTA}
 {Fore.MAGENTA}> ^ <{Fore.MAGENTA}      {Fore.LIGHTWHITE_EX}| $$   |  $$$$$$/| $$$$$$$${Fore.LIGHTWHITE_EX}    {Fore.MAGENTA}> ^ < {Fore.MAGENTA}
 {Fore.MAGENTA}/\_/\{Fore.MAGENTA}      {Fore.LIGHTWHITE_EX}|__/    \______/ |________/{Fore.LIGHTWHITE_EX}    {Fore.MAGENTA}/\_/\ {Fore.MAGENTA}
{Fore.MAGENTA}( o.o )                                   ( o.o )
 > ^ <                                     > ^ < 
 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
"""
    print(logo)
    return ''