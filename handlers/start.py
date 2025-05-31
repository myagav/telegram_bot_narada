async def start_router(update, context):
    await update.message.reply_text(
        "Привіт! Я нарада ботік :). Ось ліст доступних команд:\n/all - відмітити всіх на нараду\n/quote - рандом цитата студентів\n/joke - анекдоти які ми любимо"
    )
