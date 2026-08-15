import telebot

TOKEN = "8896894096:AAGRKjS_b3jxwnlndIaS8OMuzSNSaEASRQU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🚀 PulSar Host Support\n\n"
        "Привет! Я автоматический помощник хостинга.\n"
        "Опиши проблему, и я попробую помочь."
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🛠 Я могу помочь с:\n\n"
        "🎮 Сервер не запускается\n"
        "📡 Проблемы с подключением\n"
        "⚙️ Ошибки модов и плагинов\n"
        "🐌 Лаги сервера\n"
        "📋 Ошибки консоли"
    )

@bot.message_handler(func=lambda message: True)
def support(message):
    text = message.text.lower()

    if "не запускается" in text or "не стартует" in text:
        answer = (
            "🔴 Сервер не запускается.\n\n"
            "Попробуй:\n"
            "1. Проверить последнюю ошибку в консоли.\n"
            "2. Проверить файлы сервера.\n"
            "3. Перезапустить сервер."
        )

    elif "лаг" in text or "лаги" in text:
        answer = (
            "🐌 Проблемы с лагами.\n\n"
            "Проверь:\n"
            "1. Использование RAM.\n"
            "2. Количество игроков.\n"
            "3. Лишние плагины или моды."
        )

    elif "ошибка" in text or "error" in text:
        answer = (
            "⚠️ Найдена ошибка.\n\n"
            "Отправь:\n"
            "• полный текст ошибки\n"
            "• лог консоли\n"
            "• версию игры"
        )

    elif "подключ" in text or "зайти" in text:
        answer = (
            "📡 Проблема с подключением.\n\n"
            "Проверь:\n"
            "1. IP сервера.\n"
            "2. Версию клиента.\n"
            "3. Интернет-соединение."
        )

    else:
        answer = (
            "🤖 Я пока не нашёл решение.\n\n"
            "Опиши проблему подробнее:\n"
            "• какая игра?\n"
            "• какая ошибка?\n"
            "• что произошло?"
        )

    bot.send_message(message.chat.id, answer)

print("PulSar Host Support запущен")

bot.infinity_polling()
