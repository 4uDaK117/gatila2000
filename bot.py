import os
from groq import Groq  # Змінили бібліотеку на Groq
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# 1. Твої ключі (Вставлено напряму для 100% спрацювання)
GROQ_KEY = "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"
TELEGRAM_TOKEN = "8609235826:AAHNaHMPzaeWX22kOXiESuttZ6WzUwPTwpE"

# 2. Ініціалізація клієнта Groq
client = Groq(api_key=GROQ_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    await update.message.reply_text(
        "😎 Мачо-бот активований! Що там написала краля? Розберемо по фактах."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    user_text = update.message.text

    try:
        # Ефект "друкує" в Телеграмі
        if update.effective_chat:
            await context.bot.send_chat_action(
                chat_id=update.effective_chat.id, action="typing"
            )

        # ЗАМІНЕНО НА АКТУАЛЬНУ МОДЕЛЬ llama-3.3-70b-versatile
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Ти харизматичний, впевнений мачо. Пиши коротко, впевнено, з гумором, українською мовою.",
                },
                {
                    "role": "user",
                    "content": f"Дівчина написала: '{user_text}'. Дай варіант відповіді.",
                },
            ],
        )

        reply = (
            response.choices[0].message.content
            or "Помилка: порожня відповідь від моделі"
        )
        await update.message.reply_text(reply)

    except Exception as e:
        # Якщо ключ Groq видасть помилку, ми побачимо її тут
        await update.message.reply_text(f"⚠️ Помилка Groq: {str(e)}")


def main():
    # Створюємо додаток Telegram
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Додаємо команди та обробку тексту
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 БОТ НА GROQ ЗАПУЩЕНИЙ! Перевіряй Telegram.")
    app.run_polling()


if __name__ == "__main__":
    main()
