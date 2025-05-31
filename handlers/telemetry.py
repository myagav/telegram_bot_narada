from lib.members import update_member_id


async def telemetry_router(update, context):
    update_member_id(update.message.from_user.id)
