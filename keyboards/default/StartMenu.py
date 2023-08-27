from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Boshmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Darslar📚"),
            KeyboardButton(text="info🧾"),

        ],
        [
            KeyboardButton(text="👩🏻‍🏫Attestatsiya👨🏻‍🏫"),
        ],
        [
            KeyboardButton(text="Programalar🖥"),
        ],
        [
            KeyboardButton(text="Изменить язык⚙"),
        ],
    ],
    resize_keyboard=True,
)


ruBoshmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Общие уроки📚"),
            KeyboardButton(text="инфо🧾"),

        ],
                [
            KeyboardButton(text="Программы🖥"),
        ],
        [
            KeyboardButton(text="Tilni o\'zgartirish⚙"),
        ],
    ],
    resize_keyboard=True,
)


