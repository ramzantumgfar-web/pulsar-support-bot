import telebot
from telebot import types

from config import TOKEN, ADMIN_ID
from database import add_user, get_users_count
from knowledge import KNOWLEDGE
from ai import ai_answer
from tickets import create_ticket, get_user_tickets, close_ticket


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
        """
🚀 PulSar Host Support AI Ultimate

Ваш цифровой помощник по игровым серверам.

Выберите раздел или опишите проблему.
        """,
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

🎫 Тикеты: включены

🤖 Статус: Online
"""
        )

    else:

        bot.send_message(
            message.chat.id,
            "❌ Нет доступа"
        )


@bot.message_handler(commands=["mytickets"])
def mytickets(message):

    tickets = get_user_tickets(
        message.from_user.id
    )

    if not tickets:

        bot.send_message(
            message.chat.id,
            "🎫 У вас нет тикетов."
        )

        return


    text = "🎫 Ваши тикеты:\n\n"

    for ticket in tickets:

        text += (
            f"#{ticket[0]}\n"
            f"Проблема: {ticket[3]}\n"
            f"Статус: {ticket[4]}\n"
            f"Дата: {ticket[5]}\n\n"
        )


    bot.send_message(
        message.chat.id,
        text
    )


@bot.message_handler(commands=["close"])
def close(message):

    try:

        ticket_id = int(
            message.text.split()[1]
        )

        close_ticket(ticket_id)

        bot.send_message(
            message.chat.id,
            f"✅ Тикет #{ticket_id} закрыт."
        )


    except:

        bot.send_message(
            message.chat.id,
            "Используй:\n/close номер_тикета"
        )



@bot.message_handler(func=lambda message: True)
def support(message):

    text = message.text.lower()


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

Администратор скоро ответит.
"""
        )


        bot.send_message(
            ADMIN_ID,
            f"""
🔔 Новый тикет

Номер: #{ticket_id}

Пользователь:
@{message.from_user.username}

Проблема:
{message.text}
"""
        )

        return



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



print("🚀 PulSar Host Support AI Ultimate запущен")

bot.infinity_polling()
