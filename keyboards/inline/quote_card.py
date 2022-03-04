from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.callback_data.quote_card.callback import next, previous, random_next

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Next', callback_data=next.new())]
    ]
)

default = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Previous', callback_data=previous.new()),
            InlineKeyboardButton(text='Next', callback_data=next.new())
        ]
    ]
)

last = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Next', callback_data=next.new())]
    ]
)

random_next = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Next', callback_data=random_next.new())]
    ]
)