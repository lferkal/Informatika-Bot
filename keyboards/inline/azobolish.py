from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ObunaButton = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Men obuna bo\'ldim / Я подписался ✅ ", callback_data="Obuna"),

        ],
        [
            InlineKeyboardButton(text="👉🏻Kanal👈🏻", url="https://t.me/DarsInformatika"),
        ],
    ])

