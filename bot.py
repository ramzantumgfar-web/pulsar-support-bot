import telebot
from telebot import types
from config import TOKEN, ADMIN_ID
from knowledge import KNOWLEDGE

bot = telebot.TeleBot(TOKEN)

users = set()


def create_menu():
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "🎮 Ошибка сервера",
        "📡 Подключение"
    )

    keyboard.add(
        "🐌 Лаги",
        "⚙️ Моды"
    )

    keyboard.add(
        "🧠 AI Помощь"
    )

    return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    users.add(message.from_user.id)

    bot.send_message(
        message.chat.id,
        "🚀 PulSar Host Support AI\n\n"
        "Я помогу решить проблему с сервером.",
        reply_markup=create_menu()
    )


@bot.message_handler(commands=["admin"])
def admin(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(
            message.chat.id,
            f"👑 Админ панель\n\n"
            f"Пользователей: {len(users)}\n"
            f"Статус: 🟢 Онлайн"
        )
    else:
        bot.send_message(
            message.chat.id,
            "❌ Нет доступа"
        )


@bot.message_handler(func=lambda message: True)
def support(message):

    text = message.text.lower()

    for problem, answer in KNOWLEDGE.items():

        if problem in text:
            bot.send_message(
                message.chat.id,
                answer
            )
            return


    bot.send_message(
        message.chat.id,
        "🤖 Я не нашёл решение.\n\n"
        "Напиши:\n"
        "🎮 Какая игра?\n"
        "📜 Какая ошибка?\n"
        "🖥 Отправь лог."
    )


print("PulSar Host Support AI запущен")

bot.infinity_polling()
