from lib.members import MembersManager


async def telemetry_router(update, context):
    MembersManager().update_member_id(update.message.from_user.id)
