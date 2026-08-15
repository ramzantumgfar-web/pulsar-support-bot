import telebot
from telebot import types

from config import TOKEN, ADMIN_ID
from database import add_user, get_users_count
from knowledge import KNOWLEDGE
from ai import ai_answer


bot = telebot.TeleBot(TOKEN)


def menu():
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "🎮 Игра",
        "📜 Лог"
    )

    keyboard.add(
        "🧠 AI помощь"
    )

    return keyboard


@bot.message_handler(commands=["start"])
def start(message):

    add_user(
        message.from_user.id,
        message.from_user.username
    )

    bot.send_message(
        message.chat.id,
        "🚀 PulSar Host Support AI Ultimate\n\n"
        "Ваш виртуальный инженер поддержки.\n"
        "Опишите проблему или выберите раздел.",
        reply_markup=menu()
    )


@bot.message_handler(commands=["admin"])
def admin(message):

    if message.from_user.id == ADMIN_ID:

        bot.send_message(
            message.chat.id,
            f"""
👑 PulSar Host Admin Panel

👥 Пользователей: {get_users_count()}

🤖 Статус:
🟢 Бот работает
"""
        )

    else:

        bot.send_message(
            message.chat.id,
            "❌ У вас нет доступа."
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


    answer = ai_answer(text)

    bot.send_message(
        message.chat.id,
        answer
    )


print("🚀 PulSar Host Support AI Ultimate запущен")

bot.infinity_polling()
