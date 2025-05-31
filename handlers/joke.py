from lib.texts import get_random_joke, TextManager


async def joke_router(update, context):
    request = update.message.text.split()
    if len(request) == 1:
        action = "random_joke"
    elif len(request) == 2:
        _, action = request
        if action != "list":
            action = "invalid_action"
    elif len(request) >= 3:
        _, action, *args = request

    match action:  # type: ignore
        case "random_joke":  # NOTE: 1 Arg
            await random_joke_action(update=update)
        case "list":  # NOTE: 2 Args
            await list_joke_action(update=update)
        case "add":  # NOTE: 3 Args
            await add_joke_action(update=update, text=" ".join(args))  # type: ignore
        case "remove":
            await remove_joke_action(update=update, text_id=args[0])  # type: ignore
        case "invalid_action":
            await error_joke_action(update=update)


async def random_joke_action(update):
    await update.message.reply_text(get_random_joke())


async def add_joke_action(update, text: str):
    tm = TextManager()
    tm.add_text(text=text, t_type="joke")
    await update.message.reply_text("жарт додано")


async def list_joke_action(update):
    tm = TextManager()
    responses = []
    responses.append("список жартів:\n")
    for joke in tm.jokes:
        responses.append(f"ID: {joke.id}: {joke.text}")

    await update.message.reply_text("\n".join(responses))


async def remove_joke_action(update, text_id: str):
    tm = TextManager()
    try:
        text_to_remove = tm.get_text(text_id)
    except KeyError:
        await update.message.reply_text("жарт не існує (житомир?)")
        return

    if text_to_remove.type == "joke":
        tm.remove_text(text_id=text_id)
        await update.message.reply_text("жарт видалено")
    else:
        await update.message.reply_text("жарт не існує (житомир?)")


async def error_joke_action(update):
    await update.message.reply_text("не робе")

