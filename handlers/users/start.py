from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.Boshmenu import Sinflar, klass
from keyboards.inline.azobolish import ObunaButton
from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from keyboards.default.StartMenu import *
from keyboards.inline.adminButton import Yaratuvchi, Yaratuvchiru, Til
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.Birsinfkitoblar import *
from keyboards.inline.programms import *

keyboard2 = types.ReplyKeyboardRemove()


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_file_id_p(message: types.Message):
    await message.reply(message.document.file_id)


NOTSUB_MESSAGE = "‼Подпишись на канал, чтобы бот заработал‼\n‼Bot ishlashi uchun kanalga obuna bo'ling‼ \n\n👉🏻@DarsInformatika👈🏻"


def check_Sub_channel(chat_member):
    print(chat_member["status"])
    if chat_member["status"] != "left":
        return True
    else:
        return False


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.chat.type == "private":
        if check_Sub_channel(await bot.get_chat_member(chat_id="@DarsInformatika", user_id=message.from_user.id)):
            photo_id = "AgACAgIAAxkBAAIUV2MDzl7snZ6iweRJ1hbT11wpX-yqAAIQwzEbe2UhSDemMIqqHJhzAQADAgADcwADKQQ"
            await message.answer_photo(photo_id, caption=f"""🖐🏻Salom, {message.from_user.full_name}!
Bizning Bot Informatika bo'yicha ma'lumotlarni va g'oyalarni tarqatishga mo'ljallangan 

Bot videodarslar va kitoblarni izlashda vaqtingizni tejaydi 

Shu bilan birga attestatsiya savollariga tayyorlanishga ko'makchidir

🎥Video - 267 dona 
📚Kitob - 22 dona (UZ|RU)
📝Testlar - 22 dona
📋Ish rejasi hamma sinflar uchun 

➖➖➖➖➖➖➖➖➖
🖐🏻Привет, {message.from_user.full_name}!

Наш бот предназначен для реализации идей и информации по предмету Информатика.

Бот может сэкономить ваше время в поиске учебника и видео уроков.

Также поможет подготовиться к аттестации 

🎥Видео - 267 штук
📚Книги - 22 штук (UZ|RU)
📝Тесты - 22 штук
📋План Работы для всех классов 
""", reply_markup=Boshmenu)
            await message.delete()
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=ObunaButton)


@dp.callback_query_handler(text="Obuna")
async def Obunabulish(call: CallbackQuery):
    if check_Sub_channel(await bot.get_chat_member(chat_id="@DarsInformatika", user_id=call.message.chat.id)):
        photo_id = "AgACAgIAAxkBAAIUV2MDzl7snZ6iweRJ1hbT11wpX-yqAAIQwzEbe2UhSDemMIqqHJhzAQADAgADcwADKQQ"
        await call.message.answer_photo(photo_id, caption=f"""🖐🏻Salom {call.message.chat.full_name}
 
Bizning Bot Informatika bo'yicha ma'lumotlarni va g'oyalarni tarqatishga mo'ljallangan 

Bot videodarslar va kitoblarni izlashda vaqtingizni tejaydi 

Shu bilan birga attestatsiya savollariga tayyorlanishga ko'makchidir

🎥Video - 267 dona 
📚Kitob - 22 dona (UZ|RU)
📝Testar - 22 dona
📋Ish rejasi hamma sinflar uchun

➖➖➖➖➖➖➖➖➖
🖐🏻Привет, {call.message.chat.full_name}!

Наш бот предназначен для реализации идей и информации по предмету Информатика.

Бот может сэкономить ваше время в поиске учебника и видео уроков.

Также поможет подготовиться к аттестации 

🎥Видео - 267 штук
📚Книги - 22 штук ( UZ | RU )
📝Тесты - 22 штук
📋План Работы для всех классов 

""", reply_markup=Boshmenu)
        await call.message.delete()
    else:
        await bot.send_message(call.message.chat.id, NOTSUB_MESSAGE, reply_markup=ObunaButton)
        await call.message.delete()


@dp.message_handler()
async def FiltrBosh(message: types.Message):
    if message.text == "Darslar📚":
        await message.answer("Iltimos sinfni tanglang👇🏻", reply_markup=Sinflar)
        await message.delete()
    elif message.text == "info🧾":
        await message.answer("""
Ma'lumot:
Bizning Bot Informatika bo'yicha ma'lumotlarni va g'oyalarni tarqatishga mo'ljallangan 

Bot videodarslar va kitoblarni izlashda vaqtingizni tejaydi 

Shu bilan birga attestatsiya savollariga tayyorlanishga ko'makchidir

🎥Video - 267 dona 
📚Kitob - 22 dona ( UZ | RU )
📝Testar - 22 dona

Admin: @Ferkka""", reply_markup=Yaratuvchi)
        await message.delete()
    elif message.text == "Изменить язык⚙":
        await message.answer("Выберите язык", reply_markup=Til)
        await message.answer("Языки указаны наверху", reply_markup=keyboard2)
        await message.delete()
    elif message.text == "Общие уроки📚":
        await message.answer("Пожалуйста выберите класс👇🏻", reply_markup=klass)
        await message.delete()
    elif message.text == "инфо🧾":
        await message.answer(
            "Информация:\nНаш бот предназначен для реализации идей и информации по предмету Информатика.\n\nБот может сэкономить ваше время в поиске учебника и видео уроков.\n\nТакже поможет подготовиться к аттестации\n\n🎥Видео - 267 штук\n📚Книги - 22 штук (UZ|RU)\n📝Тесты - 22 штук\n📋План Работы для всех классов \n\nАдмины:@Ferkka",
            reply_markup=Yaratuvchiru)
        await message.delete()
    elif message.text == "Tilni o\'zgartirish⚙":
        await message.answer("Til Tanglang", reply_markup=Til)
        await message.answer("Tillar yuqorida ko'rsatilgan", reply_markup=keyboard2)
        await message.delete()
    elif message.text == "👩🏻‍🏫Attestatsiya👨🏻‍🏫":
        await message.answer("👇🏻Iltimos qanaqa ma\'lumot kerakligini tanglang👇🏻", reply_markup=Attmenu),
        await message.answer("👆🏻Ma'lumotlar yuqorida ko\'rsatilgan👆🏻",reply_markup=keyboard2)
        await message.delete()
    elif message.text == "Programalar🖥":
        await message.answer("👇🏻Iltimos qanaqa Programa kerakligini tanglang👇🏻", reply_markup=Program)
        await message.answer("👆🏻Programalar yuqorida ko\'rsatilgan👆🏻", reply_markup=keyboard2)
        await message.delete()
    elif message.text == "Программы🖥":
        await message.answer("👇🏻Выберите программу👇🏻", reply_markup=Programru)
        await message.answer("👆🏻Программы указаны наверху👆🏻", reply_markup=keyboard2)
        await message.delete()
    else:
        await message.answer(
            "‼Sizni tushunmadim, Iltimos menyudagi bo\'limidan tanglang ‼\n ‼Я вас не понял, Пожалуйста выберите пункт из меню‼")


@dp.callback_query_handler(text="RusTil")
async def nazad(call: CallbackQuery):
    await call.message.answer("Язык Изменен", reply_markup=ruBoshmenu)
    await call.message.delete()


@dp.callback_query_handler(text="UzTil")
async def nazad(call: CallbackQuery):
    await call.message.answer("Til o\'zgardi", reply_markup=Boshmenu)
    await call.message.delete()
