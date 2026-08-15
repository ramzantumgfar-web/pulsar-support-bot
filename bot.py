import telebot

TOKEN = "8896894096:AAGRKjS_b3jxwnlndIaS8OMuzSNSaEASRQU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🚀 PulSar Host Support\n\n"
        "Привет! Я бот технической поддержки.\n"
        "Опиши свою проблему, и я помогу разобраться."
    )

@bot.message_handler(func=lambda message: True)
def support(message):
    text = message.text.lower()

    if "ошибка" in text or "error" in text:
        answer = (
            "🔍 Попробуй отправить:\n"
            "1. Текст ошибки\n"
            "2. Логи консоли\n"
            "3. Версию игры и сервера"
        )
    elif "сервер" in text:
        answer = (
            "🎮 Проверим сервер.\n"
            "Убедись, что сервер запущен и отправь ошибку из консоли."
        )
    else:
        answer = (
            "📩 Заявка принята.\n"
            "Опиши проблему подробнее, и мы поможем."
        )

    bot.send_message(message.chat.id, answer)

print("PulSar Host Support запущен")

bot.infinity_polling()
