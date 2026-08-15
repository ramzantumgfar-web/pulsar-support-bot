def ai_answer(text):

    text = text.lower()

    if "minecraft" in text:
        return (
            "🎮 Minecraft режим\n\n"
            "Отправь:\n"
            "• версию сервера\n"
            "• ошибку\n"
            "• лог консоли"
        )

    if "rust" in text:
        return (
            "🎮 Rust режим\n\n"
            "Отправь ошибку запуска или настройки сервера."
        )

    if "cs" in text:
        return (
            "🎮 CS режим\n\n"
            "Проверь SteamCMD, файлы сервера и конфиг."
        )

    return (
        "🧠 AI помощник PulSar Host\n\n"
        "Мне нужна информация:\n"
        "1. Какая игра?\n"
        "2. Какая ошибка?\n"
        "3. Что произошло?"
    )
