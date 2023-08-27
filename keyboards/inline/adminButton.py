from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Yaratuvchi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="‼Yaratuvchi‼", callback_data="Yaratuv"),
        ],

    ])

Yaratuvchiru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="‼Создатель‼", callback_data="Yaratuvru"),
        ],
    ])

Til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="RU 🇷🇺", callback_data="RusTil"),
            InlineKeyboardButton(text="UZ 🇺🇿", callback_data="UzTil"),
        ],
    ])
