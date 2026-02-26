# Telegram Groq Chatbot

This repository contains a simple Telegram bot implemented in Python. It uses the Groq API to process user messages and generate responses with a model.

## Setup

1. Install Git (if not already installed).
2. Clone or initialize the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Install dependencies (e.g., `pip install python-telegram-bot groq`).
4. Run the bot:
   ```bash
   python bot.py
   ```

## Configuration

- `GROQ_KEY` and `TELEGRAM_TOKEN` are hardcoded in `bot.py` for simplicity.

## Notes

- Ensure you have a valid Groq API key and Telegram bot token.
- Keep credentials secure in a real project by using environment variables.