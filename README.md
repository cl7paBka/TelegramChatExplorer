
# 💬 TelegramChatExplorer

**TelegramChatExplorer** is a powerful command-line tool designed to help you dive deep into your Telegram chat data!
🌐
Whether you're curious about your group chats or personal conversations, this app gives you all the insights you need from your exported JSON data. Analyze, track, and visualize your Telegram interactions like never before! 🚀

---

## Features 🛠

- 📝 Automatically detect the type of chat (group or private)
- 👥 Get detailed statistics on the number of participants and users
- 📊 Analyze message counts both overall and for individual users
- 📝 Track the total number of characters written, broken down by user
- 📄 Count the total number of words, both globally and per user
- 🔤 Discover the average message length for each user (in characters)
- 🔠 Measure count of unique words used in the chat
- 🖼 Track the total count of media messages (voice/video messages, stickers, etc.) 
- 🎞 Breakdown of media messages per user
- 🎙 Find out the total duration of all voice messages and video messages exchanged
- 🏆 Identify the most frequently used words with a "Top Words" list

---

## Installation 📦

1. Clone the project from GitHub:
    ```bash
    git clone https://github.com/cl7paBka/TelegramChatExplorer
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Export your Telegram chat (desktop only) in JSON format (**without media**). Here's a helpful [video guide](https://www.youtube.com/watch?v=_H8O6Oc1_Zw&t) on how to export your chats.

---

## Usage 🚀

To run the application, use the command-line arguments provided through `argparse`. Below is an example:

```bash
python telegram_chat_explorer.py -f <path_to_chat.json> -u
```

[help]: https://raw.githubusercontent.com/cl7paBka/TelegramChatExplorer/main/readme_assets/--help.png "Logo Title Text 2"
### Key arguments:
- `-f, --file`: Path to the JSON file containing the chat data.
- `-l, --language`: Select the language (default: en, available: ru).
- `-e, --exclude`: List of words to exclude from the analysis (e.g., stop words).
- `-t, --top`: Number of top words to display.
- `-p, --participants`: Show participant statistics.
- `-m, --messages`: Show message statistics.
- `-w, --words`: Show word statistics.
- `-mc, --media_content`: Show media content statistics.

---

## Examples 📊

Here’s an example of how to use the tool to analyze your chat:

```bash
python telegram_chat_explorer.py -f my_chat.json -t 10 -m -p
```

This command will analyze the chat from the `my_chat.json` file, display the top 10 words, message statistics, and participant information.  
(Screenshots demonstrating output can be added in the future!)

---

## Requirements 🔧

- Python version >= 3.x
- Install dependencies via `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```
  
---
## 📂 Project Structure

```bash
TelegramChatExplorer/
│
├── src/                # Source folder containing core logic
│   ├── analyzer.py     # Module responsible for data analysis and chat processing
│   ├── config.py       # Handles configuration management and parameters
│   ├── utils.py        # Utility functions for various helper tasks
│
├── tce.py              # Entry point script to run the Telegram Chat Explorer
├── requirements.txt    # Dependencies and required libraries for the project
│
└── README.md           # Project overview, structure, and instructions
```

---

## Contributing 🤝

We welcome contributions! To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License 📜

This project is currently not licensed. Feel free to use and modify for personal projects.

---

### Thank you for using TelegramChatExplorer! 🎉

Now you can easily analyze your Telegram chats and get unique insights into your group or personal conversations. Give it a try, and discover new details in your chat history!
