from telegram.ext import Application
from telegram import Update
from config import TOKEN

from handlers import (
    start_handler,
    members_handler,
    quote_handler,
    joke_handler,
    telemetry_handler,
)
from lib.members import MembersManager
from lib.texts import TextManager


def main():
    updater = Application.builder().token(TOKEN).build()

    # Singleton init
    MembersManager(config={"members_path": "./members.json"})
    TextManager(config={"texts_path": "./texts.json"})

    # NOTE: Command handlers
    updater.add_handler(start_handler)
    updater.add_handler(members_handler)
    updater.add_handler(quote_handler)
    updater.add_handler(joke_handler)
    # NOTE: Message handlers
    updater.add_handler(telemetry_handler)

    updater.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
