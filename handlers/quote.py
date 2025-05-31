from handlers.utils import is_admin
from lib.texts import get_random_quote, TextManager


async def quote_router(update, context):
    request = update.message.text.split()
    if len(request) == 1:
        action = "random_quote"
    elif len(request) == 2:
        _, action = request
        if action != "list":
            action = "invalid_action"
    elif len(request) >= 3:
        _, action, *args = request

    match action:  # type: ignore
        case "random_quote":  # NOTE: 1 Arg
            await random_quote_action(update=update)
        case "list":  # NOTE: 2 Args
            await list_quote_action(update=update)
        case "add":  # NOTE: 3 Args
            await add_quote_action(update=update, text=" ".join(args))  # type: ignore
        case "remove":
            await remove_quote_action(update=update, text_id=args[0])  # type: ignore
        case "invalid_action":
            await error_quote_action(update=update)


async def random_quote_action(update):
    await update.message.reply_text(get_random_quote())


async def add_quote_action(update, text: str):
    if not is_admin(update.message.from_user.id):
        await random_quote_action(update=update)

    tm = TextManager()
    tm.add_text(text=text, t_type="quote")
    await update.message.reply_text("цитату додано")


async def list_quote_action(update):
    if not is_admin(update.message.from_user.id):
        await random_quote_action(update=update)

    tm = TextManager()
    responses = []
    responses.append("список цитат:\n")
    for quote in tm.quotes:
        responses.append(f"ID: {quote.id}: {quote.text}")

    await update.message.reply_text("\n".join(responses))


async def remove_quote_action(update, text_id: str):
    if not is_admin(update.message.from_user.id):
        await random_quote_action(update=update)

    tm = TextManager()
    try:
        text_to_remove = tm.get_text(text_id)
    except KeyError:
        await update.message.reply_text("цитати не існує (житомир?)")
        return

    if text_to_remove.type == "quote":
        tm.remove_text(text_id=text_id)
        await update.message.reply_text("цитату видалено")
    else:
        await update.message.reply_text("цитати не існує (житомир?)")


async def error_quote_action(update):
    await update.message.reply_text("не робе")
