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
        """
🚀 PulSar Host Support AI

Ваш помощник по игровым серверам.

Выберите раздел:
        """,
        reply_markup=menu()
    )


@bot.message_handler(commands=["admin"])
def admin(message):

    if message.from_user.id == ADMIN_ID:

        bot.send_message(
            message.chat.id,
            f"""
👑 PulSar Host Admin

👥 Пользователей: {get_users_count()}

🤖 Бот: Online
"""
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
        ai_answer(text)
    )


print("🚀 PulSar Host Support AI запущен")

bot.infinity_polling()
