"""
Everything what's in this module, should interact with lib and telegram
"""

from telegram.ext import CommandHandler, MessageHandler, filters
# NOTE: ensure telegram.ext installed

from .call import members_router
from .start import start_router
from .quote import quote_router
from .joke import joke_router
from .telemetry import telemetry_router

# NOTE: Command handlers
start_handler = CommandHandler("start", start_router)
members_handler = CommandHandler("all", members_router)
quote_handler = CommandHandler("quote", quote_router)
joke_handler = CommandHandler("joke", joke_router)

# NOTE: Message handlers
telemetry_handler = MessageHandler(filters.ALL, telemetry_router)
