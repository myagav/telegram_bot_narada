from lib.texts import get_random_joke


async def joke_router(update, context):
    await random_joke_action(update, context)


async def random_joke_action(update, context):
    await update.message.reply_text(get_random_joke)
