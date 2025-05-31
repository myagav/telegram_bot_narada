from lib.texts import get_random_joke, TextManager


async def joke_router(update, context):
    command, action, text = update.message.text.split()
    match action:
        case "add":
            await add_joke_action(update=update, text=text)
        case "list":
            await list_joke_action(update=update)
        case _:
            await random_joke_action(update=update)


async def random_joke_action(update):
    await update.message.reply_text(get_random_joke())


async def add_joke_action(update, text: str):
    tm = TextManager()
    tm.add_text(text=text, type_="joke")
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
    text_id = int(text_id)
    try:
        text_to_remove = tm.get_text(text_id)
    except KeyError:
        update.message.reply_text("жарт не існує (житомир?)")
        return

    if text_to_remove.type == "joke":
        tm.remove_text(text_id=text_id)
        update.message.reply_text("жарт видалено")
    else:
        update.message.reply_text("жарт не існує (житомир?)")
