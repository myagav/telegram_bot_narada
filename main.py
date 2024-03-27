from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.constants import ChatAction, ChatMemberStatus
from telegram import Update
import random
from config import TOKEN
import json

MEMBER_IDS = set()

async def start(update, context):
    await update.message.reply_text("Привіт! Я нарада ботік :). Ось ліст доступних команд:\n/all - відмітити всіх на нараду\n/quote - рандом цитата студентів\n/joke - анекдоти які ми любимо")

async def all_members(update, context):
    chat_id = update.message.chat_id
    members = MEMBER_IDS
    members_in_chat = [await update.message.chat.get_member(member) for member in members]
    mention_strings = [f"tg://user?id={member.user.id}" for member in members_in_chat if not member.status == ChatMemberStatus.LEFT]
    custom_names = [generate_custom_name() for _ in members_in_chat]
    mention_strings = list(map(lambda mention, names: f"[{names}]({mention}),", mention_strings, custom_names))
    await context.bot.send_chat_action(chat_id, action=ChatAction.TYPING)
    await update.message.reply_text(' '.join(mention_strings), parse_mode="MarkdownV2")

custom_names = {}

def generate_custom_name():
    # Генерація облікового запису для олімпіади
    adjective = random.choice(["страшний", "неперевершениий", "анімє", "засмаглива", "аборигенний", "смачний", "антропометричний", "щільний", "гейський", "ангорський", "аґро", "няшка", "вумен", "мен", "звільненний", "недоторканний", "на Бахмут", "на Авдіївку", "зековський", "кліматичний"])
    noun = random.choice(["гей", "порося", "кішечка", "мама", "юра", "карев", "саня", "азов", "камера", "семпай", "с-300", "крим наш", "геноцид", "бандера", "придатний на війну", "чмобік", "олех", "мобілка", "світ", "коханий"])
    return f"{adjective} {noun}"

# Список цитат студентів
quotes = [
    "я повісився щоб не йти на пару",
    "я не хочу просинатись та йти до медведєвої",
    "що робити коли тебе грузе Голев?",
    "я не хочу робити роботу",
    "мамі своєї покажеш",
    "тобі більше всіх треба?",
    "навіщо ти мене ображаєш? В школі не навчили?",
    "яка пара в мене бізнеси",
    "допомагаємо та не кидаємо в біде",
]

async def quote(update, context):
    random_quote = random.choice(quotes)
    await update.message.reply_text(random_quote)

async def custom_joke(update, context):
    custom_quotes = [
        "топ 2 знаки зодіаку. 1 - близнюки. 2 - 11 вересня",
        "переходила бабка не на той світ а опинилась на тому",
        "я точно все здам",
        "негри кинули пити й ти зможеш",
        "мені вистачає стипендії на життя",
        "я точно все здам голеву",
    ]
    
    joke = random.choice(custom_quotes)
    await update.message.reply_text(joke)

async def read_member_id(update, context):
    global MEMBER_IDS
    if update.message.from_user.id not in MEMBER_IDS:
        MEMBER_IDS.add(update.message.from_user.id)
        with open("./members.json", "w") as file:
            file.write(json.dumps(list(MEMBER_IDS)))


def main():
    global MEMBER_IDS
    with open("members.json", "r") as members_file:
        members_list = json.load(members_file)
    MEMBER_IDS = set(members_list)
    updater = Application.builder().token(TOKEN).build()

    updater.add_handler(CommandHandler("start", start))
    updater.add_handler(CommandHandler("all", all_members))
    updater.add_handler(CommandHandler("quote", quote))
    updater.add_handler(CommandHandler("joke", custom_joke))
    updater.add_handler(MessageHandler(filters.ALL, read_member_id))

    updater.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
