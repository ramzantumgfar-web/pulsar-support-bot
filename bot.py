import telebot
from telebot import types

from config import TOKEN, ADMIN_ID
from database import add_user, get_users_count
from knowledge import KNOWLEDGE
from ai import ai_answer
from tickets import create_ticket


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
        "🧠 AI помощь",
        "🎫 Создать тикет"
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
        "Я помогу решить проблему с сервером.\n"
        "Выберите раздел или опишите проблему.",
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

🎫 Система тикетов: 🟢 Включена

🤖 Бот: Онлайн
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


    # Создание тикета
    if "тикет" in text or "🎫" in text:

        ticket_id = create_ticket(
            message.from_user.id,
            message.from_user.username,
            message.text
        )

        bot.send_message(
            message.chat.id,
            f"""
🎫 Тикет создан!

Номер заявки: #{ticket_id}

Администратор PulSar Host скоро рассмотрит проблему.
"""
        )

        bot.send_message(
            ADMIN_ID,
            f"""
🔔 Новый тикет!

Номер: #{ticket_id}

Пользователь:
@{message.from_user.username}

Проблема:
{message.text}
"""
        )

        return


    # Проверка базы знаний
    for problem, answer in KNOWLEDGE.items():

        if problem in text:

            bot.send_message(
                message.chat.id,
                answer
            )

            return


    # AI помощь
    bot.send_message(
        message.chat.id,
        ai_answer(text)
    )


print("🚀 PulSar Host Support AI Ultimate запущен")

bot.infinity_polling()
