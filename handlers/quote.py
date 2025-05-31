from lib.texts import get_random_quote


async def quote_router(update, context):
    await random_quote_action(update, context)


async def random_quote_action(update, context):
    await update.message.reply_text(get_random_quote)
