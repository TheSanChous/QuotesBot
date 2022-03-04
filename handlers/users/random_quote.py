from loader import dp
from quotes.repository import QuotesRepository
from quotes.cards.random import RandomQuoteCardSender
from aiogram.types import Message, CallbackQuery
from keyboards.callback_data.quote_card.callback import random_next


@dp.message_handler(commands=["random"])
async def random_command_handler(message: Message):
    await RandomQuoteCardSender().send(message)


@dp.callback_query_handler(random_next.filter())
async def random_command_handler(callback: CallbackQuery):
    await callback.answer(cache_time=1)
    await RandomQuoteCardSender().replace(callback.message)
