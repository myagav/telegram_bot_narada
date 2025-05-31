from telegram.constants import ChatAction, ChatMemberStatus
from lib.texts import generate_custom_name
from lib.members import MembersManager


custom_names = {}


async def members_router(update, context):
    chat_id = update.message.chat_id
    members = MembersManager().member_ids
    members_in_chat = await get_chat_members(update, members)
    mention_strings = [
        f"tg://user?id={member.user.id}"
        for member in members_in_chat
        if not member.status == ChatMemberStatus.LEFT
    ]
    custom_names = [generate_custom_name() for _ in members]
    mention_strings = list(
        map(
            lambda mention, names: f"[{names}]({mention})",
            mention_strings,
            custom_names,
        )
    )
    await context.bot.send_chat_action(chat_id, action=ChatAction.TYPING)
    await update.message.reply_text(
        ", ".join(mention_strings) if mention_strings else "немає кого відмічати",
        parse_mode="MarkdownV2",
    )


async def get_chat_members(update, members):
    members_in_chat = []
    for member in members:
        try:
            members_in_chat.append(await update.message.chat.get_member(member))
        except Exception as error:
            continue
    return members_in_chat
