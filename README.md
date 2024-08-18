### 🚀 **Telegram Chat Explorer**

[**Русская версия**](#README_ru.md)📜  

---

Welcome to **Telegram Chat Explorer**! This is a powerful tool for analyzing Telegram chats exported in JSON format. Use it to obtain detailed statistics about users, messages, media files, and much more. Both personal and group chats are supported!



## ⚙️ **Features**

- Count messages from each user.
- Count characters in each user's messages.
- Count unique words and words in each message.
- Analyze media files: support for voice messages, video messages, stickers, audio files, and GIFs.
- Top popular words with the option to exclude prepositions and other words.
- Average message length in characters and words.

## 🛠 **Installation**
README
To use this tool, you need to clone the repository.

```bash
git clone https://github.com/cl7paBka/TelegramChatExplorer.git
cd TelegramChatExplorer
```

## 🚀 **Usage**

To analyze chats, you need to export data from Telegram in JSON format. Then you can run the script by specifying the path to the chat file:

```bash
python main.py <path_to_your_exported_chat.json>
```

### Example:

```bash
python main.py --file ./chat_data.json
```

## 📊 **Usage Examples**

After running the script, you will receive full statistics on:

- Number of messages from each user.
- Number of characters and words in messages.
- Popular and unique words in the chat.
- Number of media messages, including videos, audio, and animations.

## 📝 **License**

This project is not licensed.

## 📧 **Contact**

If you have any questions or suggestions, feel free to open an [Issue](https://github.com/cl7paBka/TelegramChatExplorer/issues/new).
