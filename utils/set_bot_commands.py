from commands import all_commands


async def set_default_commands(dp):
    await dp.bot.set_my_commands(commands=all_commands)
