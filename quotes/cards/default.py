from aiogram.types.message import Message, Chat
from keyboards.inline.quote_card import default


class DefaultCardSender:
    @staticmethod
    async def send(chat: Chat, quote):
        text = f"""
<i>Nice!</i>

<code>{quote.body}</code>

<b>Tap on text to copy</b>

1/1
        """
        await chat.bot.send_message(chat_id=chat.id, text=text, reply_markup=default)