from aiogram.types import Chat, Message
from quotes.repository import QuotesRepository
from quotes.cards.templates.random import random_quote_card_template
from keyboards.inline.quote_card import random_next


class RandomQuoteCardSender:
    @staticmethod
    async def send(message: Message):
        quote = await QuotesRepository().get_random()
        await message.answer(text=random_quote_card_template.format(
                                header="Nice!",
                                quote=quote.body,
                                hint="Tap on text to copy"
                            ), reply_markup=random_next)

    @staticmethod
    async def replace(message: Message):
        quote = await QuotesRepository().get_random()
        await message.edit_text(text=random_quote_card_template.format(
                                        header="Nice!",
                                        quote=quote.body,
                                        hint="Tap on text to copy"), reply_markup=random_next)
