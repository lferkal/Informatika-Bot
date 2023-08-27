from aiogram import types
from aiogram.types import CallbackQuery, Message
from loader import dp, bot
from keyboards.inline.Birsinfkitoblar import *
from keyboards.default.Boshmenu import klass, Sinflar
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.StartMenu import Boshmenu, ruBoshmenu
from keyboards.inline.adminButton import Yaratuvchi
from keyboards.inline.programms import Program

keyboard2 = types.ReplyKeyboardRemove()


@dp.callback_query_handler(text="Yaratuv")
async def Yarat(call: CallbackQuery):
    photo_id = "AgACAgIAAxkBAAIUomMD1S-6AVcGL0XYkWufo4qYzOZmAAJnwDEbNQggSOBIJlBwHX_cAQADAgADcwADKQQ"
    await call.message.answer_photo(photo_id,
                                    caption="Dasturlovchi: Surxondaryo viloyati Denov tuman 74-Maktabning 8\"A\" sinf o'quvchisi Abdullayev Firuzbek")


@dp.callback_query_handler(text="Yaratuvru")
async def Yarat(call: CallbackQuery):
    photo_id = "AgACAgIAAxkBAAIUomMD1S-6AVcGL0XYkWufo4qYzOZmAAJnwDEbNQggSOBIJlBwHX_cAQADAgADcwADKQQ"
    await call.message.answer_photo(photo_id,
                                    caption="Создатель: Ученик 8\"A\" класса Школы №74 города Денау Сурхандаринской облости Абдуллаев Фирузбек")


@dp.callback_query_handler(text="5Kitobuz")
async def KitobBesh(call: CallbackQuery):
    KitobBeshsinf = 'BQACAgIAAxkBAANXYvjlPNijUKYc2_IIqM51eXQlDiIAAkwcAAL4F8lLGFWKpsJA4dApBA'
    await call.message.reply_document(KitobBeshsinf)


@dp.callback_query_handler(text="6Kitobuz")
async def KitobBesh(call: CallbackQuery):
    Kitoboltisinf = 'BQACAgIAAxkBAAN3Yvkz0Rr2HUwBo1RIUVxCm_Fk2ncAAsoVAAJU8uBJXyKJFONLknApBA'
    await call.message.reply_document(Kitoboltisinf)


@dp.callback_query_handler(text="7Kitobuz")
async def KitobBesh(call: CallbackQuery):
    Kitobyettisinf = 'BQACAgIAAxkBAAN5Yvkz3KByE9afaGCI6-qTjy7bVzIAAssVAAJU8uBJ_H9yMalpp9opBA'
    await call.message.reply_document(Kitobyettisinf)


@dp.callback_query_handler(text="8Kitobuz")
async def KitobBesh(call: CallbackQuery):
    Kitobsaksinf = 'BQACAgIAAxkBAAN3Yvkz0Rr2HUwBo1RIUVxCm_Fk2ncAAsoVAAJU8uBJXyKJFONLknApBA'
    await call.message.reply_document(Kitobsaksinf)


@dp.callback_query_handler(text="9Kitobuz")
async def KitobBesh(call: CallbackQuery):
    Kitobtosinf = 'BQACAgIAAxkBAAN9Yvkz90lgokSuFWz32lflhFIcfRUAAs4VAAJU8uBJOT2oliqLlbApBA'
    await call.message.reply_document(Kitobtosinf)


@dp.callback_query_handler(text="10Kitobuz")
async def KitobBesh(call: CallbackQuery):
    Kitobonsinf = 'BQACAgIAAxkBAAOAYvk0AzOp-jgeoQpi72H-byFHJ30AAtAVAAJU8uBJPI3zDsw49BgpBA'
    await call.message.reply_document(Kitobonsinf)


@dp.callback_query_handler(text="11Kitobuz")
async def KitobBesh(call: CallbackQuery):
    Kitobonbsinf = 'BQACAgIAAxkBAAODYvk0GoHQ8_y7Oi6AyBczoSQWeJcAAtIVAAJU8uBJ6iT_SePQ694pBA'
    await call.message.reply_document(Kitobonbsinf)


################################################################################################################


@dp.message_handler(text="5️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik5)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="6️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik6)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="7️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik7)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="8️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik8)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="9️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik9)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="1️⃣0️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik10)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="1️⃣1️⃣-класс")
async def sinfbir(message: types.Message):
    await message.answer("Выберите преднадлежность ", reply_markup=ruDarslik11)
    await message.answer("👆🏻Предметы указаны наверху👆🏻", reply_markup=keyboard2)


#########################################################################################################


@dp.callback_query_handler(text="nazadSinf10")
async def nazadon(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik10)


@dp.callback_query_handler(text="nazadSinf9")
async def nazadon(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik9)


@dp.callback_query_handler(text="nazadSinf11")
async def nazadon(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik11)


@dp.callback_query_handler(text="nazadru")
async def nazadru(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=klass)


@dp.callback_query_handler(text="nazad")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Sinflar)


@dp.callback_query_handler(text="nazadMenu")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Boshmenu)


@dp.callback_query_handler(text="nazadSinf6")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik6)


@dp.callback_query_handler(text="nazadSinf5")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik5)


@dp.callback_query_handler(text="nazadSinf5ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=ruDarslik5)


@dp.callback_query_handler(text="nazadSinf6ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=ruDarslik6)


@dp.callback_query_handler(text="nazadSinf7ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=ruDarslik7)


@dp.callback_query_handler(text="nazadSinf8ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=ruDarslik8)


@dp.callback_query_handler(text="nazadSinf9ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=ruDarslik9)


@dp.callback_query_handler(text="nazadSinf10ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik10)


@dp.callback_query_handler(text="nazadSinf11ru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik11)


@dp.callback_query_handler(text="nazadSinf7")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik7)


@dp.callback_query_handler(text="nazadSinf8")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Darslik8)


@dp.message_handler(text="⬅ - назад")
async def nazaddeff(message: types.Message):
    await message.answer("Вы вернулись назад", reply_markup=ruBoshmenu)
    await message.delete()


@dp.message_handler(text="⬅ - Orqaga")
async def nazaddeff(message: types.Message):
    await message.answer("Siz orqaga qaytingiz", reply_markup=Boshmenu)
    await message.delete()


@dp.callback_query_handler(text="Attorqaga")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Attnazad")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Attmenu)


@dp.callback_query_handler(text="Programorqaga")
async def nazad(call: CallbackQuery):
    await call.message.answer("Siz orqaga qaytingiz", reply_markup=Program)


@dp.callback_query_handler(text="Attorqagaru")
async def nazad(call: CallbackQuery):
    await call.message.answer("Вы вернулись назад", reply_markup=ruBoshmenu)


###############################################################################################################


@dp.message_handler(text="5️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik5)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="6️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik6)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="7️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik7)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="8️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik8)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="9️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik9)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="1️⃣0️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik10)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)
    await message.delete()


@dp.message_handler(text="1️⃣1️⃣-sinf")
async def sinfbir(message: types.Message):
    await message.answer("👇🏻Qanaqa darslar kerakligini tanglang👇🏻", reply_markup=Darslik11)
    await message.answer("👆🏻Darslar yuqoridagi bo\'limda ko'rsatilgan 👆🏻", reply_markup=keyboard2)


#############################################################################################################

@dp.callback_query_handler(text="Oldingi62")
@dp.callback_query_handler(text="6Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAICG2L7-t1YTOg48h8QzOf22VYEZIq0AAIbHAAC03TZSwWu9TAdXVypKQQ'
    await call.message.reply_video(VDars1, caption="1-dars. Matn muharrirlari")
    video2 = "BAACAgIAAxkBAAICHWL7_GeHlOC6VnfjTYUQwO4bHZ64AAL4GwAC03TZS2AIjPaBxCIdKQQ"
    await call.message.answer_video(
        video2, caption="2-dars. MS Word matn protssesorining interfeysi"
    )
    video3 = "BAACAgIAAxkBAAICH2L7_IDRhk0G1qjnFJz8i-sg5pIsAAIkHAAC03TZS5IDuwXqXl19KQQ"
    await call.message.answer_video(
        video3, caption="3-dars. Hujjatni hosil qilish va saqlash"
    )
    video4 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video4, caption="4-dars. Amaliy mashg'ulot"
    )
    video5 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video5, caption="5-dars. Wordda matn yozish qoidalari"
    )
    video6 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video6, caption="6-dars. Amaliy mashg'ulot"
    )
    video7 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video7, caption="7-dars. Hujjatlarning asosiy parametrlari"
    )
    video8 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video8, caption="8-dars. Amaliy mashg'ulot"
    )
    video9 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video9, caption="9-dars. Amaliy mashg'ulot. Takrorlash"
    )
    video10 = "BAACAgIAAxkBAAICL2L7_hYtvhT4wj4N2bDGGqqi0MtzAAIDGQAC7wrhS_Z12EsWOJCWKQQ"
    await call.message.answer_video(
        video10, caption="10-dars. Hujjatlarni tahrir qilish", reply_markup=DavomVideo61
    )


@dp.callback_query_handler(text="Oldingi63")
@dp.callback_query_handler(text="davom61")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIDBmL8jWeoQZEGWVcK8mciUnuGGUfuAAIqHAAC03TZS2NhhW06d4VsKQQ'
    await call.message.reply_video(VDars1, caption="11-dars. Hujjatlarni tahrir qilish bo'yicha amaliy mashg'ulot")
    video2 = "BAACAgIAAxkBAAIDCmL8kXf4tvoTPtP7Jv9lZyw1ysaZAAIiHAAC03TZSzVpc2fGctOWKQQ"
    await call.message.answer_video(
        video2, caption="12-dars. Hujjatni formatlash"
    )
    video3 = "BAACAgIAAxkBAAIDDmL8kdEsUopTkyyrmPu3GZTyAs90AAIgHAAC03TZS8fxNMWXt_7jKQQ"
    await call.message.answer_video(
        video3, caption="13-dars. Hujjatni tahrirlash va formatlashga oid mashqlar"
    )
    video4 = "BAACAgIAAxkBAAIFqGL8sMGarhOkM8lB0UffwuZO6ssvAAMcAALTdNlLlD9Rrxe5QAwpBA"
    await call.message.answer_video(
        video4, caption="14-dars. Hujjatlarda rasmlar bilan ishlarga oid mashqlar"
    )
    video5 = "BAACAgIAAxkBAAIDFmL8klcCbaJ04FHP37UZI5r2TglPAAIhHAAC03TZSxEecse9wOdOKQQ"
    await call.message.answer_video(
        video5, caption="15-dars. Rasm va chizmalarga oid amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIDG2L8kvEzbIPIHI5S01PeI6biTnBjAAIVHAAC03TZS8ukfJM1an2NKQQ"
    await call.message.answer_video(
        video6, caption="16-dars. Rasm va chizmalarga oid amaliy mashg'ulot"
    )
    video7 = "BAACAgIAAxkBAAIDH2L8kwRwdIvwYU3B3-nAbtGxcNodAAIKHAAC03TZS9WuOoQyxw9kKQQ"
    await call.message.answer_video(
        video7, caption="17-dars. SmartArt obyekti maketlaridan foydalanish"
    )
    video8 = "BAACAgIAAxkBAAIDImL8kyXmCJHpM_v10diaF2lxl-NsAAIHHAAC03TZSxJNzFCw93L7KQQ"
    await call.message.answer_video(
        video8, caption="18-dars. Hujjatlarda jadvallar bilan ishlash"
    )
    video9 = "BAACAgIAAxkBAAIDJmL8k2NDA74qZz7PDI_Ej29uYIJrAAL7GwAC03TZS1DInyQadXJSKQQ"
    await call.message.answer_video(
        video9, caption="19-dars. Jadvallar ustida amallar"
    )
    video10 = "BAACAgIAAxkBAAIDK2L8k4p_2vW6G4RESD7E_K0EZwYWAAIBHAAC03TZS4ott7mAYKk4KQQ"
    await call.message.answer_video(
        video10, caption="20-dars. Jadvallar ustida amallar. Amaliy mashg'ulot", reply_markup=DavomVideo62
    )


@dp.callback_query_handler(text="davom62")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIE7mL8mmN6stkUS59up0KgKShPfpvhAAIJHAAC03TZS0gp2JESYaD5KQQ'
    await call.message.reply_video(VDars1, caption="21-dars. Hujjatga havola va gipermurojaat joylashtirish")
    video2 = "BAACAgIAAxkBAAIE8mL8oqipRGCsj6h2koynqWV8L5OOAAIoHAAC03TZSwkd90oMX_sqKQQ"
    await call.message.answer_video(
        video2, caption="22-dars. Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIE9mL8qa7wTXbWZYm-ESTVq3b24TlfAAIMHAAC03TZS57GRdP3R6qHKQQ"
    await call.message.answer_video(
        video3, caption="23-dars. WordART obyekti"
    )
    video4 = "BAACAgIAAxkBAAIE-mL8qfeyS4rwqShcuczPo1_H4oEmAAInHAAC03TZSzy1_RvN-yPmKQQ"
    await call.message.answer_video(
        video4, caption="24-dars. Word dasturida formulalar yozish"
    )
    video5 = "BAACAgIAAxkBAAIE_mL8qh5p_r5brrmsmyLpXrM6ewovAAL6GwAC03TZSxMY96jkynoIKQQ"
    await call.message.answer_video(
        video5, caption="25-dars. Amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIFHWL8q1xxEK63BzcJ5SFBON6Z4uSjAAILHAAC03TZS2xy59RcMOiTKQQ"
    await call.message.answer_video(
        video6, caption="26-dars. Amaliy mashg'ulot"
    )
    video7 = "BAACAgIAAxkBAAIFIWL8q35_Q4QzGuWPdYsjp-7j05uNAAL9GwAC03TZS26DmTyo_IO9KQQ"
    await call.message.answer_video(
        video7, caption="27-dars. Takrorlash"
    )
    video8 = "BAACAgIAAxkBAAIFJWL8q4_d1T5IurEkDBRglMUWbv6AAALyGwAC03TZS1MhhapHjXlsKQQ"
    await call.message.answer_video(
        video8, caption="28-dars. \"Word\" da hujjatni chop etish"
    )
    video9 = "BAACAgIAAxkBAAIFKWL8rgFlbNIDXMOv9N0H67xdJwi1AAIZHAAC03TZSwNUYm8W4j5mKQQ"
    await call.message.answer_video(
        video9, caption="29-dars. Mustahkamlash"
    )
    video10 = "BAACAgIAAxkBAAIFLWL8rialfoqCATOGe7HtYkwT_9FzAAL3GwAC03TZS0__zIpqKp1JKQQ"
    await call.message.answer_video(
        video10, caption="30-dars. Mustahkamlash", reply_markup=DavomVideo63
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi52")
@dp.callback_query_handler(text="5Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIHW2L-O8Y0yGAlEeSHpPBYvMU8gpEBAAIHHQACnt3xS1JxUf70e2KXKQQ'
    await call.message.reply_video(VDars1,
                                   caption="1-dars . Xavfsizlik texnikasi qoidalari va sanitariya-gigiyena talablari")
    video2 = "BAACAgIAAxkBAAIHXWL-PHUcojlP7_R2yLD41T_22kUTAAIFHQACnt3xS1ODmqvUaAEvKQQ"
    await call.message.answer_video(
        video2, caption="2-dars. Informatika fani haqida"
    )
    video3 = "BAACAgIAAxkBAAIHYGL-PK2xJKdX-FZmIxXVDp__I19rAAL-HAACnt3xSyVb1zAzVgAB9ykE"
    await call.message.answer_video(
        video3, caption="3-dars. Axborot va raqamli texnologiyalar"
    )
    video4 = "BAACAgIAAxkBAAIHYmL-PMtW1cqEO1DC09NjUC1rPllvAAL6HAACnt3xS0iAt-6ilq-zKQQ"
    await call.message.answer_video(
        video4, caption="4-dars. Axborotni kodlash. Axborot o'lchov birliklari"
    )
    video5 = "BAACAgIAAxkBAAIHZGL-PPOM4CgMHsIJUEDOB_r-X9XPAAL3HAACnt3xS3wBC5edlx6eKQQ"
    await call.message.answer_video(
        video5, caption="5-dars. Amaliy mashg`ulot"
    )
    video6 = "BAACAgIAAxkBAAIHbmL-PRQh8C8fkbP4rdxlN6tPDkYOAAL0HAACnt3xS5rUQJsVAAHyhykE"
    await call.message.answer_video(
        video6, caption="6-dars. Kompyuterning qo'shimcha qurilmalari"
    )
    video7 = "BAACAgIAAxkBAAIHemL-P6bmcFghStP7p447kTLn8KqqAALxHAACnt3xS4Yd49ttY6j0KQQ"
    await call.message.answer_video(
        video7, caption="7-dars. Klaviatura va sichqoncha bilan ishlash ko`nikmalari"
    )
    video8 = "BAACAgIAAxkBAAIHfGL-P9n4g_EHKP83kA03IMFQx-DHAALsHAACnt3xS2ubSLoBsJSVKQQ"
    await call.message.answer_video(
        video8, caption="8-dars. Klaviatura trenajorlari va \"tezkor terish\" mashqlari"
    )
    video9 = "BAACAgIAAxkBAAIHfmL-QAIBMyU2M4XyzAcpa-GtgQrxAALoHAACnt3xS7XAuzGPMfHxKQQ"
    await call.message.answer_video(
        video9, caption="9-dars. Kompyuterni boshqaruvchi dasturlar"
    )
    video10 = "BAACAgIAAxkBAAIHgGL-QGR_vKwVM_zoZtUlYvhcM9CAAALkHAACnt3xS635PuMCC79bKQQ"
    await call.message.answer_video(
        video10, caption="10-dars. Amaliy mashg'ulot", reply_markup=DavomVideo51
    )


@dp.callback_query_handler(text="Oldingi53")
@dp.callback_query_handler(text="davom51")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIHgGL-QGR_vKwVM_zoZtUlYvhcM9CAAALkHAACnt3xS635PuMCC79bKQQ'
    await call.message.reply_video(VDars1, caption="11-dars. Matn protsessori dasturi va uning interfeysi")
    video2 = "BAACAgIAAxkBAAIHlmL-QWv15iLTfLd0ovHDIbTckfPbAALcHAACnt3xS-zbR2Obx3MbKQQ"
    await call.message.answer_video(
        video2, caption="12-dars. Hujjatlarni formatlash uskunalari"
    )
    video3 = "BAACAgIAAxkBAAIHmGL-QcEU2vAvQ0DxkCJg4BfsyNKRAALWHAACnt3xS6F9_WvDv7WLKQQ"
    await call.message.answer_video(
        video3, caption="13-dars. Matn protsessori va dasturida hujjat yaratish va tahrirlash"
    )
    video4 = "BAACAgIAAxkBAAIHmmL-Qf__KycREqRgP3i3rmttI4AmAALVHAACnt3xS6d2GVRtoBUfKQQ"
    await call.message.answer_video(
        video4, caption="14-dars. Hujjatlarda jadballar bilan ishlash"
    )
    video5 = "BAACAgIAAxkBAAIHnGL-QjvZA5tvV9fAMdFGdqtT1vRLAALSHAACnt3xS0DfjQkz1pv_KQQ"
    await call.message.answer_video(
        video5, caption="15-dars. WordArt obyekti va sarvaraq (titul) yaratish"
    )
    video6 = "BAACAgIAAxkBAAIHoGL-QxqQ5YKtIhhXXmfhuLWcQbA6AAJAHQACnt3xS5F2YuS-tMdiKQQ"
    await call.message.answer_video(
        video6, caption="16-dars. Grafik muharrir interfeysi va uskunalar paneli"
    )
    video7 = "BAACAgIAAxkBAAIHomL-Q3HxQRsnNvoKo8PQKx5_5DbGAALPHAACnt3xSwwMRVGlMTuYKQQ"
    await call.message.answer_video(
        video7, caption="17-dars. Grafik muharrirlarida matn bilan ishlash"
    )
    video8 = "BAACAgIAAxkBAAIHomL-Q3HxQRsnNvoKo8PQKx5_5DbGAALPHAACnt3xSwwMRVGlMTuYKQQ"
    await call.message.answer_video(
        video8, caption="18-dars. Grafik muharrirlarida matn bilan ishlash"
    )
    video9 = "BAACAgIAAxkBAAIHpGL-Q8x5Gs3OYZRP_6cgcRSahvXoAAIdHQACnt3xS1kyfUvW9WIdKQQ"
    await call.message.answer_video(
        video9, caption="19-dars. Qatlamlar bilan ishlash"
    )
    video10 = "BAACAgIAAxkBAAIHpmL-RMahL6HYfbo8JId1LVlOxaehAAJNHQACnt3xS7c0kKVJ5_syKQQ"
    await call.message.answer_video(
        video10, caption="20-dars. Scratch dasturlash muhiti", reply_markup=DavomVideo52
    )


@dp.callback_query_handler(text="davom52")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIH8mL-Rbqt-EXvUByWTLxnjm6gw_0PAAIUHQACnt3xSxr4eZMZPwP5KQQ'
    await call.message.reply_video(VDars1, caption="21-dars. Sodda animatsiya dasturni yaratish")
    video2 = "BAACAgIAAxkBAAIH9GL-Rf4lq3Ozg5PqRDEZUqjwIdJSAAISHQACnt3xS5MC7DS0iWyNKQQ"
    await call.message.answer_video(
        video2, caption="22-dars. Spraytlar liboslari (kostyumlari)ni almashtirish"
    )
    video3 = "BAACAgIAAxkBAAIH9mL-RiQPNT6YgSr6My3vb9-YuxnmAAINHQACnt3xS3jINUtqPPSuKQQ"
    await call.message.answer_video(
        video3, caption="23-dars. Ovoz va matn bilan ishlash"
    )
    video4 = "BAACAgIAAxkBAAIIAmL-RxrFC7QP19TeaX3FI1XmaNDXAAJYHQACnt3xS7BoLmGMeyk1KQQ"
    await call.message.answer_video(
        video4, caption="24-dars. Scratch muhitida shakllar yaratish"
    )
    video5 = "BAACAgIAAxkBAAIIAAFi_kahp1BCJ2J3YMaddNyXJuGpQQACCh0AAp7d8UthQpEjseEE6SkE"
    await call.message.answer_video(
        video5, caption="25-dars. Mustahkamlash", reply_markup=DavomVideo53
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi72")
@dp.callback_query_handler(text="7Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIJBWL-kH9SuT8TN5m_JK3zfCsB1gF-AAK7HgACnt3xSzoxMba3RzNcKQQ'
    await call.message.reply_video(VDars1, caption="1-dars. Axborot tushunchasi va bilish haqida")
    video2 = "BAACAgIAAxkBAAIJCWL-kSp6Bi-US_AYYIpCkD2XEcBaAAK0HgACnt3xS5H8zQABqOQgeSkE"
    await call.message.answer_video(
        video2, caption="2-dars. Axborotlar ustida bajariladigan amallar."
    )
    video3 = "BAACAgIAAxkBAAIJC2L-kU1miIKYm_xG8JlE0J42m0HmAAK5HgACnt3xS9m3a7JYFWiQKQQ"
    await call.message.answer_video(
        video3, caption="3-dars. Axborotlarni kodlash usullari."
    )
    video4 = "BAACAgIAAxkBAAIJDWL-kYV64aDLtrTW5fXq8BDQ_8ZkAAKyHgACnt3xS7NeY8dkPVk-KQQ"
    await call.message.answer_video(
        video4, caption="4-dars. Amaliy mashg'ulot.Takrorlash"
    )
    video5 = "BAACAgIAAxkBAAIJD2L-kc945pEqVQwsL9upg9V6dB9EAAKxHgACnt3xS0ROvXiUWrXZKQQ"
    await call.message.answer_video(
        video5, caption="5-dars. Sanoq sistemalari haqida."
    )
    video6 = "BAACAgIAAxkBAAIJEWL-klu6C7YP9iKcC3SZ7PU2Nq3RAAKqHgACnt3xS2IfUWC4A-hbKQQ"
    await call.message.answer_video(
        video6, caption="6-dars. Ikkilik sanoq sistemasida amallar bajarish."
    )
    video7 = "BAACAgIAAxkBAAIJE2L-koIvIZmhW5ycZydAbgp_6fzlAAKnHgACnt3xS5hX0V4wYXHHKQQ"
    await call.message.answer_video(
        video7, caption="7-dars. Amaliy mashg'ulot."
    )
    video8 = "BAACAgIAAxkBAAIJFWL-kqVCurcL7hPJalQ42pXX-HWiAAKZHgACnt3xSzzZ40tcOy38KQQ"
    await call.message.answer_video(
        video8, caption="8-dars. Takrorlash darsi."
    )
    video9 = "BAACAgIAAxkBAAIJF2L-ksFd9wR7QZb2DHLT0nJWwgQ6AAKYHgACnt3xS2WwG-cEQuZ7KQQ"
    await call.message.answer_video(
        video9, caption="9-dars. Bir sanoq sistemasidagi sonlarni boshqa sanoq sistemasida tasvirlash."
    )
    video10 = "BAACAgIAAxkBAAIJGWL-kuTUDsU3O1wwUCyFV-saLIYnAAKVHgACnt3xS7ULe0RClI3gKQQ"
    await call.message.answer_video(
        video10, caption="10-dars. Amaliy mashg'ulot", reply_markup=DavomVideo71
    )


@dp.callback_query_handler(text="Oldingi73")
@dp.callback_query_handler(text="davom71")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIJHWL-k5aA20YdNQ8TtP7XUdaM8U0qAAKSHgACnt3xS4sdH4Zafr3GKQQ'
    await call.message.reply_video(VDars1, caption="11-dars. Axborotlarning kompyuterda tasvirlanishi")
    video2 = "BAACAgIAAxkBAAIJG2L-kwymZ57BUxZ1MsCXqemPZRoXAAKPHgACnt3xSxz4c5Fu_iF-KQQ"
    await call.message.answer_video(
        video2, caption="12-dars. \"Axborotlarni kompyuterda tasvirlanishi\" mavzusida Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIJH2L-k-yDo4oJwW7K3sLT3-31s3yXAAKOHgACnt3xSyAawiwYvjpJKQQ"
    await call.message.answer_video(
        video3, caption="13-dars. Takrorlash"
    )
    video4 = "BAACAgIAAxkBAAIJIWL-lBgzo62AAAGDz_cjF-lLmIYxoQACiR4AAp7d8UtCJYnlj8PbeSkE"
    await call.message.answer_video(
        video4, caption="14-dars. Mustahkamlash"
    )
    video5 = "BAACAgIAAxkBAAIJI2L-lGy3euhyWS7Q4mxTlg7aDEekAAKMHgACnt3xS-yOHJzievftKQQ"
    await call.message.answer_video(
        video5, caption="15-dars. Axborot texnologiyalari"
    )
    video6 = "BAACAgIAAxkBAAIJJWL-lJBD60-jh01W8hPUfWyagdnqAAKEHgACnt3xS7u48DGF7sv8KQQ"
    await call.message.answer_video(
        video6, caption="16-dars. Axborot olam muammolari va internet"
    )
    video7 = "BAACAgIAAxkBAAIJJ2L-lLqKdRq1yAAB646TnzxYpnikggACgx4AAp7d8Usyu056FPiKGykE"
    await call.message.answer_video(
        video7, caption="17-dars. Amaliy mashg'ulot"
    )
    video8 = "BAACAgIAAxkBAAIJKWL-lOn1Qh6j9p2rkJ2lTjgiSjXIAAJ_HgACnt3xS_uJS7kzPmyfKQQ"
    await call.message.answer_video(
        video8,
        caption="18-dars. \"Axborot texnologiyalari va axborotli olam muammolari va internet\" mavzularini takrorlash"
    )
    video9 = "BAACAgIAAxkBAAIJRWL-npqzxflsQWWx_EDmeku97ILuAAJ9HgACnt3xSwx5JwqrdZRSKQQ"
    await call.message.answer_video(
        video9, caption="19-dars. Internetda ishlashni ta'minlovchi dasturlar"
    )
    video10 = "BAACAgIAAxkBAAIJMWL-mlCs250QU709x59C7pehnNYZAAJ7HgACnt3xSwaFWbg0OjHeKQQ"
    await call.message.answer_video(
        video10, caption="20-dars. \"Internetda ishlashni ta'minlovchi dasturla\" mavzusida amaliy mashg'ulot",
        reply_markup=DavomVideo72
    )


@dp.callback_query_handler(text="davom72")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIJM2L-mofIel84tTG39lTxYYjNbz87AAJ5HgACnt3xS_AvAv3PltmgKQQ'
    await call.message.reply_video(VDars1,
                                   caption="21-dars. \"Internetda ishlashni ta'minlovchi dasturlar\" mavzusini takrorlash")
    video2 = "BAACAgIAAxkBAAIJNWL-mrC2kvyEfrAT7y2KjG7jTGVyAAJ4HgACnt3xS46ULfHKu4zsKQQ"
    await call.message.answer_video(
        video2, caption="22-dars. Internetda ma'lumotlarni izlash"
    )
    video3 = "BAACAgIAAxkBAAIJN2L-ms4PcYNq_12NJZFTDkJJwTvIAAJ2HgACnt3xS9fnVLjAwpISKQQ"
    await call.message.answer_video(
        video3, caption="23-dars. \"Internetda ma'lumotlarni izlas\" mavzusida amaliy mashg'ulot"
    )
    video4 = "BAACAgIAAxkBAAIJOWL-mvImLuZzcJN_BuxOKKry-WZUAAJxHgACnt3xS1O-GgfgLMgLKQQ"
    await call.message.answer_video(
        video4, caption="24-dars. Elektron pochta"
    )
    video5 = "BAACAgIAAxkBAAIJO2L-mxjSmcfqKTM8N2PwiJ99I-beAAJuHgACnt3xS-ZPgSzU26KwKQQ"
    await call.message.answer_video(
        video5, caption="25-dars. Amaliy mashg'ulot. Elektron pochta"
    )
    video6 = "BAACAgIAAxkBAAIJPWL-m1X3-OUuSS4ErM3DcTLrjyhAAALFHgACnt3xS1ZnRYjaA_X3KQQ"
    await call.message.answer_video(
        video6, caption="26-dars. Axborotlarni himoyalash va antiviruslar haqida"
    )
    video7 = "BAACAgIAAxkBAAIJP2L-m3SB1a4JzHuGZp8mVAYoZbS7AALDHgACnt3xSzj4rxqSUMGfKQQ"
    await call.message.answer_video(
        video7, caption="27-dars. Axborotlarni himoyalash va antiviruslar haqida"
    )
    video8 = "BAACAgIAAxkBAAIJQWL-m5c2WbVyOT0MGX8_VF5psFeeAALCHgACnt3xSwVG0lbU4tJKKQQ"
    await call.message.answer_video(
        video8, caption="28-dars. Amaliy mashg'ulot. Axborotlarni ximoyalash va antiviruslar haqida"
    )
    video9 = "BAACAgIAAxkBAAIJQ2L-nMKg1oN_pWl5WR8YwLNqgpLGAAK9HgACnt3xS9_5uEQUm7n8KQQ"
    await call.message.answer_video(
        video9, caption="29-dars. Axborotlarni himoyalash va antirivuslar haqida"
    )
    video10 = "BAACAgIAAxkBAAIJSWL-n9d5huqKCmW7apaFWfSBmaOLAAI5HwACnt3xSxrCC5DqJqxRKQQ"
    await call.message.answer_video(
        video10, caption="30-dars. Takrorlash darsi. (Internetda ishlash asoslari)"
    )
    video11 = "BAACAgIAAxkBAAIJXWL-o64YgUmHZNu9WZghqvwi2fvdAAK8HgACnt3xS9fYBNYnpRHXKQQ"
    await call.message.answer_video(
        video11, caption="31-dars. Yakuniy takrorlash darsi", reply_markup=DavomVideo73
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi82")
@dp.callback_query_handler(text="8Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIKsmL_a6dlwL5CFWfLVt2MQzZY9Z5qAAJHGwACfBD4S9otO-ghLg1zKQQ'
    await call.message.reply_video(VDars1,
                                   caption="1-dars. SMM (Social media marketing - ijtmoiy media marketing) haqida")
    video2 = "BAACAgIAAxkBAAIKtGL_bhx8oI0de1_okQqldRnR3t3FAAJGGwACfBD4S-p0gcfDK5cIKQQ"
    await call.message.answer_video(
        video2, caption="1-dars. SMM (Social media marketing - ijtmoiy media marketing) haqida"
    )
    video3 = "BAACAgIAAxkBAAIKt2L_bkTvDQpKfkJtN4NkkB69dddRAAJEGwACfBD4S11FUv6gk0lSKQQ"
    await call.message.answer_video(
        video3, caption="3-dars. SMM platformalari bilan tanishish. Telegram tarmog'i"
    )
    video4 = "BAACAgIAAxkBAAIKuWL_bmIVMAMUrVnctt94OX8yJoUeAAJDGwACfBD4SxI2x6Ud2NpOKQQ"
    await call.message.answer_video(
        video4, caption="4-dars. SMM platformalari bilan tanishish. YouTube sayti"
    )
    video5 = "BAACAgIAAxkBAAIKu2L_bqDU_Ek_O9uhmwtR-ZrJ0POHAAJAGwACfBD4S3Gl72RcXBJeKQQ"
    await call.message.answer_video(
        video5, caption="5-dars. SMM platformalari bilan tanishish. Telegram tarmog'i"
    )
    video6 = "BAACAgIAAxkBAAIKvWL_brblnmvQPMdmTDsJAToOCcJLAAJCGwACfBD4S-0YiAoMSYs0KQQ"
    await call.message.answer_video(
        video6, caption="6-dars. SMM platformalari bilan tanishish. Instagram tarmog'i"
    )
    video7 = "BAACAgIAAxkBAAIKv2L_btQiDgSzArTKr_3cjaQKEzOMAAI9GwACfBD4S0aqg-eHgI10KQQ"
    await call.message.answer_video(
        video7, caption="7-dars. SMMni Internet tarmog'ida harakatlantirish"
    )
    video8 = "BAACAgIAAxkBAAIKwWL_bwZhtXXiFcqV7IP26v2m8NcXAAI_GwACfBD4Sza5zsmEiqjrKQQ"
    await call.message.answer_video(
        video8, caption="8-dars. Amaliy ish"
    )
    video9 = "BAACAgIAAxkBAAIKw2L_bykxZvFaifJ3-ha4j3bGw4p8AAI3GwACfBD4S72mIvUFx_UWKQQ"
    await call.message.answer_video(
        video9, caption="9-dars. SMM asosida tadqiqot loyihalarini boshqarish. YouTube saytida kanal ochish"
    )
    video10 = "BAACAgIAAxkBAAIKxWL_b1k668JPrK4Zjb0G1LHjHDMHAAI0GwACfBD4S5cJBMKSLJ0nKQQ"
    await call.message.answer_video(
        video10, caption="10-dars. SMM asosida tadqiqot loyihalarini boshqarish. Facebook tarmog'ida sahifa ochish",
        reply_markup=DavomVideo81
    )


@dp.callback_query_handler(text="Oldingi83")
@dp.callback_query_handler(text="davom81")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIKx2L_b55CckSDPLzAns0eqPhiTBhrAAI2GwACfBD4Sy9tzoRHm-H9KQQ'
    await call.message.reply_video(VDars1,
                                   caption="11-dars. SMM asosida tadqiqod loyihalarini boshqarish. Telegram tarmog'ida kanal ochish")
    video2 = "BAACAgIAAxkBAAIKyWL_b728hhbGgg_P5cfEyvMPoyzhAAIxGwACfBD4Szj0ihoc9czkKQQ"
    await call.message.answer_video(
        video2, caption="12-dars. CMS Platformalari bilan tanishish"
    )
    video3 = "BAACAgIAAxkBAAIKy2L_b_fR3VGEy5yDpwpNOQ_QORFtAAIvGwACfBD4SztIbP2sURUKKQQ"
    await call.message.answer_video(
        video3, caption="13-dars. Amaliy ish"
    )
    video4 = "BAACAgIAAxkBAAIKzWL_cBTfz-zkbG6S4FCRQlO8U095AAIuGwACfBD4S2vVB0Bsst9XKQQ"
    await call.message.answer_video(
        video4, caption="14-dars. Web-sayt dizayni bilan ishlash"
    )
    video5 = "BAACAgIAAxkBAAIKz2L_cMWGL-yHyk1SK8pAikBDMloxAAIoGwACfBD4S217F84BMjFvKQQ"
    await call.message.answer_video(
        video5, caption="15-dars. LMS (Learning management systems-ta'limni boshqaruv tizimlari) haqida"
    )
    video6 = "BAACAgIAAxkBAAIK0WL_cQABvwdHFd8AAbZOe6jvMHvfwy4AAicbAAJ8EPhLpczl15rvMlgpBA"
    await call.message.answer_video(
        video6, caption="16-dars. LMS platformalarning turlari va vazifalari"
    )
    video7 = "BAACAgIAAxkBAAIK02L_cSYB7UvmY_ylhNKU2RAsOUkZAAIlGwACfBD4Szj64aLgGNjwKQQ"
    await call.message.answer_video(
        video7, caption="17-dars. Amaliy ish"
    )
    video8 = "BAACAgIAAxkBAAIK1WL_cVKfx29V5GbuKojABTZbvngGAAIkGwACfBD4S52-9Jf7uevvKQQ"
    await call.message.answer_video(
        video8,
        caption="18-dars. LMS asosida masofaviy ta'lim olish. Moodle platformasi"
    )
    video9 = "BAACAgIAAxkBAAIK12L_cXK1eQhgHw_SRImH7hp2rsh8AAIjGwACfBD4S60kKpC4twqNKQQ"
    await call.message.answer_video(
        video9, caption="19-dars. Amaliy ish. Moodle platformasida ta'lim olish"
    )
    video10 = "BAACAgIAAxkBAAIK2WL_cZ9eLk7yLwWWFttKoU3vag-7AAIhGwACfBD4S062deK_WiLpKQQ"
    await call.message.answer_video(
        video10, caption="20-dars.LMS asosida masofaviy ta'lim olish. Google Classroom platformasi",
        reply_markup=DavomVideo82
    )


@dp.callback_query_handler(text="davom82")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIK22L_coUmOanDG7E2YRkWINtVOIGOAAIdGwACfBD4S14JfdIP0_pkKQQ'
    await call.message.reply_video(VDars1,
                                   caption="21-dars. MOOC (MASSIVE OPEN ONLINE COURSES - OMMAVIY OCHIQ ONLAYN KURSLAR) haqida")
    video2 = "BAACAgIAAxkBAAIK3WL_csATntG8-TAGYdpIWKdLrP82AAIcGwACfBD4S9sIsp2B5K5LKQQ"
    await call.message.answer_video(
        video2, caption="22-dars.Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIK32L_cuGEcUFAigOTeo6ARO4TIQK4AAIYGwACfBD4Szxx7UhnV4_NKQQ"
    await call.message.answer_video(
        video3, caption="23-dars. MOOC asosida masofaviy ta'lim olish"
    )
    video4 = "BAACAgIAAxkBAAIK4WL_cw0Z0TxxD9KhHLcXMctvJF1RAAIWGwACfBD4S-uSpW3fHm4EKQQ"
    await call.message.answer_video(
        video4, caption="24-dars. Amaliy mashg'ulot"
    )
    video5 = "BAACAgIAAxkBAAIK42L_czX0GFToliofnCmhmCwWShZoAAIUGwACfBD4Sxg7KnlRPAefKQQ"
    await call.message.answer_video(
        video5, caption="25-dars.\"WEB-FREELANCE\" haqida tushuncha", reply_markup=DavomVideo83
    )


#######################################################################################################################################


@dp.callback_query_handler(text="Oldingi92")
@dp.callback_query_handler(text="9Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIMwWL_1fikMsazIMPmnBj21UPNBEhCAAJBHgACfBD4S3B0GuvZSahpKQQ'
    await call.message.reply_video(VDars1,
                                   caption="1-dars. Sanoq sistemalari haqida. Ikkilik sanoq sistemasida amallar bajarish")
    video2 = "BAACAgIAAxkBAAIMxmL_1k8bNh4chyexPQABQHQnMZ_2lgACPx4AAnwQ-EtOOka4mbFaVSkE"
    await call.message.answer_video(
        video2, caption="2-dars. Sakkizlik va o'n oltilik sanoq sistemasida amallar bajarish"
    )
    video3 = "BAACAgIAAxkBAAIMyWL_1m5GhbLjq_ouhizwLM9XNhmbAAI9HgACfBD4S9JSRR4NGTXEKQQ"
    await call.message.answer_video(
        video3, caption="3-dars. Sonlarni bir sanoq sistemasidan boshqa sanoq sistemasiga o'tkazish"
    )
    video4 = "BAACAgIAAxkBAAIMyWL_1m5GhbLjq_ouhizwLM9XNhmbAAI9HgACfBD4S9JSRR4NGTXEKQQ"
    await call.message.answer_video(
        video4, caption="4-dars. Mantiqiy amallar va ifodalar"
    )
    video5 = "BAACAgIAAxkBAAIMz2L_1qlfS9VrYoqzBd5f13dXDoXjAAI2HgACfBD4S8xin1Yh1OM1KQQ"
    await call.message.answer_video(
        video5, caption="5-dars. Masalalarni kompyuterda yechish bosqichlari"
    )
    video6 = "BAACAgIAAxkBAAIM0mL_1sS5t7m2NEYSXqFklaTV_9YIAAIxHgACfBD4S7TYXUfXG0EpKQQ"
    await call.message.answer_video(
        video6, caption="6-dars. Model va uning turlari"
    )
    video7 = "BAACAgIAAxkBAAIM1WL_1wGeI3aGutMGwt9S2JrFpJ28AAItHgACfBD4S5pfR4NuGSGiKQQ"
    await call.message.answer_video(
        video7, caption="7-dars. Algoritm tushunchasi va uning xossalari"
    )
    video8 = "BAACAgIAAxkBAAIM2GL_1x3Xbvf9iifs6ieuX_5larzPAAIqHgACfBD4S2XFNmP3qEqnKQQ"
    await call.message.answer_video(
        video8, caption="8-dars. Algoritm turlari va tasvirlash usullari"
    )
    video9 = "BAACAgIAAxkBAAIM22L_1zPuVkYsFK8fgkwebETH_SPNAAIpHgACfBD4SwbS8kFT9xnLKQQ"
    await call.message.answer_video(
        video9, caption="9-dars. Algoritm turlari va tasvirlash usullariga oid amaliy mashg'ulot."
    )
    video10 = "BAACAgIAAxkBAAIM3mL_10QKPXRYI6gAAdo109YlhWW1yAACKB4AAnwQ-EsJQPtlXqIhLSkE"
    await call.message.answer_video(
        video10, caption="10-dars. Model va uning turlari (davomi).",
        reply_markup=DavomVideo91
    )


@dp.callback_query_handler(text="Oldingi93")
@dp.callback_query_handler(text="davom91")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIM4WL_12v3-pOkEnMBj80CvjiJxZx2AAIkHgACfBD4S5V-tYc8NLXdKQQ'
    await call.message.reply_video(VDars1, caption="11-dars. Chiziqli algoritmlar")
    video2 = "BAACAgIAAxkBAAIM5GL_13yRwZ-5x9_fHOu-ehS8YnOGAAIhHgACfBD4Sz4k7F4nmmiEKQQ"
    await call.message.answer_video(
        video2, caption="12-dars. Tarmoqlanuvchi algoritmlar"
    )
    video3 = "BAACAgIAAxkBAAIM52L_15sa1OTRdgFedgsdXTaTslvFAAIdHgACfBD4S4XG0YQhTFZoKQQ"
    await call.message.answer_video(
        video3, caption="13-dars. Algoritmlar mavzusiga oid amaliy mashg'ulot"
    )
    video4 = "BAACAgIAAxkBAAIM6mL_16_8rexcbLzwDZtT16oEV7UCAAIYHgACfBD4S8NZgDqqyKzAKQQ"
    await call.message.answer_video(
        video4, caption="14-dars. Takrorlanuvchi algoritmlar"
    )
    video5 = "BAACAgIAAxkBAAIM7WL_18Bx3ZTjTeA68kWHDZmjnonaAAIWHgACfBD4S-gL1m8bUsKjKQQ"
    await call.message.answer_video(
        video5, caption="15-dars. Algoritm mavzusiga oid amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIM8GL_19b3sc7ShVDO7JK-uBQZS25XAAISHgACfBD4SyiUn2SfjTsLKQQ"
    await call.message.answer_video(
        video6, caption="16-dars. Dastur va dasturlash haqida"
    )
    video7 = "BAACAgIAAxkBAAIM82L_1-X2uUz7l6vBpv58Kr9g-d2wAAILHgACfBD4SxfBLyJ9TMVEKQQ"
    await call.message.answer_video(
        video7, caption="17-dars. Python dasturlash tilini o'rnatish"
    )
    video8 = "BAACAgIAAxkBAAIM9mL_2BMrNliliYGzx9GNzBIgdI9JAAL-HQACfBD4S1Yoc29GKrUDKQQ"
    await call.message.answer_video(
        video8,
        caption="18-dars. Python ma'lumot turlari"
    )
    video9 = "BAACAgIAAxkBAAIM-WL_2CZpGSumseqESoa2Pqk_MpN3AAL5HQACfBD4S6H8iSRPXg_3KQQ"
    await call.message.answer_video(
        video9, caption="19-dars. Pythonda arifmetik amallarni bajarish"
    )
    video10 = "BAACAgIAAxkBAAIM_GL_2YflU3pXlkF_jn_xmHw1crObAALXHgACfBD4S33tmr8iwcHSKQQ"
    await call.message.answer_video(
        video10, caption="20-dars. Pythonda arifmetik amallari bajarash mavzusi bo'yicha masalalar yechish",
        reply_markup=DavomVideo92
    )


@dp.callback_query_handler(text="Oldingi94")
@dp.callback_query_handler(text="davom92")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIM_2L_2btqrMaflanRLjb8INyBXk9VAALzHQACfBD4SzmxKs9dNXp0KQQ'
    await call.message.reply_video(VDars1, caption="21-dars. Pythonda satrlar bilan ishlash")
    video2 = "BAACAgIAAxkBAAINAmL_2c9mjNRWiBMkFDYR9pbXPMzOAALvHQACfBD4S5Q-xM1QImXqKQQ"
    await call.message.answer_video(
        video2, caption="22-dars. Pythonda operator va ifodalar"
    )
    video3 = "BAACAgIAAxkBAAINBWL_2g1YOcCbGHpqy6NAEJU_1fEVAALuHQACfBD4S9BRVnTPqpSAKQQ"
    await call.message.answer_video(
        video3, caption="23-dars. Pythonda sodda masalalarni dasturlash"
    )
    video4 = "BAACAgIAAxkBAAINCGL_2nTTu2GmyK6QCc9VFxn-6etbAALpHQACfBD4SzU5gTIXCndBKQQ"
    await call.message.answer_video(
        video4, caption="24-dars. Pythonda operator va ifodalar mavzusi bo'yicha amaliy mashg'ulot"
    )
    video5 = "BAACAgIAAxkBAAINC2L_2pFwUkRIcMpfvY6MBoEbAVV4AALeHQACfBD4SycKDZocBxZnKQQ"
    await call.message.answer_video(
        video5, caption="25-dars. Pythonda mantiqiy masalalarni dasturlash bo'yicha amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAINDmL_2vrR2iMSrmSTP22KgIiyztz-AALXHQACfBD4SxATxotW_pkeKQQ"
    await call.message.answer_video(
        video6, caption="26-dars. Pythonda mantiqiy masalalarni dasturlash"
    )
    video7 = "BAACAgIAAxkBAAINEWL_24OA0TTQnjds8A7jI1ToMLl2AALTHQACfBD4S2K2JXOKXPB4KQQ"
    await call.message.answer_video(
        video7, caption="27-dars. Tarmoqlanuvchi algoritmlarni dasturlash. If...else operatori"
    )
    video8 = "BAACAgIAAxkBAAINFGL_25wlvYJeY8YgSAqVM-5zmE12AALKHQACfBD4SzgcV5z18zdFKQQ"
    await call.message.answer_video(
        video8,
        caption="28-dars. Tarmoqlanuvchi algoritmlarni dasturlash. If...else operatori mavzusida amaliy mashg'ulot"
    )
    video9 = "BAACAgIAAxkBAAINGmL_3FwPTLCEgj-Q3PyB4s58g5kSAALGHQACfBD4S2slkR0Qw6TzKQQ"
    await call.message.answer_video(
        video9, caption="29-dars. Tarmoqlanuvchi algoritmlarni dasturlash. elif operatori"
    )
    video10 = "BAACAgIAAxkBAAINHWL_3HgJjFmAi2H63snRgQoCjqStAALCHQACfBD4S11MhPJAm7juKQQ"
    await call.message.answer_video(
        video10, caption="30-dars. Tarmoqlanuvchi algoritmlarni dasturlash. elif operatopi mavzusida amaliy mashg'ulot",
        reply_markup=DavomVideo93
    )


@dp.callback_query_handler(text="Oldingi95")
@dp.callback_query_handler(text="davom93")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAINIGL_3JsVUg4EbeOgdRmrf3mRijvZAAK9HQACfBD4S9Jwbji3I0q8KQQ'
    await call.message.reply_video(VDars1, caption="31-dars. Takrorlanuvchi algoritmlarni dasturlash. For operatori")
    video2 = "BAACAgIAAxkBAAINI2L_3Lc_F6oBMSg1q09RKadffT-GAAK5HQACfBD4S-WespElDnVVKQQ"
    await call.message.answer_video(
        video2,
        caption="32-dars. Takrorlanuvchi algoritmlarni dasturlash, for operatori, ichma-ich joylashgan sikllar bo'yicha amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAINJmL_3Mpgux6R0w_h1HbldFNFYzP4AAK2HQACfBD4SyebyB25A_frKQQ"
    await call.message.answer_video(
        video3, caption="33-dars. Takrorlanuvchi algoritmlarni dasturlash. for operatori"
    )
    video4 = "BAACAgIAAxkBAAINKWL_3N8M9IcB0dJLWtAHKENVgMoIAAKxHQACfBD4S3BzGIe7DeRRKQQ"
    await call.message.answer_video(
        video4, caption="34-dars. Takrorlash darsi"
    )
    video5 = "BAACAgIAAxkBAAINLGL_3R-v55A87ik5Pw2oFgGf6qulAAKqHQACfBD4S1amYwPVQ4TUKQQ"
    await call.message.answer_video(
        video5, caption="35-dars. Takrorlanuvchi algoritmlarni dasturlash."
    )
    video6 = "BAACAgIAAxkBAAINLGL_3R-v55A87ik5Pw2oFgGf6qulAAKqHQACfBD4S1amYwPVQ4TUKQQ"
    await call.message.answer_video(
        video6, caption="36-dars. Takrorlanuvchi algoritmlarni dasturlash. while operatori"
    )
    video7 = "BAACAgIAAxkBAAINL2L_3UZZ1fwWxaITCdONX-JcQpVeAAJwHgACfBD4S2R7mhE11SuBKQQ"
    await call.message.answer_video(
        video7,
        caption="37-dars. Takrorlanuvchi algoritmlarni dasturlash. while operatori mavzusi bo'yicha amaliy mashg'ulot"
    )
    video8 = "BAACAgIAAxkBAAINMmL_3VvmvZuDzHOMYg25004TJwe4AAJtHgACfBD4S-SHvy2S4jRYKQQ"
    await call.message.answer_video(
        video8, caption="38-dars. Tarmoqlanuvchi algoritmlarni dasturlash. ELIF operatori"
    )
    video9 = "BAACAgIAAxkBAAINNWL_3XZOcWrMzppWH7N60bAsGlwkAAJnHgACfBD4SyAPZCy5qK_EKQQ"
    await call.message.answer_video(
        video9, caption="39-dars. Tarmoqlanuvchi algoritmlarni dasturlash. If... else operatori"
    )
    video10 = "BAACAgIAAxkBAAINOGL_3ZZptdkZNraLCGQThUcPWmdIAAJlHgACfBD4S7hIOPNX1OwLKQQ"
    await call.message.answer_video(
        video10, caption="40-dars. Sikllarni boshqarish: continue, break operatorlari", reply_markup=DavomVideo94
    )


@dp.callback_query_handler(text="davom94")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAINO2L_3byT62c5YDCddyIr9t1Faz7mAAJkHgACfBD4S3pbtfGjp-2VKQQ'
    await call.message.reply_video(VDars1,
                                   caption="41-dars. Qism dasturlar: funksiyalar va protseduralar mavzusi bo'yicha amaliy mashg'ulot")
    video2 = "BAACAgIAAxkBAAINPmL_3c9H16LlKcFfwqdMPNLUkaqzAAJhHgACfBD4SyvvjXE4F2jRKQQ"
    await call.message.answer_video(
        video2, caption="42-dars. Funksiyalar va o'zgaruvchilar"
    )
    video3 = "BAACAgIAAxkBAAINQWL_3eSLOFqqJotcVgL7mSqXTGrEAAJfHgACfBD4S3PRw0t1l-RJKQQ"
    await call.message.answer_video(
        video3, caption="43-dars. Funksiyalar va o'zgaruvchilar (2-dars)"
    )
    video4 = "BAACAgIAAxkBAAINRGL_3gIdT5oWQEk1Y6VNmv1uD6RJAAJcHgACfBD4Sx-sFqk9-1ceKQQ"
    await call.message.answer_video(
        video4, caption="44-dars. Funksiyalar va o'zgaruvchilar mavzusida amaliy mashg'ulot"
    )
    video5 = "BAACAgIAAxkBAAINR2L_3hxkHeaIfE6Y02vc_jZXXoRnAAJaHgACfBD4Sx4iOUhWEaAOKQQ"
    await call.message.answer_video(
        video5, caption="45-dars. Python dasturlash tili kutubxonasi"
    )
    video6 = "BAACAgIAAxkBAAINSmL_3jSyX3ButBznv3l1JbcgSxdqAAJYHgACfBD4SywBnWKpaTEBKQQ"
    await call.message.answer_video(
        video6, caption="46-dars. Python dasurlash tili kutubxonasi (2-dars)"
    )
    video7 = "BAACAgIAAxkBAAINTWL_3kq3pKoT2kPlZFmuxKeSStxFAAJWHgACfBD4S-h1MmzbsBrcKQQ"
    await call.message.answer_video(
        video7, caption="47-dars. Python dasurlash tili kutubxonasi mavzusida amaliy mashg'ulot"
    )
    video8 = "BAACAgIAAxkBAAINUGL_3mf4tTvsVNOHKit4chfKbUdwAAJRHgACfBD4Sw_Z3Lpx0IARKQQ"
    await call.message.answer_video(
        video8, caption="48-dars. Pythonda foydalanuvchi grafik interfeysi bilan ishlash (1)"
    )
    video9 = "BAACAgIAAxkBAAINU2L_3nSFQc9nf92LBtNIjcj84lHSAAJRHgACfBD4Sw_Z3Lpx0IARKQQ"
    await call.message.answer_video(
        video9, caption="49-dars. Amaliy mashg'ulot"
    )
    video10 = "BAACAgIAAxkBAAINWGL_3q4F1tMDfAABvB0e2iPkVvIAATkAAkYeAAJ8EPhLGCi3KQwkxnQpBA"
    await call.message.answer_video(
        video10, caption="50-dars. O'tilgan mavzularni takrorlash", reply_markup=DavomVideo95
    )


#######################################################################################################################################


@dp.callback_query_handler(text="Oldingi102")
@dp.callback_query_handler(text="10Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIO92MAAdFZpxIeFtzJRMjS4Gh5dX3uqgAC8B0AAnwQAAFIPxum3VBD-3ApBA'
    await call.message.reply_video(VDars1,
                                   caption="1-dars. Sodda ifodalarni hisoblash")
    video2 = "BAACAgIAAxkBAAIOs2MAAcfbD5FIWKb_73SV5qyYjbqRvgACQx0AAnwQAAFImJYTQ-rPoZ4pBA"
    await call.message.answer_video(
        video2, caption="2-dars. Katakka murojaat: nisbiy, absolyut va aralash murojaat"
    )
    video3 = "BAACAgIAAxkBAAIOy2MAAct0_q5sQ0ylQob-1sHYysjUtAACrh0AAnwQAAFIEWYC_EkwVOYpBA"
    await call.message.answer_video(
        video3, caption="3-dars. Murojaatdan foydalanib amal bajarishda nusxalashning afzalligi"
    )
    video4 = "BAACAgIAAxkBAAIOzWMAAcurK_8ZC4xAIV8vxfnFF0em9AACsx0AAnwQAAFIgjQEIE3SJ3IpBA"
    await call.message.answer_video(
        video4, caption="4-dars. Sodda va murakkab funksiyalarning grafiklari"
    )
    video5 = "BAACAgIAAxkBAAIPCWMAAdQCwqP5z4CA_W8vlPmEUXV2EQADHgACfBAAAUjfgYkIMR5SyikE"
    await call.message.answer_video(
        video5, caption="5-dars. Boshqa varaq va kitobga murojaat"
    )
    video6 = "BAACAgIAAxkBAAIPB2MAAdNqeDnVL7RyY19OYK96oKctkwAC_x0AAnwQAAFIoI75s5L-ELMpBA"
    await call.message.answer_video(
        video6, caption="6-dars. MS EXCELning funksiyalar kutubxonasi"
    )
    video7 = "BAACAgIAAxkBAAIOsWMAAcedsoG2FZmU-6eFXSFqIGygCQACPR0AAnwQAAFI2rScvEC7MRopBA"
    await call.message.answer_video(
        video7, caption="7-dars. Funksiya argumenti oynasi"
    )
    video8 = "BAACAgIAAxkBAAIOvWMAAcjuAZcOz6MeofR9DYIatTD50wACZx0AAnwQAAFIOGPbq04sCUspBA"
    await call.message.answer_video(
        video8, caption="8-dars. Matnli funksiyalar"
    )
    video9 = "BAACAgIAAxkBAAIOvWMAAcjuAZcOz6MeofR9DYIatTD50wACZx0AAnwQAAFIOGPbq04sCUspBA"
    await call.message.answer_video(
        video9, caption="9-dars. Matnli funksiyalar"
    )
    video10 = "BAACAgIAAxkBAAIO72MAAdAmR40wVzCnzfdG22XoPb0WlQAC5R0AAnwQAAFITFd-_GVA0jopBA"
    await call.message.answer_video(
        video10, caption="10-dars. Matematik funksiyalar. Ko'paytmani hisoblashga oid funksiyalar",
        reply_markup=DavomVideo101
    )


@dp.callback_query_handler(text="Oldingi103")
@dp.callback_query_handler(text="davom101")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIPAWMAAdLXvd64xJpZZNyC9plJ04ar4QAC-x0AAnwQAAFIqREU_WWVJw8pBA'
    await call.message.reply_video(VDars1, caption="11-dars. Statistik funksiyalar")
    video2 = "BAACAgIAAxkBAAIO9WMAAdDjl1Mg_wTiM5Wh8E8CvxruMQAC7B0AAnwQAAFIn3tBIodI444pBA"
    await call.message.answer_video(
        video2, caption="12-dars. Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIO52MAAc7pyjiqYZ6EXaeHqUYGJ9kfRgAC1x0AAnwQAAFIPS82o3ES9R8pBA"
    await call.message.answer_video(
        video3, caption="13-dars. Ma'lumotlar ombori haqida tushuncha"
    )
    video4 = "BAACAgIAAxkBAAIO_2MAAdJK-yCf-QWvFs_mhV_xWeZvuwAC-R0AAnwQAAFInaP45ZJhN4kpBA"
    await call.message.answer_video(
        video4, caption="14-dars. Ma'lumotlar omborini boshqarish tizimlari"
    )
    video5 = "BAACAgIAAxkBAAIPBWMAAdMqeaVI5ZAWVMtmsbJlXPKnXwAC_h0AAnwQAAFIYS7BM-mw40spBA"
    await call.message.answer_video(
        video5, caption="15-dars. Amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIO4WMAAc4wLirP7NXWxSAREomQDGlRQAAC0R0AAnwQAAFImzA7m8w75FwpBA"
    await call.message.answer_video(
        video6, caption="16-dars. Amaliy mashg'ulot"
    )
    video7 = "BAACAgIAAxkBAAIO4WMAAc4wLirP7NXWxSAREomQDGlRQAAC0R0AAnwQAAFImzA7m8w75FwpBA"
    await call.message.answer_video(
        video7, caption="17-dars. Amaliy mashg'ulot."
    )
    video8 = "BAACAgIAAxkBAAIOwWMAAcm1OzIzVZiEKrEU4859mbnWBAAChh0AAnwQAAFI7Odb-t7n69MpBA"
    await call.message.answer_video(
        video8,
        caption="18-dars. MS Access 2010 dasturida ma'lumotlar omborini tashkil etish mavzusida Amaliy Mashg'ulot"
    )
    video9 = "BAACAgIAAxkBAAIO8WMAAdBbgtKkHrlpd35P69hgppyhvgAC5x0AAnwQAAFIOZlCFtT0HQEpBA"
    await call.message.answer_video(
        video9, caption="19-dars. Ilovalar yaratishning zamonaviy usullari"
    )
    video10 = "BAACAgIAAxkBAAIO1WMAAcymZSTNUShAYGM2Ki8NGFQwRwACwB0AAnwQAAFI9QFtcGYpcmwpBA"
    await call.message.answer_video(
        video10, caption="20-dars. Delphi dasturlash tili muhuti",
        reply_markup=DavomVideo102
    )


@dp.callback_query_handler(text="Oldingi104")
@dp.callback_query_handler(text="davom102")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIO0WMAAcw1_ORqj2vsZQGXATHC7xam_AACvB0AAnwQAAFI0bYoC9bQddopBA'
    await call.message.reply_video(VDars1, caption="21-dars. Delphi dasturlash tili muhiti")
    video2 = "BAACAgIAAxkBAAIOxWMAAcomPVtSaFb4Bb0UetxKcU05TwACkx0AAnwQAAFISBxDyfDRnKwpBA"
    await call.message.answer_video(
        video2, caption="22-dars. Boshqarish tugmasi"
    )
    video3 = "BAACAgIAAxkBAAIOr2MAAcdUpqFwJXKiOagKyMo2qozwzAACOh0AAnwQAAFIJZwYX7h7l-MpBA"
    await call.message.answer_video(
        video3, caption="23-dars. Boshqaruv tugmasi mavzusi bo'yicha Amaliy mashg'ulot"
    )
    video4 = "BAACAgIAAxkBAAIPC2MAAdRB-hvjKSteRuGh1eso_SS3xAACAh4AAnwQAAFIMxnKX2cYXiApBA"
    await call.message.answer_video(
        video4, caption="24-dars. Showmessage oynasi"
    )
    video5 = "BAACAgIAAxkBAAIOw2MAAcn7VECiD-6Ke6-8vYPxtTpfcgACkR0AAnwQAAFIHT2xRf7KsNUpBA"
    await call.message.answer_video(
        video5, caption="25-dars. Takrorlash"
    )
    video6 = "BAACAgIAAxkBAAIO42MAAc5xHYy2VOvWQKT-UNDYgsavkQAC0x0AAnwQAAFIO2WqeUmUIcspBA"
    await call.message.answer_video(
        video6, caption="26-dars. Ilova oynasiga ma'lumot joylash"
    )
    video7 = "BAACAgIAAxkBAAIO5WMAAc6uQQV2QDXvdyS_QoHaZ0ToxwAC1B0AAnwQAAFIV4d-Fv7Ch9EpBA"
    await call.message.answer_video(
        video7, caption="27-dars. Ilova oynasiga ma'lumot joylash mavzusida. Amaliy mashg'ulot."
    )
    video8 = "BAACAgIAAxkBAAIP0mMAAfRUqrPAQJ8h2VpOfdB3NdOXAgACPx0AAnwQCEgGLafj3mXTiikE"
    await call.message.answer_video(
        video8,
        caption="28-dars. Boshqarish obyektlarining faolligi va ko'rinmasligi"
    )
    video9 = "BAACAgIAAxkBAAIO32MAAc3yK-HFsWDCi2dhdrk2XU0wKQAC0B0AAnwQAAFInTBTk84aSispBA"
    await call.message.answer_video(
        video9, caption="29-dars. Boshqarish obyektlarining faolligi va ko'rinmasligi mavzusida amaliy mashg'ulot"
    )
    video10 = "BAACAgIAAxkBAAIO6WMAAc84LtHl43DQB6FCz6CBwzEPSwAC2R0AAnwQAAFIlYiQPO_7QYopBA"
    await call.message.answer_video(
        video10, caption="30-dars. Ilovaga ma'lumotlar kiritish",
        reply_markup=DavomVideo103
    )


@dp.callback_query_handler(text="Oldingi105")
@dp.callback_query_handler(text="davom103")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIO8WMAAdBbgtKkHrlpd35P69hgppyhvgAC5x0AAnwQAAFIOZlCFtT0HQEpBA'
    await call.message.reply_video(VDars1, caption="31-dars. Ilovaga ma'lumotlar kiritish mavzusida amaliy mashg'ulot")
    video2 = "BAACAgIAAxkBAAIPA2MAAdL8cmY9pduBFno9k3O0V3o7YAAC_B0AAnwQAAFImUvDZK_kkn4pBA"
    await call.message.answer_video(
        video2,
        caption="32-dars. Ma'lumotlar turini o'zgartirish"
    )
    video3 = "BAACAgIAAxkBAAIO_WMAAdINpTdxPfKeWWh6KjjTJo0eBQAC9x0AAnwQAAFIx9UMj5gf5hUpBA"
    await call.message.answer_video(
        video3, caption="33-dars. Ilovada radiotugmalar guruhidan foydalanish"
    )
    video4 = "BAACAgIAAxkBAAIOz2MAAcv6p7f4JtI__jic0fsvyeSPxAACuR0AAnwQAAFIcUOmwoNp3bwpBA"
    await call.message.answer_video(
        video4, caption="34-dars. ListBox va ComboBox obyektlari"
    )
    video5 = "BAACAgIAAxkBAAIOu2MAAciydde1-W7OK9JMngzp2jklWwACYB0AAnwQAAFIWoijIZFG158pBA"
    await call.message.answer_video(
        video5, caption="35-dars. Memo boshqarish obyekti"
    )
    video6 = "BAACAgIAAxkBAAIO2WMAAc0u4fmZhZEkTmQUovKwBNJ0OAACyR0AAnwQAAFIi5eBBueIc3EpBA"
    await call.message.answer_video(
        video6, caption="36-dars. Amaliy mashg'ulot. Memo boshqarish obyekti"
    )
    video7 = "BAACAgIAAxkBAAIO-2MAAdHmZR1cOhlamxTNGq0FiabFVAAC9R0AAnwQAAFIgA_MwJq5vSApBA"
    await call.message.answer_video(
        video7,
        caption="37-dars. Delphida grafika bilan ishlash"
    )
    video8 = "BAACAgIAAxkBAAIO82MAAdCb48lcCi_a9R81wPyEXygaagAC6R0AAnwQAAFI1vGgaFPHpJMpBA"
    await call.message.answer_video(
        video8, caption="38-dars. Takrorlash darsi"
    )
    video9 = "BAACAgIAAxkBAAIO3WMAAc21r08hkSXjXeLLTnHXNcmVhgACzx0AAnwQAAFILxGUlGBNWhMpBA"
    await call.message.answer_video(
        video9, caption="39-dars. Timer obyekti va undan foydalanish"
    )
    video10 = "BAACAgIAAxkBAAIOx2MAAcpsWAvGHHEFURksgTK1Af6zxAACmh0AAnwQAAFIcRKLl4fmj7opBA"
    await call.message.answer_video(
        video10, caption="40-dars. Timer obyekti va undan foydalanish", reply_markup=DavomVideo104
    )


@dp.callback_query_handler(text="davom104")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIOv2MAAck4WnmmGh_ShTWmi_ZMUnsZfgACbx0AAnwQAAFICljoQB0J2EEpBA'
    await call.message.reply_video(VDars1,
                                   caption="41-dars. Amaliy mashg'ulot. Timer obyekti va undan foydalanish")
    video2 = "BAACAgIAAxkBAAIO22MAAc1hNJZJZgiZ5I8J4YC0bhZLfwACzh0AAnwQAAFI5noqg7Ek7YopBA"
    await call.message.answer_video(
        video2, caption="42-dars. Rasmga boshqa obyektlarni joylash"
    )
    video3 = "BAACAgIAAxkBAAIO02MAAcxqh0dXTtVN2sF2-uWpEooZOAACvh0AAnwQAAFIx9CprfM7AAEGKQQ"
    await call.message.answer_video(
        video3, caption="43-dars. Amaliy mashg'ulot: Rasmga boshqa obyektlarni joylash"
    )
    video4 = "BAACAgIAAxkBAAIP1WMAAfWhNX8xf8Uaw00TmaH4dbQwpwACQx0AAnwQCEg9AQNymSeSpykE"
    await call.message.answer_video(
        video4, caption="44-dars. Kompyuter viruslari va viruslardan himoyalash usullari"
    )
    video5 = "BAACAgIAAxkBAAIO7WMAAc-t_cikqYPuCc7BxusU3yA1lAAC4B0AAnwQAAFIPsG8J5VwYuwpBA"
    await call.message.answer_video(
        video5, caption="45-dars. Grafik va animatsion ilovalarga misollar"
    )
    video6 = "BAACAgIAAxkBAAIOt2MAAchBHce3xI_x_2yziMmHanA0KAACUR0AAnwQAAFIeT0f3qnLEU8pBA"
    await call.message.answer_video(
        video6, caption="46-dars. Amaliy mashg'ulot. Grafik va animatsion ilovalarga misollar"
    )
    video7 = "BAACAgIAAxkBAAIOtWMAAcgPVXTfiXq6UfwNCHbRu8aHQQACSR0AAnwQAAFIkk6WOcKPApIpBA"
    await call.message.answer_video(
        video7, caption="47-dars. Yakuniy takrorlash darsit", reply_markup=DavomVideo105
    )


#######################################################################################################################################


@dp.callback_query_handler(text="Oldingi112")
@dp.callback_query_handler(text="11Video")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIRFGMB4uJ-5NaKarRJVXO2raPqEdyLAAJKGgACOUoRSOskBH9l5-QFKQQ'
    await call.message.reply_video(VDars1, caption="1-dars. Grafik obyektlar va ularni kompyuterda tasvirlash usullari")
    video2 = "BAACAgIAAxkBAAIRLGMB5lXJVJ5mFQABAwSgGWg-zaIhQgACahoAAjlKEUgJ2TR4eullvSkE"
    await call.message.answer_video(
        video2, caption="2-dars. Ikki va uch o'lchamli kompyuter grafikasi turlari"
    )
    video3 = "BAACAgIAAxkBAAIRKGMB5cZdvcvimGPuzdYTA04HHAt9AAJoGgACOUoRSCK9iUgkM9YkKQQ"
    await call.message.answer_video(
        video3, caption="3-dars. Photoshop - rastorli grafik muharririda ishlash asoslari. Photoshop interfeysi"
    )
    video4 = "BAACAgIAAxkBAAIREGMB4oMm_sE5KBvVHRgCPAs64UHcAAJHGgACOUoRSHTuQret9EWJKQQ"
    await call.message.answer_video(
        video4, caption="4-dars. Amaliy mashg'ulot"
    )
    video5 = "BAACAgIAAxkBAAIRSmMB6pZICimlhWvjIgbziSF51bYQAAKbGgACOUoRSPTtOwX5DkdIKQQ"
    await call.message.answer_video(
        video5, caption="5-dars. Takrorlash darsi"
    )
    video6 = "BAACAgIAAxkBAAIRMmMB50y-5dv4a6wXOWUWx3AVKcr7AAJxGgACOUoRSN80cEiscJagKQQ"
    await call.message.answer_video(
        video6, caption="6-dars. Photoshopning uskunalar paneli va palitralari"
    )
    video7 = "BAACAgIAAxkBAAIRQGMB6UWGHT4EF5EFiFfCotFwhIFHAAKPGgACOUoRSNAjdac18fhUKQQ"
    await call.message.answer_video(
        video7, caption="7-dars. Amaliy mashg'ulot"
    )
    video8 = "BAACAgIAAxkBAAIRKmMB5f_JCWV5N8eWdgHG9KESolyFAAJpGgACOUoRSJy-VINm_8SvKQQ"
    await call.message.answer_video(
        video8, caption="8-dars. Photoshopda grafik obyekt fayllari bilan ishlash"
    )
    video9 = "BAACAgIAAxkBAAIRNGMB53xJe8vRxj_SXR7q1ZSsEXLqAAJ0GgACOUoRSMhChx0bk_RcKQQ"
    await call.message.answer_video(
        video9, caption="9-dars. Photoshopda geometrik shakl ko'rinishidagi qismni ajratib olish."
    )
    video10 = "BAACAgIAAxkBAAIRJGMB5WbWQSJ9H-BUWEB9CMLF-O6SAAJlGgACOUoRSMuiQHDlupNfKQQ"
    await call.message.answer_video(
        video10, caption="10-dars . Tasvir bo'lagini ajratib olishning boshqa usullari",
        reply_markup=DavomVideo111
    )


@dp.callback_query_handler(text="Oldingi113")
@dp.callback_query_handler(text="davom111")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIRGGMB42srHVPKdp51_V7vLdpQdAGSAAJQGgACOUoRSBlFFRcJWj_vKQQ'
    await call.message.reply_video(VDars1,
                                   caption="11-dars. Tasvirlarni kadrlash va ulardan shakl almashtirish amallarini bajarish")
    video2 = "BAACAgIAAxkBAAIRRGMB6c2A-rjKiwYCpV2HtTbZplPjAAKVGgACOUoRSPPCHx9NRmSDKQQ"
    await call.message.answer_video(
        video2, caption="12-dars. Photoshopda qatlamlar va ulardan foydalanish"
    )
    video3 = "BAACAgIAAxkBAAIRTmMB6xKv8NP7XT-Ji-OauQkmJqpIAAKeGgACOUoRSDoNi-fGbqptKQQ"
    await call.message.answer_video(
        video3, caption="13-dars. Amaliy mashg'ulot."
    )
    video4 = "BAACAgIAAxkBAAIRCGMB4dVsONae9n-06W1p8-sGUJJeAAI_GgACOUoRSHIXTMb0P6mFKQQ"
    await call.message.answer_video(
        video4, caption="14-dars. Photoshopda rang tizimlari"
    )
    video5 = "BAACAgIAAxkBAAIRDGMB4iXRvZdAAx2vjqsCpF8fo9VPAAJCGgACOUoRSIJdEL-1KkHVKQQ"
    await call.message.answer_video(
        video5, caption="15-dars. Photoshopda ranglar bilan ishlash"
    )
    video6 = "BAACAgIAAxkBAAIRTGMB6tSaHLruqrLR8Rfgz4ZRyRtjAAKcGgACOUoRSCEbImCFyJAkKQQ"
    await call.message.answer_video(
        video6, caption="16-dars. Kanallar va filtrlar haqida ma'lumot"
    )
    video7 = "BAACAgIAAxkBAAIREmMB4qplswZoY_8knX9TPRfI7pJsAAJIGgACOUoRSG6vlfVB2bUGKQQ"
    await call.message.answer_video(
        video7, caption="17-dars. Qalam va mo'yqalam bilan ishlash"
    )
    video8 = "BAACAgIAAxkBAAIQ-mMB4KjBNYGPP0KD0uM6DmU4cHVEAAIvGgACOUoRSEPLZ3zf9xkGKQQ"
    await call.message.answer_video(
        video8,
        caption="18-dars. Amaliy mashg'ulot"
    )
    video9 = "BAACAgIAAxkBAAIRVmMB7AAB7HN_F0kNdVObXH68s-7UEAACphoAAjlKEUhOt1xB3behtSkE"
    await call.message.answer_video(
        video9, caption="19-dars. Tasvirga geometrik obyektlarni va vektorli obyektlarni joylash"
    )
    video10 = "BAACAgIAAxkBAAIRn2MCbhHsHOwIqL-M5Cz2xXwmrxkXAAItGgACOUoRSHzMrRBqrMXsKQQ"
    await call.message.answer_video(
        video10, caption="20-dars. Amaliy mashg'ulot",
        reply_markup=DavomVideo112
    )


@dp.callback_query_handler(text="Oldingi114")
@dp.callback_query_handler(text="davom112")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIRJmMB5Yuij1yxwFheKgfvsA6TGdbFAAJnGgACOUoRSP3vDKpP68kkKQQ'
    await call.message.reply_video(VDars1, caption="21-dars. Amaliy mashg'ulot")
    video2 = "BAACAgIAAxkBAAIRAAFjAeEckPF9Jyr6vnMKpJlOhkEs6wACOBoAAjlKEUiVAQ97AAFkygMpBA"
    await call.message.answer_video(
        video2, caption="22-dars. Web-sahifa, Web-sayt va Web-dizayn tushunchalari"
    )
    video3 = "BAACAgIAAxkBAAIRBmMB4aCCX_yQkF8yUZEPt5s9MVoxAAI8GgACOUoRSCmWd67fgYRXKQQ"
    await call.message.answer_video(
        video3, caption="23-dars. Amaliy mashg'ulot"
    )
    video4 = "BAACAgIAAxkBAAIRRmMB6fucAniuTbJpMgEzUHeCrd6TAAKWGgACOUoRSOcb40_KOqiIKQQ"
    await call.message.answer_video(
        video4,
        caption="24-dars. Web-dizayn va uning dasturiy ta'minoti. Macromedia Flash dasturi yordamida Web-sahifa va yaratish va bezash"
    )
    video5 = "BAACAgIAAxkBAAIRXmMB7Vv2Cy9kG-5Xs57Xlj2cPM9HAAKxGgACOUoRSHpStOGJpSzcKQQ"
    await call.message.answer_video(
        video5, caption="25-dars. Amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIRYmMB7eIYYpFP1topbwxenwRP_zcTAAK2GgACOUoRSGSPyV-GbmabKQQ"
    await call.message.answer_video(
        video6, caption="26-dars. Web-sahifalarga rasmli, grafikli ma'lumotlarni joylashtirish va bezash"
    )
    video7 = "BAACAgIAAxkBAAIRAmMB4UHYUl8LN6JDp2CsPrgEKA5OAAI6GgACOUoRSB1l-sfUcKVoKQQ"
    await call.message.answer_video(
        video7, caption="27-dars. Amaliy mashg'ulot"
    )
    video8 = "BAACAgIAAxkBAAIRCmMB4gABcEA-63IZ-r8ztt6YusBATAACQBoAAjlKEUgF7HpCW89kyCkE"
    await call.message.answer_video(
        video8,
        caption="28-dars. Takrorlash darsi"
    )
    video9 = "BAACAgIAAxkBAAIRWGMB7Da0_H5NFnAvru0UFGfnB-FTAAKnGgACOUoRSEOJZXfYEnGvKQQ"
    await call.message.answer_video(
        video9, caption="29-dars. Web sahifada formalar yaratish va bezash"
    )
    video10 = "BAACAgIAAxkBAAIRPGMB6HuIgOLAUiy_GurzFuPd4iKQAAKGGgACOUoRSMOrlpwNtbP-KQQ"
    await call.message.answer_video(
        video10, caption="30-dars. Takrorlash darsi",
        reply_markup=DavomVideo113
    )


@dp.callback_query_handler(text="Oldingi115")
@dp.callback_query_handler(text="davom113")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIROGMB5_Ejj1_8rAGjGqxbIfCd054oAAJ9GgACOUoRSPIHrjnKez6TKQQ'
    await call.message.reply_video(VDars1, caption="31-dars. Web-sahifalarda animatsiya va ularni o'rnatish")
    video2 = "BAACAgIAAxkBAAIRLmMB5oBFEuMojYpL3-Vi41y5FJctAAJrGgACOUoRSJN5RwfWfcE8KQQ"
    await call.message.answer_video(
        video2,
        caption="32-dars. Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIRQmMB6XyEqQ2EEbjCweXShksbFpqPAAKSGgACOUoRSAK2gawxtGEzKQQ"
    await call.message.answer_video(
        video3, caption="33-dars. Tovushli ma'lumotlar va ular bilan ishlash"
    )
    video4 = "BAACAgIAAxkBAAIRXGMB7O-JLFVn8jkh5DNcIEcLfIgfAAKsGgACOUoRSLjuQeK_BMI9KQQ"
    await call.message.answer_video(
        video4, caption="34-dars. Takrorlash darsi"
    )
    video5 = "BAACAgIAAxkBAAIRHmMB5K4_Qhq1LlG_jWj-LsJDd9yeAAJdGgACOUoRSJAYTOBhsnNKKQQ"
    await call.message.answer_video(
        video5, caption="35-dars. Amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIRYGMB7ZUrQsgTToXp8CKt2ZQqR5B5AAKzGgACOUoRSNbChzzi7V_aKQQ"
    await call.message.answer_video(
        video6, caption="36-dars. Amaliy mashg'ulot"
    )
    video7 = "BAACAgIAAxkBAAIRWmMB7HqyNfOEViQsL9cK42X1CX6mAAKpGgACOUoRSL301Mp-OZE_KQQ"
    await call.message.answer_video(
        video7,
        caption="37-dars. Web-sahifalar orasida aloqalarni o'rnatish imkoniyatlari"
    )
    video8 = "BAACAgIAAxkBAAIRMGMB5rYR8sdhBBBmRoNP30yFzNcpAAJtGgACOUoRSKlxyurY2aY-KQQ"
    await call.message.answer_video(
        video8, caption="38-dars. Amaliy mashg'ulot"
    )
    video9 = "BAACAgIAAxkBAAIRNmMB560VbF0oW41JveU6_O8Zv4rUAAJ3GgACOUoRSH3PIUPIPPk_KQQ"
    await call.message.answer_video(
        video9, caption="39-dars. Amaliy mashg'ulot"
    )
    video10 = "BAACAgIAAxkBAAIRPmMB6PK1iHz1MBBmqyeQ6evjgwT3AAKMGgACOUoRSFwHB2A-UrN0KQQ"
    await call.message.answer_video(
        video10, caption="40-dars. Axborot xavfsizligi tushunchasi va samaradorligi ko'rsatkichlari",
        reply_markup=DavomVideo114
    )


@dp.callback_query_handler(text="Oldingi116")
@dp.callback_query_handler(text="davom114")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIQ_GMB4MurDvao7J90hTw_Bc-oM4wmAAI0GgACOUoRSDwEfciqizymKQQ'
    await call.message.reply_video(VDars1,
                                   caption="41-dars. Axborot xavfsizligi muammolari. Axborotlarni himoyalashning tarkibiy qismlari va usullari")
    video2 = "BAACAgIAAxkBAAIRBGMB4XLXF9KScQABsEl-pcjDpARjBQACOxoAAjlKEUj4DqJ9XJ8cLCkE"
    await call.message.answer_video(
        video2, caption="42-dars. Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIhcmMWIumja2-77i_jJZol1kNcvZHiAAIqHQACCg6xSOJqsozDvoySKQQ"
    await call.message.answer_video(
        video3, caption="43-dars. Amaliy mashg'ulot: Rasmga boshqa obyektlarni joylash"
    )
    video4 = "BAACAgIAAxkBAAIRDmMB4kv9BlxqTtvisNNf9WDd6xJOAAJEGgACOUoRSHRgOcUS2HSiKQQ"
    await call.message.answer_video(
        video4, caption="44-dars. Mintaqaviy va global kompyuter tarmog'i va uni himoyalash"
    )
    video5 = "BAACAgIAAxkBAAIRFmMB4yJFE1EV_zpN6C6xUe3vssK6AAJLGgACOUoRSOGAOQ5b3qbFKQQ"
    await call.message.answer_video(
        video5, caption="45-dars. Amaliy mashg'ulot"
    )
    video6 = "BAACAgIAAxkBAAIRUmMB63h06pbVkAizhRbgh-wjpkCKAAKiGgACOUoRSHgQtyJcWKlFKQQ"
    await call.message.answer_video(
        video6, caption="46-dars. Internetda saqlanayotgan axborot manbalarining xavfsizligi muammolari"
    )
    video7 = "BAACAgIAAxkBAAIRHGMB5CrWKwQk8e23l2Iv9MM-XGpOAAJXGgACOUoRSPu7Bqu6lzu5KQQ"
    await call.message.answer_video(
        video7, caption="47-dars. Amaliy mashg'ulot"
    )
    video8 = "BAACAgIAAxkBAAIRGmMB49_1rneBYoItsA90wAFLyAgIAAJTGgACOUoRSOClkBTBlJ_LKQQ"
    await call.message.answer_video(
        video8, caption="48-dars. Elektron hukumat"
    )
    video9 = "BAACAgIAAxkBAAIRSGMB6kPHgc9wcKslacmGAnttmahYAAKYGgACOUoRSCM1Ve-tvHYUKQQ"
    await call.message.answer_video(
        video9, caption="49-dars. Amaliy mashg'ulot"
    )
    video10 = "BAACAgIAAxkBAAIROmMB6EL_olQg7V-WWIPAG0cSqluCAAKFGgACOUoRSLtoSwwSzLg6KQQ"
    await call.message.answer_video(
        video10, caption="50-dars. Elektron pochta xizmati tuzilmasi", reply_markup=DavomVideo115
    )


@dp.callback_query_handler(text="davom115")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIRImMB5SgEOhGFvK_t5Pmr4wkOS8hcAAJjGgACOUoRSNJHY0btx86zKQQ'
    await call.message.reply_video(VDars1,
                                   caption="51-dars. Amaliy mashg'ulot")
    video2 = "BAACAgIAAxkBAAIQ_mMB4O4qd0xFRPXUJyRW9XNiFSKmAAI1GgACOUoRSIkg9fpbQI2pKQQ"
    await call.message.answer_video(
        video2, caption="52-dars. Amaliy mashg'ulot"
    )
    video3 = "BAACAgIAAxkBAAIRVGMB69Z2N_MJnSDXmW1d3qgVQBfCAAKjGgACOUoRSOdfORMAASWiwSkE"
    await call.message.answer_video(
        video3, caption="53-dars. Takrorlash darsi"
    )
    video4 = "BAACAgIAAxkBAAIRUGMB606MvBrLWZv7MudrvCNwm2DjAAKhGgACOUoRSFx_dJkkhoSiKQQE"
    await call.message.answer_video(
        video4, caption="54-dars. Mustahkamlash darsi", reply_markup=DavomVideo116
    )


#######################################################################################################################

@dp.callback_query_handler(text="TestATT")
async def Test(call: CallbackQuery):
    Test_id1 = "BQACAgIAAxkBAAIoL2NiiByoufVnH9Ga4G-xEtr5uDZyAAJVHQACJQj5STwBjPPV8PKkKgQ"
    await call.message.answer_document(Test_id1)
    Test_id2 = "BQACAgIAAxkBAAIoO2NiiCsAAXAoXWfEUHW7q9LydmBU6wACmRsAAgm4iEpzqo_qA9StByoE"
    await call.message.answer_document(Test_id2)
    Test_id3 = "BQACAgIAAxkBAAIoPWNiiDk-P-WJI2zRSw3R7TjYpyLiAAKAHwACXHKRSj3YFTAKwJkaKgQ"
    await call.message.answer_document(Test_id3)
    Test_id4 = "BQACAgIAAxkBAAIoP2NiiEurIwl9o6paoOgVjTdzEUaDAAJtFAACLBr4SBNkDyIxk0f3KgQ"
    await call.message.answer_document(Test_id4)
    Test_id5 = "BQACAgIAAxkBAAIoQWNiiFXlWSE3cQbe5OklFtLpIkFyAAL-GwACYAgoSmXwFvRID9mYKgQ"
    await call.message.answer_document(Test_id5)
    Test_id6 = "BQACAgIAAxkBAAIoQ2NiiF-VrU0hw1tTzQPKbkvN5tIJAAMcAAJgCChKIpW6y_Z5F_gqBA"
    await call.message.answer_document(Test_id6)
    Test_id7 = "BQACAgIAAxkBAAIoRWNiiGxO43-OTbBqBQABj8ORhyIIcQACAxwAAmAIKEpejW7_FA76LCoE"
    await call.message.answer_document(Test_id7)
    Test_id8 = "BQACAgIAAxkBAAIoR2NiiHYX2P-7Cpa5XucAAZdOAAFcNy8AAl8UAAKt2ChKvI2WPq7e_dQqBA"
    await call.message.answer_document(Test_id8)
    Test_id9 = "BQACAgIAAxkBAAIoSWNiiH9YPEoHqgAB2f_4_o0GsTodngACYBQAAq3YKEqCpwSLc946MyoE"
    await call.message.answer_document(Test_id9)
    Test_id10 = "BQACAgIAAxkBAAIoS2NiiIgOIFXNX51An1Rc0hBadMABAAMeAAKxmvBKwPPvtvRglUYqBA"
    await call.message.answer_document(Test_id10 , reply_markup=Boshmenu)



@dp.callback_query_handler(text="5Testru")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVYmMD67XGRV5EEg8KzZlpUNJBAbkbAAJxIgACe2UhSPh5kAXm5Q48KQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="5Test")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVVGMD6ow9esY3VyfTS053jhyCod-2AAJoIgACe2UhSDryD4ZyF3yuKQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="8Test")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVVmMD6pLu5VLxJNrvQ30CmiPQfNZAAAJpIgACe2UhSCJmwY6nXfaUKQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="9Test")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVWGMD6piMx02YjapiBabDRW94KbK8AAJqIgACe2UhSOQomwJcZP1cKQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="5Kitobru")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVWmMD6r0_hK5Sb0h3CXSJNlmHE1BTAAJsIgACe2UhSJsebt2YD7ijKQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="6Kitobru")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVXGMD6uRR5NTGH2XQ2LbIiBCWhXcmAAJtIgACe2UhSBsNt-0WBLZoKQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="8Kitobru")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVXmMD6zBJAbWog10gcMiU8F08G_jRAAJuIgACe2UhSJh1rBvam2itKQQ"
    await call.message.answer_document(Test_id)


@dp.callback_query_handler(text="9Kitobru")
async def Test(call: CallbackQuery):
    Test_id = "BQACAgIAAxkBAAIVYGMD6zaVLVOTnJ1sXVgbrlkdLXEVAAJvIgACe2UhSOC6FQTozh-RKQQ"
    await call.message.answer_document(Test_id)


###################################################################################################################


@dp.callback_query_handler(text="VideoAtt")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIV2mMD74hC084vlX35g_iUyhM2ogwEAAJVDgACtlEoSUUAAWwVk7vOuCkE'
    await call.message.reply_video(VDars1, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI")
    video2 = "BAACAgIAAxkBAAIV3GMD74-in2HMst7klZpKygTNJceRAAJbDgACtlEoSY-MclGb71qHKQQ"
    await call.message.answer_video(
        video2, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI "
    )
    video3 = "BAACAgIAAxkBAAIV3mMD75oYYEvdw2_CEHDLhXBoEk0gAAL_DAACa2gISOWOF8UP43iVKQQ"
    await call.message.answer_video(
        video3, caption="📹 ATTESTATSIYAGA TUSHGAN ALI, VALI, SOLI, XOLI, TOIR, ZOIR, HALIL MASALA VA MISOLLAR YECHIMI "
    )
    video4 = "BAACAgIAAxkBAAIV4GMD76O_35X4Rgjd27gJc1Cu2Y4tAAKqCwACysSJSFvGGs1KWwt5KQQ"
    await call.message.answer_video(
        video4, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI "
    )
    video5 = "BAACAgIAAxkBAAIV4mMD77CtFcnIQm49I8wtpqFUVHEoAAJzCQACAofwSO7jbAABctvFlSkE"
    await call.message.answer_video(
        video5, caption="📹 GRAFIK MA'LUMOTLARNI KODLASH | ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI"
    )
    video6 = "BAACAgIAAxkBAAIV5GMD78mxSsLDPur2RXeXmzJr_BfrAAJiDgACtlEoSR76LEE3xtnhKQQ"
    await call.message.answer_video(
        video6, caption="📹 INFORMATIKA FANIDAN 2020 YILDA ATTESTATSIYAGA TUSHGAN MISOL VA MASALALAR YECHIMI"
    )
    video7 = "BAACAgIAAxkBAAIV5mMD79X4HNE6qu77tHiaO6wkt9zRAAJnDgACtlEoSaCKATGu4YSgKQQ"
    await call.message.answer_video(
        video7, caption="📹 2020 YILDA ATTESTATSIYAGA TUSHGAN MISOL VA MASALALAR YECHIMI"
    )
    video8 = "BAACAgIAAxkBAAIV6GMD7-K56I4xSmMGunDkQ9Gw3wHbAAK-CgACntjASMtfGQ1MsXUjKQQ"
    await call.message.answer_video(
        video8, caption="📹 MODELLASHTIRISH VA DASTURLASH (OBUNACHILAR TOMONIDAN KELGAN SAVOLLAR) "
    )
    video9 = "BAACAgIAAxkBAAIV6mMD7-pqIxhH8fyOIDKymV_NcxqWAAKMCwACysSJSH-x5XpNhnvWKQQ"
    await call.message.answer_video(
        video9, caption="📹 OBUNACHILARDAN KELGAN SAVOLLAR (-514 NI ICHKI KO’RINISHI, INTERNETDA SO’ROVLAR)"
    )
    video10 = "BAACAgIAAxkBAAIV7GMD7_GvzDxglVVMspRLnwgssxMfAAJyDgACtlEoSSvIIerakL4gKQQ"
    await call.message.answer_video(
        video10, caption="📹 MODELLASHTIRISH VA DASTURLASH. ALI, VALI",
        reply_markup=Att1
    )


@dp.callback_query_handler(text="AttO2")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIV2mMD74hC084vlX35g_iUyhM2ogwEAAJVDgACtlEoSUUAAWwVk7vOuCkE'
    await call.message.reply_video(VDars1, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI")
    video2 = "BAACAgIAAxkBAAIV3GMD74-in2HMst7klZpKygTNJceRAAJbDgACtlEoSY-MclGb71qHKQQ"
    await call.message.answer_video(
        video2, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI "
    )
    video3 = "BAACAgIAAxkBAAIV3mMD75oYYEvdw2_CEHDLhXBoEk0gAAL_DAACa2gISOWOF8UP43iVKQQ"
    await call.message.answer_video(
        video3, caption="📹 ATTESTATSIYAGA TUSHGAN ALI, VALI, SOLI, XOLI, TOIR, ZOIR, HALIL MASALA VA MISOLLAR YECHIMI "
    )
    video4 = "BAACAgIAAxkBAAIV4GMD76O_35X4Rgjd27gJc1Cu2Y4tAAKqCwACysSJSFvGGs1KWwt5KQQ"
    await call.message.answer_video(
        video4, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI "
    )
    video5 = "BAACAgIAAxkBAAIV4mMD77CtFcnIQm49I8wtpqFUVHEoAAJzCQACAofwSO7jbAABctvFlSkE"
    await call.message.answer_video(
        video5, caption="📹 GRAFIK MA'LUMOTLARNI KODLASH | ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI"
    )
    video6 = "BAACAgIAAxkBAAIV5GMD78mxSsLDPur2RXeXmzJr_BfrAAJiDgACtlEoSR76LEE3xtnhKQQ"
    await call.message.answer_video(
        video6, caption="📹 INFORMATIKA FANIDAN 2020 YILDA ATTESTATSIYAGA TUSHGAN MISOL VA MASALALAR YECHIMI"
    )
    video7 = "BAACAgIAAxkBAAIV5mMD79X4HNE6qu77tHiaO6wkt9zRAAJnDgACtlEoSaCKATGu4YSgKQQ"
    await call.message.answer_video(
        video7, caption="📹 2020 YILDA ATTESTATSIYAGA TUSHGAN MISOL VA MASALALAR YECHIMI"
    )
    video8 = "BAACAgIAAxkBAAIV6GMD7-K56I4xSmMGunDkQ9Gw3wHbAAK-CgACntjASMtfGQ1MsXUjKQQ"
    await call.message.answer_video(
        video8, caption="📹 MODELLASHTIRISH VA DASTURLASH (OBUNACHILAR TOMONIDAN KELGAN SAVOLLAR) "
    )
    video9 = "BAACAgIAAxkBAAIV6mMD7-pqIxhH8fyOIDKymV_NcxqWAAKMCwACysSJSH-x5XpNhnvWKQQ"
    await call.message.answer_video(
        video9, caption="📹 OBUNACHILARDAN KELGAN SAVOLLAR (-514 NI ICHKI KO’RINISHI, INTERNETDA SO’ROVLAR)"
    )
    video10 = "BAACAgIAAxkBAAIV7GMD7_GvzDxglVVMspRLnwgssxMfAAJyDgACtlEoSSvIIerakL4gKQQ"
    await call.message.answer_video(
        video10, caption="📹 MODELLASHTIRISH VA DASTURLASH. ALI, VALI",
        reply_markup=Att1
    )


@dp.callback_query_handler(text="AttO3")
@dp.callback_query_handler(text="AttD1")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIV7mMD7_ebkYqZYAabovhqqd3sogh4AAJzDgACtlEoSQpcpqrNwGQLKQQ'
    await call.message.reply_video(VDars1, caption="📹 MODELLASHTIRISH VA DASTURLASH. RANDOM, INT, WHILE")
    video2 = "BAACAgIAAxkBAAIV8GMD7_xrDImQJwFX9Sd2tX1rRNnjAAIuCAACIYLpSBjcFwABdzfl6SkE"
    await call.message.answer_video(
        video2, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN NAMUNAVIY MISOL VA MASALALAR YECHIMI"
    )
    video3 = "BAACAgIAAxkBAAIV8mMD8AvjZwyGW8DbY1_U6jlSQNOKAAK6CgACNFGoSNsS2THLJfL7KQQ"
    await call.message.answer_video(
        video3, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN NAMUNAVIY MISOL VA MASALALAR YECHIMI"
    )
    video4 = "BAACAgIAAxkBAAIV9GMD8BKee3pBQ_Djzc2lk3w93k8EAAJWDQAC2vC5SAExejgzOB7QKQQ"
    await call.message.answer_video(
        video4, caption=" ATTESTATSIYAGA TAYYORLANAYOTGAN O'QITUVCHILAR UCHUN KODLASHGA DOIR MISOLLAR YECHIMI"
    )
    video5 = "BAACAgIAAxkBAAIV9mMD8BlUlvhMemquaxpuQN1Xg6N2AAJVDQAC2vC5SO1qEC9ywOIPKQQ"
    await call.message.answer_video(
        video5, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TAYYORLANAYOTGANLAR UCHUN FANO DARAXTI MANTIQ DASTURLASH"
    )
    video6 = "BAACAgIAAxkBAAIV-GMD8B-dJFVvHw6lN7qzIPxb7wE_AAJtDAAC2vDBSDPMAZ_bTjUNKQQ"
    await call.message.answer_video(
        video6, caption="📹 ATTESTATSIYAGA TAYYORLANAYOTGAN  O'QITUVCHILAR UCHUN  HTML TILIGA DOIR MISOLLAR YECHIMI"
    )
    video7 = "BAACAgIAAxkBAAIV-mMD8CVdyXVXJYFBEa4WKkET7OKiAAITCgACJ0_RSNj6ZXjPbUEtKQQ"
    await call.message.answer_video(
        video7, caption="📹 INFORMATIKA FANIDAN 2020 YILDA ATTESTATSIYAGA TUSHGAN MISOL VA MASALALAR YECHIMI "
    )
    video8 = "BAACAgIAAxkBAAIV_GMD8Cz-uVfRi2fPyvyXyIXgEKC4AALSBwACIYLpSPqynUWAlw3lKQQ"
    await call.message.answer_video(
        video8,
        caption="📹 INFORMATIKA FANIDAN 2020 YILDA ATTESTATSIYAGA TUSHGAN MISOL VA MASALALAR YECHIMI"
    )
    video9 = "BAACAgIAAxkBAAIV_mMD8DT8EyKnjJr6Seb-xR9S2XfCAAJkCgACTSXpSBB1_h1onW2RKQQ"
    await call.message.answer_video(
        video9, caption="📹 QO‘ZG‘ALMAS NUQTALI SONLARNI TURLI SANOQ TIZIMLARIGA O’TKAZISH, AXBOROT UZATISH TEZLIGIGI"
    )
    video10 = "BAACAgIAAxkBAAIWAAFjA_A6Zx-NNGlvVUaiR2DR7xigzQACVAkAAga46EgcDRqYbR8XaikE"
    await call.message.answer_video(
        video10, caption="📹 KHZ (КИЛОГЕРЦ), TOVUSH CHASTOTASI, DISKETDAGI SEKTORLAR, AXBOROT HAJMI ",
        reply_markup=Att2
    )


@dp.callback_query_handler(text="AttO4")
@dp.callback_query_handler(text="AttD2")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIWAmMD8EPK1A8Ty3Jkl5B-u_o9nWCDAAJ9CQACSLUAAUmddzQu52eCEykE'
    await call.message.reply_video(VDars1, caption="📹 MASSIV ELEMENTLARI QIYMATLARINI YIG'INDISINI HISOBLASH")
    video2 = "BAACAgIAAxkBAAIWBGMD8ElrHQwUcXfpz78CdtumXtuoAAJ8CQACSLUAAUmgbDzhRb3BHykE"
    await call.message.answer_video(
        video2, caption="📹 PYTHON DASTURLASH TILIDA O'ZGARUVCHILAR TAVSIFLASH VA PRINT OPERATORIGA DOIR DASTURLAR"
    )
    video3 = "BAACAgIAAxkBAAIWBmMD8E_QFquBX3YZ0OzdFm0DEXt3AAIGDAACP0AIScz98MuxFMyuKQQ"
    await call.message.answer_video(
        video3, caption="📹 INPUT OPERATORI, TYPE FUNKSIYASIGA DOIR DASTURLAR (PYTHON DASTURLASH TILIDA)"
    )
    video4 = "BAACAgIAAxkBAAIWCGMD8Fiy7gKfrQKF3dIKSpOxVNboAAKJDAAC8EIRSUphGlxce8VmKQQ"
    await call.message.answer_video(
        video4, caption="📹 WHILE, REPEAT TAKRORLANISH OPERATORLARI (OBUNACHILAR TOMONIDAN YUBORILGAN SAVOLLAR)"
    )
    video5 = "BAACAgIAAxkBAAIWCmMD8GOOLVwfqMHJBgYpF1Am3_51AAJ-CwAC8EIhSU0M-RsS7x_TKQQ"
    await call.message.answer_video(
        video5, caption="PYTHON DASTURLASH TILI (% BO'LINMANI QOLDIG'I, // BUTUN QIYMATI, ** DARAJAGA KO'TARISH)"
    )
    video6 = "BAACAgIAAxkBAAIWDGMD8G5bawNOxl2qVVUy9AYSrfdKAAJuDQAC9RA4SVbmoRZ6EfPmKQQ"
    await call.message.answer_video(
        video6, caption="📹 PYTHON DASTURLASH TILI (SATR UZUNLIGI, PINGVIN, KVADRAT, UCHBURCHAK SHAKLLARINI YASASH)"
    )
    video7 = "BAACAgIAAxkBAAIWDmMD8IPZ1oOtQLpLRNAMHZ_rjvbiAAJwDQAC9RA4SSL0mELAarlkKQQ"
    await call.message.answer_video(
        video7, caption=" PYTHON DASTURLASH TILI (SPLIT USULI, SEP, END PRINT FUNKSIYASINING ARGUMENTLARI)"
    )
    video8 = "BAACAgIAAxkBAAIWEGMD8Ik6GxtAON7SkQz-gYn5t9NUAAKuDQACfiZISZsppBl58Nn5KQQ"
    await call.message.answer_video(
        video8,
        caption="📹 PYTHON DASTURLASH TILI (ANVAR, DILSHOD, MAHMUD, BOG`BON, TEZLANISH, KUCH, MASSA, YUZA)"
    )
    video9 = "BAACAgIAAxkBAAIWEmMD8JJ036K-j3vz1Arnka4vckv0AAKJCgACAkahSfzOyi8soN9dKQQ"
    await call.message.answer_video(
        video9, caption="📹 PYTHON DASTURLASH TILI (CHUMOLI, AVTOBUS YURGAN MASOFA, KVADRAT, DOIRA YUZI) "
    )
    video10 = "BAACAgIAAxkBAAIWFGMD8J_kl3q9W9QyMApeyiMPJTD7AALrCQACWOhhScC8kk8jXraFKQQ"
    await call.message.answer_video(
        video10, caption="📹 PYTHONDA MANTIQIY MASALALARNI DASTURLASH (OR, AND, NOT) ",
        reply_markup=Att3
    )


@dp.callback_query_handler(text="AttO5")
@dp.callback_query_handler(text="AttD3")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIWFmMD8Kgk5_y7Ykn6HEWugdfG9CNyAAIDDAACfWWISdvkf2gTgapUKQQ'
    await call.message.reply_video(VDars1,
                                   caption="📹 PYTHON DASTURLASH TILI (ALGORITMLARNI DASTURLASH. IF…ELSE OPERATORI)")
    video2 = "BAACAgIAAxkBAAIWGGMD8RPSW-qgowxaR4Uhj5m4kjSYAAJADAACw_hxSZ0qVHY3auuLKQQ"
    await call.message.answer_video(
        video2,
        caption="📹 PYTHON DASTURLASH TILI (TARMOQLANUVCHI ALGORITMLARNI DASTURLASH. ELIF OPERATORI)"
    )
    video3 = "BAACAgIAAxkBAAIWGmMD8XC8L333UpJq7jicxV5kibnDAAJsCQACUwqASd_OSSMWN2sFKQQ"
    await call.message.answer_video(
        video3, caption="📹 PYTHON DASTURLASH TILI (TAKRORLANUVCHI ALGORITMLARNI DASTURLASH. FOR OPERATORI)"
    )
    video4 = "BAACAgIAAxkBAAIWHGMD8XRe-6BBsrD02JA8mrGt1i7_AALQDgAC_uOASRcxJK2u94jjKQQ"
    await call.message.answer_video(
        video4, caption="📹 PYTHON DASTURLASH TILI (FOR OPERATORI, MAXSULOT NARXI, SUTKANING N SEKUNDI, OXIRGI RAQAM) "
    )
    video5 = "BAACAgIAAxkBAAIWHmMD8YBu23xoFhi7ibRvWAfUhxsOAALACQACrNOgScVU6cx8IARVKQQ"
    await call.message.answer_video(
        video5, caption="📹 PYTHON DASTURLASH TILI (WHILE OPERATORI, NATURAL SONNI BO`LUVCHILARI)"
    )
    video6 = "BAACAgIAAxkBAAIWIGMD8YcxB_DUKrCxSGtatOtJZvpBAALkCgACbnugSfNY_YX66veeKQQ"
    await call.message.answer_video(
        video6, caption="📹 ATTESTATSIYAGA TAYYORLANAYOTGANLAR UCHUN INFORMATIKA FANIDAN MISOL VA MASALALAR YECHIMI"
    )
    video7 = "BAACAgIAAxkBAAIWImMD8ZZaRDAZA3vRxkdz81bbNqNgAAKsDAACkvLBSWAV5OmjNVK4KQQ"
    await call.message.answer_video(
        video7,
        caption="PYTHON DASTURLASH TILI (BREAK OPERATORI)"
    )
    video8 = "BAACAgIAAxkBAAIWJGMD8Z7tJyGbXuzp9c0nQyzj0qoxAALDCwACWuz5ScXl2koS9RuuKQQ"
    await call.message.answer_video(
        video8, caption="📹 ATTESTATSIYAGA TAYYORLANAYOTGANLAR UCHUN INFORMATIKA FANIDAN MISOL VA MASALALAR YECHIMI"
    )
    video9 = "BAACAgIAAxkBAAIWJmMD8aXYEKP1SySLm6XQeyC7jL6lAAIvCgACj5roSfoB0pFakpxiKQQ"
    await call.message.answer_video(
        video9, caption="📹 PYTHON DASTURLASH TILI (QISM DASTURLAR. FUNKSIYALAR VA PROTSEDURALAR)"
    )
    video10 = "BAACAgIAAxkBAAIWKGMD8bfwYV05vREvGR2f1H4QDJk6AAK7DAAC3ej5SeROsOxxJ2J3KQQ"
    await call.message.answer_video(
        video10, caption="📹 2020 YIL ATTESTATSIYAGA TUSHGAN ALI, VALI, ... MASALALAR YECHIMLARI ", reply_markup=Att4
    )


@dp.callback_query_handler(text="AttO6")
@dp.callback_query_handler(text="AttD4")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIWKmMD8cGFepVJhPlzQUZX-_Zvnsb5AAJOCQACVuEQSsoPuBHSb0ZyKQQ'
    await call.message.reply_video(VDars1,
                                   caption="📹 INFORMATIKA FANIDAN ONLAYN-REPETITSIYA MASALALAR YECHIMI ")
    video2 = "BAACAgIAAxkBAAIWLGMD8c2hQq9T24JLdAYxLat6K8K_AAIlCQACX0owSs2cZulQQa1cKQQ"
    await call.message.answer_video(
        video2, caption="📹 PYTHON DASTURLASH TILI (FUNKSIYALAR VA O'ZGARUVCHILAR, PROTSEDURALAR) "
    )
    video3 = "BAACAgIAAxkBAAIWLmMD8dM9b8N7mG5BWsyzJ8qJ8RucAAJCCgACkXdwSn37WyN5E_szKQQ"
    await call.message.answer_video(
        video3, caption="📹 PYTHON DASTURLASH TILI KUTUBXONASI (RANDOM VA MATH MODULI)"
    )
    video4 = "BAACAgIAAxkBAAIWMGMD8dnZyvenZOtltvDjAAFm_NOwXgACoA4AArMViEoKQLUUUsaG2ykE"
    await call.message.answer_video(
        video4,
        caption="📹 PYTHONDA FOYDALANUVCHI GRAFIK INTERFEYSI (Tkinter moduli, OptionMenu, Button, Text vijetlar)"
    )
    video5 = "BAACAgIAAxkBAAIWMmMD8eBAViWKK-Z8aCyLujJPniR9AAKkCAACe52RSlnZunMPjje_KQQ"
    await call.message.answer_video(
        video5, caption="📹 PYTHONDA FOYDALANUVCHINING GRAFIK INTERFEYSI (GUI). EKUB, EKUK, TUB SON. "
    )
    video6 = "BAACAgIAAxkBAAIWNGMD8epSH2LMI9FQrxA3CKQF57fdAAL0DAACgYjQSnPl5CUeWoqUKQQ"
    await call.message.answer_video(
        video6, caption="📹 PYTHON DASTURLASH TILI (SONNI AKSLANTIRISH, CANVAS, BELGINI ALMASHTIRISH)"
    )
    video7 = "BAACAgIAAxkBAAIWNmMD8fHiq1KgqjnSKjPoiFKBZQSEAAJUCwAC-4fhSuj3ScZZsM2LKQQ"
    await call.message.answer_video(
        video7, caption="📹 PYTHON DASTURLASH TILI (SHILLIQQURT, KALKULYATOR, PINGVIN DASTURI)"
    )
    video8 = "BAACAgIAAxkBAAIWOGMD8fkR7XLki2VZGWOapl4ZFNDRAAIbCgAC5GHYS4a_VC3UrOtJKQQ"
    await call.message.answer_video(
        video8, caption="📹 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN MASALALAR YECHIMI"
    )
    video9 = "BAACAgIAAxkBAAIWOmMD8f8DIybdm1zcW1MrfAQJ8OkLAAL_DAAC28xBS4TThdTNM4DOKQQ"
    await call.message.answer_video(
        video9, caption="📹 2021 INFORMATIKA FANIDAN ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI (61-DARS)"
    )
    video10 = "BAACAgIAAxkBAAIWPGMD8gnEunx-R_9R88Nv8pnqiBeQAAJVCwACO1DZSwe9CYrwgj-tKQQ"
    await call.message.answer_video(
        video10, caption="📹 OBUNACHILARIMIZ TOMONIDAN YUBORILGAN 2021-YILDA ATTESTATSIYAGA TUSHGAN SAVOLLAR YECHIMI",
        reply_markup=Att5
    )


@dp.callback_query_handler(text="AttD5")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIWPmMD8hQEbEr42J3hXhWvAAHjLsji0wACtBYAAguVyEhAzRKCkcY-wykE'
    await call.message.reply_video(VDars1,
                                   caption="📹 ATTESTATSIYA 2021-YIL PYTHON DASTURLASH TILINING FOR OPERATORI SAVOLLAR YECHIMI")
    video2 = "BAACAgIAAxkBAAIWQGMD8h840wI3EidbK_joqe2H14TMAAKrEwACBNMISgm9QTmNE7ykKQQ"
    await call.message.answer_video(
        video2, caption="📹 ATTESTATSIYA 2022-YIL IP manzili, Tarmoq maskasi, Tarmoq manzili, List, Funksiya"
    )
    video3 = "BAACAgIAAxkBAAIWQmMD8iq4TbGUyhuPaqs7G8matqtQAAIUFQACy90xShf8G16mtDd8KQQ"
    await call.message.answer_video(
        video3, caption="📹 ATTESTATSIYA 2022-YIL Bitwise operatorlar (|, &), Bug'doy maydoni, Zinama-zina masalasi"
    )
    video4 = "BAACAgIAAxkBAAIWRGMD8jPkdKjgpo-u4e6l3L11EgjqAAIFGwAC80lhS0xzlYebj74oKQQ"
    await call.message.answer_video(
        video4, caption="📹 Bug'doy maydoni. Tenglama, ildizga doir sanoq sistemalari.", reply_markup=Att6
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi52ru")
@dp.callback_query_handler(text="5Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIYVmMM6m5a9d50aGk-FUnhxosiMjFGAALnGwACYGloSA9SmDlHyYsXKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 1. Техника безопасности в кабинете информатики и ИТ и санитарно-гигиенические требования")
    video2 = "BAACAgIAAxkBAAIYVGMM6i13xNQLYLmtQy0DflUI_EnUAALlGwACYGloSMa9BfrILfWHKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. О науке Информатика"
    )
    video3 = "BAACAgIAAxkBAAIYUmMM6eRh5vfHKzwEutF53bK8o8z2AALjGwACYGloSH1OwdLAztrdKQQ"
    await call.message.answer_video(
        video3, caption="Урок 3. Информационные и цифровые технологии"
    )
    video4 = "BAACAgIAAxkBAAIYUGMM6YcdeCciXJrJmCVjUDb9OhISAALiGwACYGloSN6qcC84w6zzKQQ"
    await call.message.answer_video(
        video4, caption="Урок 4. Кодирование информации. Единицы измерения информация"
    )
    video5 = "BAACAgIAAxkBAAIYTmMM6NQVAsuQ3W7NBJWgHXfPxbmiAALhGwACYGloSA_jur_t8nUeKQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Компьютер и его структура"
    )
    video6 = "BAACAgIAAxkBAAIYTGMM6G4CJOj0mybuGNxe0OYrP2iJAALbGwACYGloSHVdQbwqa4_bKQQ"
    await call.message.answer_video(
        video6, caption="Урок 6. Аппаратные средства компьютера."
    )
    video7 = "BAACAgIAAxkBAAIYSmMM5_zbNo2McvGkY6fxS8bEu_3JAALXGwACYGloSIbCvoMzWrEzKQQ"
    await call.message.answer_video(
        video7, caption="Урок 7. Навыки работы с клавиатурой и мышью"
    )
    video8 = "BAACAgIAAxkBAAIYSGMM57Q_weHce9r9FasfBZibiO-QAALRGwACYGloSGKScGBDEYjoKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Программное обеспечение для управления с компьютером"
    )
    video9 = "BAACAgIAAxkBAAIYRmMM51CEXk5rgRa0sEUr5Uxr7yC6AALIGwACYGloSIR_eaoUheDqKQQ"
    await call.message.answer_video(
        video9, caption="Урок 9. Понятие файла и папки"
    )
    video10 = "BAACAgIAAxkBAAIYRGMM5umrFdUVft621qS7UZBL2XdmAAK6GwACYGloSFxcN4jbket9KQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. Знакомство с текстовым процессором", reply_markup=DavomVideo51ru
    )


@dp.callback_query_handler(text="Oldingi53ru")
@dp.callback_query_handler(text="davom51ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIYQmMM5njXWgubprTEwa1O6t4_7MV0AAKyGwACYGloSD_Zy553CWx1KQQ'
    await call.message.reply_video(VDars1, caption="Урок 11. Возможности форматирования документов")
    video2 = "BAACAgIAAxkBAAIYQGMM5jIzvCAssNgDf00XMKCIhaYVAAKrGwACYGloSN1OtpD_LyygKQQ"
    await call.message.answer_video(
        video2, caption="Урок 12. Создание редактирование документа в текстовом процессоре"
    )
    video3 = "BAACAgIAAxkBAAIYPmMM5eADJPGbxl3orTybhrs2dyRgAAKoGwACYGloSJg4vdCnbyyqKQQ"
    await call.message.answer_video(
        video3, caption="Урок 13. Работа с рисунками в документах"
    )
    video4 = "BAACAgIAAxkBAAIYPGMM5arapFv-az1x7vb1rJaRJ2w_AAKmGwACYGloSIA7TxVlry0mKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Работа с таблицами в документе"
    )
    video5 = "BAACAgIAAxkBAAIYOmMM5UGVfsUeaJTNKS15zN8zHJW9AAKfGwACYGloSEY9JL04RRSAKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Работа с объектами Wordart и создание титульного листа"
    )
    video6 = "BAACAgIAAxkBAAIYOGMM5Nq4B4PxeIizM_AH6Ijc9RijAAKaGwACYGloSDUiJ7tuyJrtKQQ"
    await call.message.answer_video(
        video6, caption="Урок 16. Интерфейс графического редактора и панель инструментов"
    )
    video7 = "BAACAgIAAxkBAAIYNmMM5I0597KGErZ2C9yJgOqdE937AAKXGwACYGloSDcQr7CgLgyUKQQ"
    await call.message.answer_video(
        video7, caption="Урок 17. Работа с текстом в графическом редакторе"
    )
    video8 = "BAACAgIAAxkBAAIYMmMM451lFC0GyoevAj67LZykGS6MAAKPGwACYGloSP93prUF-2wPKQQ"
    await call.message.answer_video(
        video8, caption="Урок 18. Работа со слоями"
    )
    video9 = "BAACAgIAAxkBAAIYMmMM451lFC0GyoevAj67LZykGS6MAAKPGwACYGloSP93prUF-2wPKQQ"
    await call.message.answer_video(
        video9, caption="Урок 19. Работа со слоями"
    )
    video10 = "BAACAgIAAxkBAAIYMGMM4zbfvYLI9gzSmhnf6xnWP9tUAAKGGwACYGloSMx9RK908rZiKQQ"
    await call.message.answer_video(
        video10, caption="Урок 20. Обработка фотографий и изображений в графических редакторах",
        reply_markup=DavomVideo52ru
    )


@dp.callback_query_handler(text="davom52ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIYLmMM4tlXPTqjPbhk1PK8ss11cKw8AAJ9GwACYGloSPgdXK7JYKzFKQQ'
    await call.message.reply_video(VDars1, caption="Урок 21. Работа со спрайтами")
    video2 = "BAACAgIAAxkBAAIYKmMM4j2EIzs09xLxgNFIwSTxHYmuAAJ3GwACYGloSPzdleCpOak9KQQ"
    await call.message.answer_video(
        video2, caption="Урок 22. Создание простой анимационной программы"
    )
    video3 = "BAACAgIAAxkBAAIYLGMM4pxoBum8zTBqJGS4sBs0ZbztAAJ6GwACYGloSLfE2YCxrXwaKQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Смена костюмов Спрайта"
    )
    video4 = "BAACAgIAAxkBAAIYWmMM6zGi9bWkLg93C6a9gkAJ1UuYAALsGwACYGloSGkjgF0LZHngKQQ"
    await call.message.answer_video(
        video4, caption="Урок 24. Работа со звуком и текстом"
    )
    video5 = "BAACAgIAAxkBAAIYWGMM6tbIkOUsVSnvFQYJTdmfmTO8AALqGwACYGloSEepguJ86JA5KQQ"
    await call.message.answer_video(
        video5, caption="Урок 25. Создание простых мультфильмов в scratsh среде", reply_markup=DavomVideo53ru
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi62ru")
@dp.callback_query_handler(text="6Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIY0GMPUKkvHEXRveSQP3XYgcfASogQAAIoHwAC4nt4SKttNMxIrbMfKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 1. Интерфейс текстового процессора Microsoft Word")
    video2 = "BAACAgIAAxkBAAIY5GMPU8-aAcea_8lkMEb3FI4a86uhAAJRHwAC4nt4SLpt0JGVgEJzKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. Текстовые редакторы"
    )
    video3 = "BAACAgIAAxkBAAIY_mMPWAyIXvDGsvOQbFy_lGMkcmm2AAKpHwAC4nt4SOySehrbgsp1KQQ"
    await call.message.answer_video(
        video3, caption="Урок 3. Создание и сохранение документа"
    )
    video4 = "BAACAgIAAxkBAAIY0mMPURAEBarvNjuSCuXvASjJWlzpAAIqHwAC4nt4SJS0mRnyYHiyKQQ"
    await call.message.answer_video(
        video4, caption="Урок 4. Правила ввода текста"
    )
    video5 = "BAACAgIAAxkBAAIY2mMPUk1Y52k-6l-8mMuVY1y-nhKkAAI8HwAC4nt4SE7OhPadXfPVKQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Основные параметры документа"
    )
    video6 = "BAACAgIAAxkBAAIY4mMPU6n6fiWzBYsVUfZkllKLuZPcAAJOHwAC4nt4SIBxfPDBrMczKQQ"
    await call.message.answer_video(
        video6, caption="Урок 6. Редактирование документа"
    )
    video7 = "BAACAgIAAxkBAAIZAmMPWMnWG_XTu4vMmYBsMRjB3AMlAAK9HwAC4nt4SLrDgrZXfT3UKQQ"
    await call.message.answer_video(
        video7, caption="Урок 7. Форматирование документа"
    )
    video8 = "BAACAgIAAxkBAAIZBmMPWXTZp39tRsi_cDqTg_Ran8bSAALKHwAC4nt4SHmNFSg2ckvbKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Работа с рисунками в документе"
    )
    video9 = "BAACAgIAAxkBAAIY_GMPV5o7w70t4PXOt1ACRl-N5fZBAAKeHwAC4nt4SPtTk0Mp_qOoKQQ"
    await call.message.answer_video(
        video9, caption="Урок 9. Фигуры и схемы в документе"
    )
    video10 = "BAACAgIAAxkBAAIY_GMPV5o7w70t4PXOt1ACRl-N5fZBAAKeHwAC4nt4SPtTk0Mp_qOoKQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. Фигуры и схемы в документе", reply_markup=DavomVideo61ru
    )


@dp.callback_query_handler(text="Oldingi63ru")
@dp.callback_query_handler(text="davom61ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIY7GMPVPyNCRNiygzBz5UkT7EvHhNVAAJcHwAC4nt4SLcZXsqza9XLKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 11. Программы для создания компьютерных презентации, их возможности и интерфейс")
    video2 = "BAACAgIAAxkBAAIY8mMPVf-cA_5qpyuHc1nzsvmv_h0IAAJoHwAC4nt4SPvOvi9ijkL7KQQ"
    await call.message.answer_video(
        video2, caption="Урок 12. Работа с шаблонами, инструменты форматирования и ввод текста презентации"
    )
    video3 = "BAACAgIAAxkBAAIY9GMPVmeOtsJRfq8STLkTyxhud5pFAAJ0HwAC4nt4SJojWGrHgfe9KQQ"
    await call.message.answer_video(
        video3, caption="Урок 13. Вставка картинок, фигур, таблиц и диаграмм в презентацию"
    )
    video4 = "BAACAgIAAxkBAAIY6mMPVJydSEE0kBRn--LpJNLwR_P7AAJWHwAC4nt4SAzb_O-fu8oUKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Вставка звуковых и видео файлов в презентацию"
    )
    video5 = "BAACAgIAAxkBAAIY1GMPUV6iho-tgiQSXle5XLooT5HsAAIvHwAC4nt4SKg0T_-aBmYWKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Работа с таблицами в документах"
    )
    video6 = "BAACAgIAAxkBAAIY3GMPUqytCwkuAraQc6rSC_dNn-VoAAJEHwAC4nt4SFhmwFiQdek3KQQ"
    await call.message.answer_video(
        video6, caption="Урок 16. Действия над таблицами в Word"
    )
    video7 = "BAACAgIAAxkBAAIZCGMPWcnmCu5pKg_gM0-GC9UJHdLwAALSHwAC4nt4SH9u4yBwN4t2KQQ"
    await call.message.answer_video(
        video7, caption="Урок 17. Действие над таблицами в Word. Форматирование таблиц"
    )
    video8 = "BAACAgIAAxkBAAIY2GMPUd7cWbb8DDCYDgqUzIZUgYT_AAIzHwAC4nt4SNtTS3UhYb25KQQ"
    await call.message.answer_video(
        video8, caption="Урок 18. Практическая работа. Вставка таблиц Excel"
    )
    video9 = "BAACAgIAAxkBAAIY2GMPUd7cWbb8DDCYDgqUzIZUgYT_AAIzHwAC4nt4SNtTS3UhYb25KQQ"
    await call.message.answer_video(
        video9, caption="Урок 19. Практическая работа. Вставка таблиц Excel"
    )
    video10 = "BAACAgIAAxkBAAIZCmMPWfwwl17_1o2REOvT7o6ha_9WAALYHwAC4nt4SDf2CDDVIxTgKQQ"
    await call.message.answer_video(
        video10, caption="Урок 20. Практическая работа. Использование инструмента вставка таблиц.",
        reply_markup=DavomVideo62ru
    )


@dp.callback_query_handler(text="davom62ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIY9mMPVq_-1T2e_Ru9tO-QU2qucTetAAJ7HwAC4nt4SAin2UkEin_OKQQ'
    await call.message.reply_video(VDars1, caption="Урок 21. Практическая работа. Работа с таблицами EXCEL")
    video2 = "BAACAgIAAxkBAAIY7mMPVVQWzxQPlzFOM6enbHxTMqUgAAJgHwAC4nt4SEKeNCCwF8iDKQQ"
    await call.message.answer_video(
        video2, caption="Урок 22. Практическая работа. использование таблиц Excel"
    )
    video3 = "BAACAgIAAxkBAAIY1mMPUafl64u65_XxZOse8urn_K9cAAIxHwAC4nt4SFoLP-sZjyRSKQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Практическая работа. Работа с таблицамиа"
    )
    video4 = "BAACAgIAAxkBAAIY8GMPVZvKHKELjTuGRUkpb3xxqjelAAJkHwAC4nt4SNMrfwdnrCx6KQQ"
    await call.message.answer_video(
        video4, caption="Урок 24. Объекты WordART"
    )
    video5 = "BAACAgIAAxkBAAIZAAFjD1hH3LdQGv3dwU5JvB24xXklRAACtB8AAuJ7eEi4GLBDny6VLSkE"
    await call.message.answer_video(
        video5, caption="Урок 25. Объекты WordART (Практическая работа)"
    )
    video6 = "BAACAgIAAxkBAAIY-GMPVwABGUyKtC-Myhh6u4zxqakVewACgR8AAuJ7eEjyXdXWvYQ2WykE"
    await call.message.answer_video(
        video6, caption="Урок 26. Формулы в Word"
    )
    video7 = "BAACAgIAAxkBAAIY6GMPVFZNGcjeAlGTIsOT12Sskiy8AAJVHwAC4nt4SHIu2-WiZgrvKQQ"
    await call.message.answer_video(
        video7, caption="Урок 27. Формулы в Word. Практическая работа"
    )
    video8 = "BAACAgIAAxkBAAIY-mMPV0BpM90bHZZkCDnN7ZRrQ-FEAAKRHwAC4nt4SMMWSJzl5swwKQQ"
    await call.message.answer_video(
        video8, caption="Урок 28. Формулы в Word. Повторение"
    )
    video9 = "BAACAgIAAxkBAAIY4GMPUxnYeA6JU8E9Ty5SvTE1liY5AAJLHwAC4nt4SC_HmDDdm57sKQQ"
    await call.message.answer_video(
        video9, caption="Урок 29. Распечатка документа в WORD"
    )
    video10 = "BAACAgIAAxkBAAIY5mMPVCS8EjOToMh4cRCkyZC0rv6SAAJSHwAC4nt4SBeffxzhWU3BKQQ"
    await call.message.answer_video(
        video10, caption="Урок 30. Обобщающее повторение",
        reply_markup=DavomVideo63ru
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi72ru")
@dp.callback_query_handler(text="7Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIbz2MR-uF5FufrSJSOX3x_QB2vgmOhAALYHgAC-HCRSJyGGqok99ltKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 1. Информация.")
    video2 = "BAACAgIAAxkBAAIbzWMR-nuatkR8_DI_yCgcrUAfWucXAALXHgAC-HCRSLNo6vftR12QKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. Действия с информацией."
    )
    video3 = "BAACAgIAAxkBAAIby2MR-fR-U569fVSlVCj7ketCTbywAALUHgAC-HCRSI1NpxtucDdyKQQ"
    await call.message.answer_video(
        video3, caption="Урок 3. Методы кодирования информации."
    )
    video4 = "BAACAgIAAxkBAAIbyWMR-YcMrjyNeGznIdcAAeFhQFaHIAAC0R4AAvhwkUhG5-fBXvrnwCkE"
    await call.message.answer_video(
        video4, caption="Урок 4. Системы счисления."
    )
    video5 = "BAACAgIAAxkBAAIbx2MR-OLczjq7VU56uJzuS8Vl5xwCAALLHgAC-HCRSCEmigEYisi-KQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Действия в двоичной системе счисления."
    )
    video6 = "BAACAgIAAxkBAAIbxWMR-GKTxDiGPLuArALj8wABfKjBsAACyR4AAvhwkUhxV4q7H4ExXykE"
    await call.message.answer_video(
        video6, caption="Урок 6. Перевод чисел из одной системы счисления в другую систему счисления."
    )
    video7 = "BAACAgIAAxkBAAIbw2MR9-ud5TQNovZxqCBb6uie6ti9AALDHgAC-HCRSJgruLeySwgfKQQ"
    await call.message.answer_video(
        video7, caption="Урок 7. Представление информации в компьютере(1)"
    )
    video8 = "BAACAgIAAxkBAAIb1WMR_AHWxwHhejY2CNnWRJc0fGq5AALoHgAC-HCRSCt6vWzeh2caKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Объём информации и скорость передачи."
    )
    video9 = "BAACAgIAAxkBAAIb02MR-42PHT8pHagjogtl_19YpGRCAALhHgAC-HCRSCaoVN8MdLYFKQQ"
    await call.message.answer_video(
        video9, caption="Урок 9. Кодирование графической информации."
    )
    video10 = "BAACAgIAAxkBAAIb0WMR-yOvgxcCLw3n31Yjq1wg8qSGAALZHgAC-HCRSBPNLezKLmWWKQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. Сложение в различных с.с", reply_markup=DavomVideo71ru
    )


@dp.callback_query_handler(text="Oldingi73ru")
@dp.callback_query_handler(text="davom71ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIaQ2MRp8HWHvqH_U1SIqdHVzlHgo8YAAKhHAAC-HCRSLT0qR8xL2ZeKQQ'
    await call.message.reply_video(VDars1, caption="Урок 11. Арифметические действия в различных системах счисления")
    video2 = "BAACAgIAAxkBAAIaQ2MRp8HWHvqH_U1SIqdHVzlHgo8YAAKhHAAC-HCRSLT0qR8xL2ZeKQQ"
    await call.message.answer_video(
        video2, caption="Урок 12. Арифметические действия в различных системах счисления"
    )
    video3 = "BAACAgIAAxkBAAIaQWMRp3jpby9GfTxsQyanf0XU7V7-AAKfHAAC-HCRSH8U181oDfz1KQQ"
    await call.message.answer_video(
        video3, caption="Урок 13. Практическая работа"
    )
    video4 = "BAACAgIAAxkBAAIaP2MRpyhqsa-toeTIYTzpqlYFTup8AAKeHAAC-HCRSHDYBZ2px-wuKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Практическая работа. Перевод из одной системы счисления в другую"
    )
    video5 = "BAACAgIAAxkBAAIaPWMRptgqHgOp7tw26_H64sxAlTa5AAKaHAAC-HCRSMxCJ5mjyaFzKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Практическая работа"
    )
    video6 = "BAACAgIAAxkBAAIaO2MRpqH5bmOrdGlJq42scJB2v0D5AAKZHAAC-HCRSF0jialY06qnKQQ"
    await call.message.answer_video(
        video6, caption="Урок 16. Практическая работа компьютерная графика"
    )
    video7 = "BAACAgIAAxkBAAIaOWMRpnBvQ2v1bD0ag3JVShtOBFETAAKXHAAC-HCRSMr_Qg7zf-D8KQQ"
    await call.message.answer_video(
        video7, caption="Урок 17.Кодирование информации при помощи двух знаков. Кодирование звука"
    )
    video8 = "BAACAgIAAxkBAAIaN2MRpi4bwEfGD1YhFqyN8C812yl-AAKSHAAC-HCRSMHtLO5Umm8CKQQ"
    await call.message.answer_video(
        video8, caption="Урок 18. Практическая работа. Кодирование звука и графики"
    )
    video9 = "BAACAgIAAxkBAAIaNWMRpfmyvHUb8MtDkk50RghCQFWkAAKOHAAC-HCRSH4XLTDOZWj3KQQ"
    await call.message.answer_video(
        video9, caption="Урок 19. Практическая работа"
    )
    video10 = "BAACAgIAAxkBAAIaM2MRpbBccRcTzXdeaEsAAahvB14HEAACjBwAAvhwkUjmP8kY0hu6zCkE"
    await call.message.answer_video(
        video10, caption="Урок 20. Информационные технологии", reply_markup=DavomVideo72ru
    )


@dp.callback_query_handler(text="davom72ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIaMWMRpXCUlqvME3pl1bXWaqVSLfNkAAKLHAAC-HCRSJwsrvATiPPDKQQ'
    await call.message.reply_video(VDars1, caption="Урок 21. Информационные технологии. Компьютерные сети.")
    video2 = "BAACAgIAAxkBAAIaL2MRpTGZeRbrZTQY0wQ97sETaxfFAAKKHAAC-HCRSNXviBrWRMdDKQQ"
    await call.message.answer_video(
        video2, caption="Урок 22. Проблемы информационного мира и интернет"
    )
    video3 = "BAACAgIAAxkBAAIaLWMRpNFnXXrO8hq3Jo_1rkOC7amtAAKJHAAC-HCRSDMRHBDJvU0yKQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Программы, обеспечивающие работу"
    )
    video4 = "BAACAgIAAxkBAAIaK2MRpH44MXrqHIW2dTPjfGc35n_gAAKIHAAC-HCRSPjxXOB5mVjGKQQ"
    await call.message.answer_video(
        video4, caption="Урок 24. Поиск информации в интернете"
    )
    video5 = "BAACAgIAAxkBAAIaKWMRpDildcDFm9vMQAxIrZ6hAfz-AAKGHAAC-HCRSEb9iOsbDlrwKQQ"
    await call.message.answer_video(
        video5, caption="Урок 25. Поиск информации в интернете. Практическая работа"
    )
    video6 = "BAACAgIAAxkBAAIaJ2MRo7mYlZsXYfxjTa55bppGzi2DAAJ_HAAC-HCRSOI2Z7CnQU3IKQQ"
    await call.message.answer_video(
        video6, caption="Урок 26. Электронная почта"
    )
    video7 = "BAACAgIAAxkBAAIaJWMRo1gST3CTMunXEW89ZvG4JK8lAAJ6HAAC-HCRSAYtSpy5TnGYKQQ"
    await call.message.answer_video(
        video7, caption="Урок 27. Электронная почта (Практическая работа)"
    )
    video8 = "BAACAgIAAxkBAAIaYWMRrcWfDONjaRBCR-S2mk1T95ldAALGHAAC-HCRSKgnAAGG2ZJ6jykE"
    await call.message.answer_video(
        video8, caption="Урок 28. Об антивирусах и защите информации"
    )
    video9 = "BAACAgIAAxkBAAIaX2MRrX8j2xYgbHUqdfNiaZ3kajsCAALEHAAC-HCRSJMmTc_SzbLXKQQ"
    await call.message.answer_video(
        video9, caption="Урок 29. Об антивирусах и защите информации (2)"
    )
    video10 = "BAACAgIAAxkBAAIaXWMRrT-z8pa7X9YJA0m3zAgiUY6sAALDHAAC-HCRSM335PZ0zxFkKQQ"
    await call.message.answer_video(
        video10, caption="Урок 30. Обобщающее повторение"
    )
    video11 = "BAACAgIAAxkBAAIaW2MRrPZjf75AkMnXqqTTTatZoo_8AALCHAAC-HCRSFzPLEZRhtprKQQ"
    await call.message.answer_video(
        video11, caption="Урок 31. Контрольная работа",
        reply_markup=DavomVideo73ru
    )


###############################################################################################################


@dp.callback_query_handler(text="Oldingi82ru")
@dp.callback_query_handler(text="8Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIcTGMTWGC8FbvxFoyZ39AqjsjSC0PXAAJPHAACr7aYSHyPP17RZO94KQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 1. Социальный медиа маркетинг")
    video2 = "BAACAgIAAxkBAAIcSmMTWC_1R7onOcUQ2osjIq9VnIIdAAJNHAACr7aYSJyQHj-f0GTlKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. Знакомство с платформами SMM. Facebook"
    )
    video3 = "BAACAgIAAxkBAAIcSGMTV8tAM0lydVx1Zy9EFjBu32n3AAJLHAACr7aYSLuh7dt9205TKQQ"
    await call.message.answer_video(
        video3, caption="Урок 3. Знакомство с платформами SMM. YouTube"
    )
    video4 = "BAACAgIAAxkBAAIcRmMTV2xzQkNzB0bFxNz23syUbLDhAAJEHAACr7aYSDnlyvgEQ0BUKQQ"
    await call.message.answer_video(
        video4, caption="Урок 4. Знакомство с платформами SMM. Telegram"
    )
    video5 = "BAACAgIAAxkBAAIcRGMTVwjVub0_f5ekCS-4lj2NcxPdAAJDHAACr7aYSGo9LSxN17EBKQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Продвижение SMM в сети Интернет"
    )
    video6 = "BAACAgIAAxkBAAIcQmMTVq2e3gXpCE7BWxH67he53eyGAAJBHAACr7aYSAhQJkQ0TfaAKQQ"
    await call.message.answer_video(
        video6, caption="Урок 6. Знакомство с платформами SMM. Instagram"
    )
    video7 = "BAACAgIAAxkBAAIcQGMTVmBkfKHwTRxkForQ-SawBVdzAAI8HAACr7aYSLljBzAqpW5EKQQ"
    await call.message.answer_video(
        video7,
        caption="Урок 7. Управление исследовательскими проектами на основе SMM. Открытие канала на сайте YouTube"
    )
    video8 = "BAACAgIAAxkBAAIcPmMTVhqSICPGrGnZJZE1Zdsn2RbrAAI7HAACr7aYSPaq5vrgOwMeKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Исследовательские проекты на основе SMM. Открытие страницы в сети Facebook"
    )
    video9 = "BAACAgIAAxkBAAIcPGMTVdDZi4hXscRkRaEK1oWuFHcWAAI6HAACr7aYSGNYXBZbcjH5KQQ"
    await call.message.answer_video(
        video9, caption="Урок 9. Управление исследовательскими проектами на основе SMM. Открытие канала в сети Telegram"
    )
    video10 = "BAACAgIAAxkBAAIcOmMTVXT2pNpTLEUj_KlMePiZ-pGMAAI5HAACr7aYSPEteGGLsJuJKQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. СМS (Content management systems). Системы управления контентом",
        reply_markup=DavomVideo81ru
    )


@dp.callback_query_handler(text="Oldingi83ru")
@dp.callback_query_handler(text="davom81ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIcOGMTVSe_5FWdXkF1tlc_UWdbm50RAAI1HAACr7aYSCJ021GaO_1nKQQ'
    await call.message.reply_video(VDars1, caption="Урок 11. Знакомство с платформами CMS")
    video2 = "BAACAgIAAxkBAAIcNmMTVN5z22p75FxHd5Trlwu4VV6pAAI0HAACr7aYSE5L23RPSAVmKQQ"
    await call.message.answer_video(
        video2, caption="Урок 12. Практическая Работа"
    )
    video3 = "BAACAgIAAxkBAAIcNGMTVH7ksV9EQ1uNjsGfq8d2ttzJAAIwHAACr7aYSPwLBjMad8jnKQQ"
    await call.message.answer_video(
        video3, caption="Урок 13. Создание целевых веб-сайтов в CMS"
    )
    video4 = "BAACAgIAAxkBAAIcMmMTVEtAmdNydhI4kbk7F4YZVgt0AAIrHAACr7aYSMAjbZue4sCTKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Работа с дизайном веб-сайта"
    )
    video5 = "BAACAgIAAxkBAAIcMGMTVB0NWe9BPgLOWOszP5MdA8hWAAIoHAACr7aYSFSGqU_XgEZIKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Практическая работа. Работа дизайном веб-сайта в Wordpress"
    )
    video6 = "BAACAgIAAxkBAAIcLmMTU_ri_ZsTuiy1iSyku0ObQNjkAAIlHAACr7aYSCmeFFUBTpHAKQQ"
    await call.message.answer_video(
        video6, caption="Урок 16. Создание целевого веб-сайта в Wordpress"
    )
    video7 = "BAACAgIAAxkBAAIcLGMTU9FA8aEz_M6MyVVc4H0TgafCAAIiHAACr7aYSOiuWWDFe0ziKQQ"
    await call.message.answer_video(
        video7, caption="Урок 17. Работа с содержанием Веб-сайта"
    )
    video8 = "BAACAgIAAxkBAAIcKmMTU6T8yHCazeTs9fZ0Fw7tod9_AAIfHAACr7aYSKgqh1hFjpK2KQQ"
    await call.message.answer_video(
        video8, caption="Урок 18. Практическая работа. Работа с дизайном веб-сайта в Wordpress"
    )
    video9 = "BAACAgIAAxkBAAIcKGMTU3KglsqTGy1fxpZqCGm5kTVJAAIdHAACr7aYSMrg2knU-injKQQ"
    await call.message.answer_video(
        video9, caption="Урок 19.  Типы и функции платформ LMS"
    )
    video10 = "BAACAgIAAxkBAAIcJmMTUy4CAAGrV_coU7UY5qJN5qoJWwACHBwAAq-2mEiBZDzX8IJ4YykE"
    await call.message.answer_video(
        video10, caption="Урок 20. Виды и функции платформ LMS", reply_markup=DavomVideo82ru
    )


@dp.callback_query_handler(text="davom82ru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIcJGMTUv99x6nL_p5qTV_X6r-0eTEWAAIbHAACr7aYSLV7kevkyPeDKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 21. Практическое занятие. Знакомство с платформами Learndash, Schoology, Ispring learn, Google Clasroom, Moodle")
    video2 = "BAACAgIAAxkBAAIcImMTUrGdaIyn3N7m8c9OE1TxvAm8AAIZHAACr7aYSJde4SvByeKiKQQ"
    await call.message.answer_video(
        video2, caption="Урок 22. Дистанционное обучение на основе LMS платформа MOODLE"
    )
    video3 = "BAACAgIAAxkBAAIchWMTbaXGobtfRzIhueuy0gMkhUSZAALPHQACr7aYSFcKdQEZsTyEKQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Обучение на платформе MOODLE"
    )
    video4 = "BAACAgIAAxkBAAIcHmMTUjuABDjIhEXd9ucqVEblPXLXAAIWHAACr7aYSAZtjQqpo9ZDKQQ"
    await call.message.answer_video(
        video4, caption="Урок 24. Дистанционное обучение на основе ЛМС платформа GOOGLE CLASSROOM"
    )
    video5 = "BAACAgIAAxkBAAIcHGMTUe6OkF3k4_n5uJt4TzuTlD_OAAIUHAACr7aYSMMFZCHyiCdzKQQ"
    await call.message.answer_video(
        video5, caption="Урок 25. MOOC (Massive open online courses- Массовые открытые онлайн- курсы)"
    )
    video6 = "BAACAgIAAxkBAAIcGmMTUZsFEgkfNMWLKhU1uv4s32RoAAITHAACr7aYSOjuKsZY1BpAKQQ"
    await call.message.answer_video(
        video6, caption="Урок 26. Виды и задачи платформ МООС"
    )
    video7 = "BAACAgIAAxkBAAIcGGMTUVTJL5p7SdNbpmeavAr_fUmbAAISHAACr7aYSHQd4uVOQhJpKQQ"
    await call.message.answer_video(
        video7,
        caption="Урок 27. Практическая работа. Знакомство с платформами Coursera, Khan Academy, Лекториум, Edx, Udemy, Udacity"
    )
    video8 = "BAACAgIAAxkBAAIcFmMTUSZerU3EC6v47xfABFVupReSAAIOHAACr7aYSA5dYlTUy2ITKQQ"
    await call.message.answer_video(
        video8, caption="Урок 28. Понятие о WEB-FREELANCE"
    )
    video9 = "BAACAgIAAxkBAAIcTmMTWKqqtTmhs2m1mNn-_L2rj-EWAAJRHAACr7aYSN84WZPtca_iKQQ"
    await call.message.answer_video(
        video9, caption="Урок 29. Практическая занятие. Работа с фриланс сайтами",
        reply_markup=DavomVideo83ru
    )


#######################################################################################################################################


@dp.callback_query_handler(text="Oldingi92ru")
@dp.callback_query_handler(text="9Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIc9mMTq6FqSivFQXuPDHmBTTwusHIWAAIjHwACr7aYSAqNnGp8b1RaKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 1. О системах счисления. Выполнения действий в двоичной системе счисления.")
    video2 = "BAACAgIAAxkBAAIc9GMTqyG0TfWpStuF0hm1L9S5KbnDAAIgHwACr7aYSBlCnVeSz9jSKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. Выполнение действий 8-ричной и 16-ричной системах счисления"
    )
    video3 = "BAACAgIAAxkBAAIc8mMTqnp81YTRz2anTaN--VmlUX1IAAIeHwACr7aYSHXMmb_XQj3NKQQ"
    await call.message.answer_video(
        video3, caption="Урок 3. Перевод чисел из одной системы счисления в другой"
    )
    video4 = "BAACAgIAAxkBAAIc8GMTqdIFPyZpZavJS6M5uE3n4tF2AAIaHwACr7aYSNlSsBD20AN5KQQ"
    await call.message.answer_video(
        video4, caption="Урок 4. Основы логики. Логические операции и выражения."
    )
    video5 = "BAACAgIAAxkBAAIc7mMTqWCuQsbZMFPzpR_HOfhLNKOJAAIYHwACr7aYSP44MLKGstybKQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Этапы решений задач на компьютере"
    )
    video6 = "BAACAgIAAxkBAAIc7GMTqLvRpUlXOrjTz3_iQz6w1lAOAAITHwACr7aYSL-AkP-gnC8_KQQ"
    await call.message.answer_video(
        video6, caption="Урок 6. Модель. Её типы и виды"
    )
    video7 = "BAACAgIAAxkBAAIc6mMTqBif9fJbQoeMZPDG2Uu6DX2pAAIRHwACr7aYSI4TVglQGETDKQQ"
    await call.message.answer_video(
        video7, caption="Урок 7. Понятие алгоритма и его свойства"
    )
    video8 = "BAACAgIAAxkBAAIc6GMTp8Mf-nBEDsv1Fi6ezMuDu4XTAAIPHwACr7aYSJExC0PQNL0jKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Понятие алгоритма и его свойства (2 урок)"
    )
    video9 = "BAACAgIAAxkBAAIc5mMTp1cxVVU3lBZ7K-v_tFWqgCcuAAIMHwACr7aYSCg7HEL3EktdKQQ"
    await call.message.answer_video(
        video9, caption="Урок 9. Способы представления алгоритмов. Блок-схемы."
    )
    video10 = "BAACAgIAAxkBAAIc5GMTpwUGu6LP4fLb_25hIsgNN_PTAAIHHwACr7aYSAYoC3d4mEqhKQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. Модель, её типы и виды. Практическая работа.",
        reply_markup=DavomVideo91ru
    )


@dp.callback_query_handler(text="Oldingi93ru")
@dp.callback_query_handler(text="davom91ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIc4mMTpq9HvYcbhewy7oxlIbGcTx1ZAAIEHwACr7aYSI_981_Ziy0uKQQ'
    await call.message.reply_video(VDars1, caption="Урок 11. Линейные алгоритмы")
    video2 = "BAACAgIAAxkBAAIc4GMTpkUIYw-UxrbyME4AAcW6LRcPqQACAR8AAq-2mEjDSnuh3d9olSkE"
    await call.message.answer_video(
        video2, caption="Урок 12. Алгоритмы со структурой ветвления"
    )
    video3 = "BAACAgIAAxkBAAIc3mMTpg_DlB7jaPQPSBRl8Coowb-QAAMfAAKvtphIq5A0BM4hpMcpBA"
    await call.message.answer_video(
        video3, caption="Урок 13. Алгоритмы со структурой ветвления. Практическая работа"
    )
    video4 = "BAACAgIAAxkBAAIc3GMTpeLH0oW24_oP-Hq47JkD8UdTAAL_HgACr7aYSF98Yr7RKB9dKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Повторяющиеся алгоритмы"
    )
    video5 = "BAACAgIAAxkBAAIc2mMTpaYftLrHq76aFlM6WvNUipeXAAL9HgACr7aYSGCjUvLKLpWSKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Повторяющиеся (циклические) алгоритмы. Практическая работа."
    )
    video6 = "BAACAgIAAxkBAAIc2GMTpVRUyWh5LYVwzBK9M1_LdXrUAAL6HgACr7aYSBFOsnp4HuZKKQQ"
    await call.message.answer_video(
        video6, caption="Урок 16. Смешанные (комбинированные) алгоритмы. Практическое занятие"
    )
    video7 = "BAACAgIAAxkBAAIc1mMTpMUB50h_Yy2Jqzj8eMitYsZwAAL2HgACr7aYSIcWOYDhQfFCKQQ"
    await call.message.answer_video(
        video7, caption="Урок 17. Начало работы в среде программирования Python"
    )
    video8 = "BAACAgIAAxkBAAIdM2MUT5b7IAebL1K5jo_E00_xUkxhAAJ1GQACuC6gSOcU38DJyWFVKQQ"
    await call.message.answer_video(
        video8,
        caption="Урок 18. Типы данных программирования на Python"
    )
    video9 = "BAACAgIAAxkBAAIc0mMTo9cF3WCWErkTtwTM4X2N_oIYAALzHgACr7aYSMkgj364NNj0KQQ"
    await call.message.answer_video(
        video9, caption="Урок 19. Операции на языке программирования Python"
    )
    video10 = "BAACAgIAAxkBAAIc0GMTo5zCk-3x0I51_ZECeRRxNlZsAALyHgACr7aYSGhpyzuhx59mKQQ"
    await call.message.answer_video(
        video10, caption="Урок 20. Основные строк в языке программирование Python",
        reply_markup=DavomVideo92ru
    )


@dp.callback_query_handler(text="Oldingi94ru")
@dp.callback_query_handler(text="davom92ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIczmMToxe2eW-D7y5TkMHmcaIC3kTyAALwHgACr7aYSB7PHPg7sFr-KQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 21. Описание срок в языке программирования Python. Практическая работа")
    video2 = "BAACAgIAAxkBAAIczGMTopok0mtnOkCNKYuszSG8VlKFAALvHgACr7aYSOiJRNVaiMxSKQQ"
    await call.message.answer_video(
        video2, caption="Урок 22. Операторы и выражения. Практические работы"
    )
    video3 = "BAACAgIAAxkBAAIdMGMTtAuVSpjnj_GlzmeWzGQXa_yIAAJdHwACr7aYSLnuZzbFtln2KQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Операторы и выражения"
    )
    video4 = "BAACAgIAAxkBAAIdLmMTs9asOSQKFFNGhpmDkCVienSNAAJcHwACr7aYSKwE7IcEmWzjKQQ"
    await call.message.answer_video(
        video4, caption="Урок 24. Решение простых задач в Python. Практическая работа"
    )
    video5 = "BAACAgIAAxkBAAIdLGMTs5w71WkhtTPpNWo2fg_m9Yx-AAJbHwACr7aYSHODujjhMjrkKQQ"
    await call.message.answer_video(
        video5, caption="Урок 25. Программирование разветвляющихся алгоритмов. Оператор ELIF"
    )
    video6 = "BAACAgIAAxkBAAIdKmMTs1ewf9zfiAozdxH_GqKsJQKJAAJZHwACr7aYSKuRfx4bLCHqKQQ"
    await call.message.answer_video(
        video6, caption="Урок 26. Программирование логических задач в Python"
    )
    video7 = "BAACAgIAAxkBAAIdKGMTsxBGpFgFZnoV873VfWRpGCUWAAJWHwACr7aYSOOHxf4wSXVZKQQ"
    await call.message.answer_video(
        video7, caption="Урок 27. Программирование логических задач в Python. Практическая работа"
    )
    video8 = "BAACAgIAAxkBAAIdJmMTspUt92BstLqX375Gz3hP3ce7AAJUHwACr7aYSK76qklgl-UdKQQ"
    await call.message.answer_video(
        video8,
        caption="Урок 28. Программирование разветвляющихся алгоритмов. Оператор if...else"
    )
    video9 = "BAACAgIAAxkBAAIdJGMTslr6gBe1C5oQwYJ-8hFBT8-HAAJTHwACr7aYSLVR3chgNefUKQQ"
    await call.message.answer_video(
        video9, caption="Урок 29. Программирование разветвляющихся алгоритмов. Оператор ELIF."
    )
    video10 = "BAACAgIAAxkBAAIdImMTshg94Zy3g-fQRxsanAiXfeq3AAJSHwACr7aYSFy_r4mMe7deKQQ"
    await call.message.answer_video(
        video10, caption="Урок 30. Программирование повторяющихся алгоритмов оператор For",
        reply_markup=DavomVideo93ru
    )


@dp.callback_query_handler(text="Oldingi95ru")
@dp.callback_query_handler(text="davom93ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIdIGMTsekYQxr0iwHJVhZUhC-Sqf7yAAJQHwACr7aYSCk7MH6AKXJOKQQ'
    await call.message.reply_video(VDars1, caption="Урок 31. Программирование повторяющихся алгоритмов. Оператор FOR.")
    video2 = "BAACAgIAAxkBAAIdHGMTsWNy6G-u5HElVyfAFGwdFGIKAAJOHwACr7aYSHVF73iX6_otKQQ"
    await call.message.answer_video(
        video2,
        caption="Урок 32. Программирование повторяющихся алгоритмов. Вложенные циклы"
    )
    video3 = "BAACAgIAAxkBAAIdHGMTsWNy6G-u5HElVyfAFGwdFGIKAAJOHwACr7aYSHVF73iX6_otKQQ"
    await call.message.answer_video(
        video3, caption="Урок 33. Программирование повторяющихся алгоритмов. Оператор While"
    )
    video4 = "BAACAgIAAxkBAAIdGmMTsRMVVuaxHSfzaBG4HdAN0NKMAAJMHwACr7aYSD3CtevCUptCKQQ"
    await call.message.answer_video(
        video4, caption="Урок 34. Управление циклами. Операторы. Continue"
    )
    video5 = "BAACAgIAAxkBAAIdGGMTsNTIfFFfNOzqb_pU6Wj_RqoLAAJLHwACr7aYSFXanvt8o6MtKQQ"
    await call.message.answer_video(
        video5, caption="Урок 35. Программирование повторяющихся алгоритмов. Оператор While"
    )
    video6 = "BAACAgIAAxkBAAIdFmMTsGZ-6CK5YVmj_rJtPLJ0WGW_AAJGHwACr7aYSGAGO5NJzwgcKQQ"
    await call.message.answer_video(
        video6, caption="Урок 36. Подпрограммы: Функции и процедуры. Практическая работа"
    )
    video7 = "BAACAgIAAxkBAAIdFmMTsGZ-6CK5YVmj_rJtPLJ0WGW_AAJGHwACr7aYSGAGO5NJzwgcKQQ"
    await call.message.answer_video(
        video7,
        caption="Урок 37. Функции и процедуры"
    )
    video8 = "BAACAgIAAxkBAAIdEGMTr5tyCUPk0GCSxsppvvKlMtBAAAI_HwACr7aYSJnlJBE9LUGeKQQ"
    await call.message.answer_video(
        video8, caption="Урок 38. Функции и переменные. Практическая работа"
    )
    video9 = "BAACAgIAAxkBAAIdEGMTr5tyCUPk0GCSxsppvvKlMtBAAAI_HwACr7aYSJnlJBE9LUGeKQQ"
    await call.message.answer_video(
        video9, caption="Урок 39. Функции и переменные"
    )
    video10 = "BAACAgIAAxkBAAIdDmMTrz2la7vvPb2RvD25QTkFCTksAAI-HwACr7aYSDpJVdZZctS_KQQ"
    await call.message.answer_video(
        video10, caption="Урок 40. Функции и переменные", reply_markup=DavomVideo94ru
    )


@dp.callback_query_handler(text="davom94ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIdDGMTrv9p4qj6FcaW6Iw9xWWnSRMhAAI9HwACr7aYSJouZcTm4y06KQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 41. Библиотека языка программирования. Python")
    video2 = "BAACAgIAAxkBAAIdCGMTrofI7sfhjmZido_gRLq_kXGiAAI6HwACr7aYSF8ZobOmn5OsKQQ"
    await call.message.answer_video(
        video2, caption="Урок 42. Работа с графическим интерфейсом пользователя в Python"
    )
    video3 = "BAACAgIAAxkBAAIdCGMTrofI7sfhjmZido_gRLq_kXGiAAI6HwACr7aYSF8ZobOmn5OsKQQ"
    await call.message.answer_video(
        video3, caption="Урок 43. Работа с графическим интерфейсом пользователя в Python"
    )
    video4 = "BAACAgIAAxkBAAIdBmMTrhNMJHHmBZv-IIVo-EMsFAABqwACOB8AAq-2mEjUG0HchkUQ4SkE"
    await call.message.answer_video(
        video4, caption="Урок 44. Решение простых задач в Python"
    )
    video5 = "BAACAgIAAxkBAAIdAmMTrZLQ8SjbpDewAff1iycFmrYkAAIwHwACr7aYSEpDELNIPacoKQQ"
    await call.message.answer_video(
        video5, caption="Урок 45. Работа с графическим интерфейсом пользователя в Python. Практическая работа"
    )
    video6 = "BAACAgIAAxkBAAIdAmMTrZLQ8SjbpDewAff1iycFmrYkAAIwHwACr7aYSEpDELNIPacoKQQ"
    await call.message.answer_video(
        video6, caption="Урок 46. Работа с графическим интерфейсом пользователя в Python. Практическая работа"
    )
    video7 = "BAACAgIAAxkBAAIdAAFjE61J0vTIaulWSwbwwRoHWxcxBQACLR8AAq-2mEhrkcEuHGDHNSkE"
    await call.message.answer_video(
        video7, caption="Урок 47. Повторение"
    )
    video8 = "BAACAgIAAxkBAAIc_mMTrRPyLwzpyAt54Y9S1J42fYzmAAIrHwACr7aYSJp6vo9mBMI9KQQ"
    await call.message.answer_video(
        video8, caption="Урок 48. Работа с графическим интерфейсом пользователя в Python (повторение)"
    )
    video9 = "BAACAgIAAxkBAAIc_GMTrKAAATLCLAXL7P1EyqSa0JuVqgACJx8AAq-2mEg7NWK6apVmuCkE"
    await call.message.answer_video(
        video9, caption="Урок 49. Массивы в PYTHON"
    )
    video10 = "BAACAgIAAxkBAAIc-mMTrE_uF9mEo5RGROlAvyg_Q9BgAAImHwACr7aYSB8bnrSIEl8RKQQ"
    await call.message.answer_video(
        video10, caption="Урок 50. Массивы в Python. Практическая работа", reply_markup=DavomVideo95ru
    )
    video11 = "BAACAgIAAxkBAAIc-GMTrBWGTaS5KBsc01FvBrB4DsrbAAIkHwACr7aYSGq4JxR3jkArKQQ"
    await call.message.answer_video(
        video11, caption="Урок 51. Массивы в Python. Решение задач", reply_markup=DavomVideo95ru
    )


#######################################################################################################################################

@dp.callback_query_handler(text="Oldingi102ru")
@dp.callback_query_handler(text="10Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIel2MUa0mYB7G4nlejmMTGkW0vEUCBAAL7GgACCg6pSEvzLga5PB88KQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 1. Вычисление простых выражений")
    video2 = "BAACAgIAAxkBAAIelWMUau7T0jH2Hdi8GD0b4Z51-q8CAAL3GgACCg6pSHXjcyzkqWNYKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. Ссылки к ячейкам относительная, абсолютная, смешанная"
    )
    video3 = "BAACAgIAAxkBAAIek2MUanGuL2FDcIlW-8gHK6REOtHVAAL2GgACCg6pSDLhNFtNaiWAKQQ"
    await call.message.answer_video(
        video3, caption="Урок 3.Преимущества копирования при выполнении действий, используя ссылки"
    )
    video4 = "BAACAgIAAxkBAAIekWMUafBojRRjDWYG-YRXQG6YXXDUAALxGgACCg6pSOe4TiDceOc2KQQ"
    await call.message.answer_video(
        video4, caption="Урок 4. Графики простых и сложных функций"
    )
    video5 = "BAACAgIAAxkBAAIej2MUaVw6yuA-45h8mydPR9Idpfz9AALvGgACCg6pSDcQTzBjmh6XKQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Ссылки на другие листы и книги"
    )
    video6 = "BAACAgIAAxkBAAIejWMUaQU9O8_pw3EZ0XH6o8oNMVmbAALqGgACCg6pSE2eRJRMmpFJKQQ"
    await call.message.answer_video(
        video6, caption="Урок 6. Библиотека функций MS EXCEL"
    )
    video7 = "BAACAgIAAxkBAAIei2MUaLYjZE1BW2V_4Rebb01gXwABOgAC6RoAAgoOqUj1zgfEuMFjfykE"
    await call.message.answer_video(
        video7, caption="Урок 7. Окно аргумента функции. Использование строки формул"
    )
    video8 = "BAACAgIAAxkBAAIeiWMUaFqeP0dr4X86wYEWr40iQZC6AALlGgACCg6pSEJL_ihPoYZZKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Логические функции. Практическое занятие"
    )
    video9 = "BAACAgIAAxkBAAIeh2MUZ7dPRiNnMpbJ-t1E9MZRp3Q5AALjGgACCg6pSFJf5TBbuAecKQQ"
    await call.message.answer_video(
        video9, caption="Урок 9. Основные элементы MS Access 2010 и свойства полей."
    )
    video10 = "BAACAgIAAxkBAAIehWMUZ0L-VRcyQdw-TV8MtkpDjqhYAALgGgACCg6pSA7UZzNkpm2tKQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. Математические функции. Функции для вычисления произведения",
        reply_markup=DavomVideo101ru
    )


@dp.callback_query_handler(text="Oldingi103ru")
@dp.callback_query_handler(text="davom101ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIeg2MUZwABK3rX0_utrEX9WyZN7JY4AAPfGgACCg6pSAIS51iQz68ZKQQ'
    await call.message.reply_video(VDars1, caption="Урок 11. Статистические функции")
    video2 = "BAACAgIAAxkBAAIegWMUZpfhWuyvihgomyFJ_jDCOj3lAALeGgACCg6pSMBBHjDqO0rZKQQ"
    await call.message.answer_video(
        video2, caption="Урок 12. Статистические функции. Решение задач"
    )
    video3 = "BAACAgIAAxkBAAIef2MUZjpiVJUEC91RzPxyaCXSngWjAALcGgACCg6pSHlTFeWRJJWHKQQ"
    await call.message.answer_video(
        video3, caption="Урок 13. Понятие базы данных"
    )
    video4 = "BAACAgIAAxkBAAIefWMUZeRERZkL1kYmF1hKYCL-PFE5AALbGgACCg6pSKQ6jYz-udQMKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Системы управления базами данных"
    )
    video5 = "BAACAgIAAxkBAAIee2MUZZT-Ph_An29DuZwvRjXKvoKuAALaGgACCg6pSAIzkf2Y_HETKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Практическое занятие"
    )
    video6 = "BAACAgIAAxkBAAIeeWMUZV2KOsNDuxsXziVmHwR88rnfAALZGgACCg6pSIY02jbsS9TuKQQ"
    await call.message.answer_video(
        video6, caption="Урок 16. Практическое занятие"
    )
    video7 = "BAACAgIAAxkBAAIed2MUZRBmQ3ACqT0TxZdfQipN00z-AALYGgACCg6pSJnN0Zh2ZzWuKQQ"
    await call.message.answer_video(
        video7, caption="Урок 17. Создание базы данных в MS Access 2010"
    )
    video8 = "BAACAgIAAxkBAAIedWMUZNtDYjRjwDnvhklM3hviXbUxAALWGgACCg6pSNwFRmOLYGlFKQQ"
    await call.message.answer_video(
        video8,
        caption="Урок 18. Практическое занятие"
    )
    video9 = "BAACAgIAAxkBAAIec2MUZIfb6ovXYZK-9J41d9k8PgX3AALVGgACCg6pSI3_PpmMM6VGKQQ"
    await call.message.answer_video(
        video9, caption="Урок 19. Приложение и окно приложения Delphi"
    )
    video10 = "BAACAgIAAxkBAAIecWMUZD2GOTGA-ElvLuP2JMepI-gyAALUGgACCg6pSPauKPrlMHffKQQ"
    await call.message.answer_video(
        video10, caption="Урок 20. Современные методы создания приложений; современные приложения; этапы развития программирования; современные среды программирования.",
        reply_markup=DavomVideo102ru
    )


@dp.callback_query_handler(text="Oldingi104ru")
@dp.callback_query_handler(text="davom102ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIeb2MUY-uom6uKa3WU1DIyn7NTp-2CAALSGgACCg6pSHdWfs1OMbqOKQQ'
    await call.message.reply_video(VDars1, caption="Урок 21. Среда программирования Delphi")
    video2 = "BAACAgIAAxkBAAIebWMUY6L3Mk809yFln_EQPS0104NlAALQGgACCg6pSG_mw5Bw4BbrKQQ"
    await call.message.answer_video(
        video2, caption="Урок 22. Кнопка управления Delphi"
    )
    video3 = "BAACAgIAAxkBAAIea2MUY170Cvx-Okqziay3ix1n5_rmAALNGgACCg6pSPkBnEdhO0kgKQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Кнопки управления Delphi. Практическая работа"
    )
    video4 = "BAACAgIAAxkBAAIeaWMUYxjgA1gaPsdc5QVnRJPnqwfnAALLGgACCg6pSFsmLqkIAW8qKQQ"
    await call.message.answer_video(
        video4, caption="Урок 24. Окно Showmessage"
    )
    video5 = "BAACAgIAAxkBAAIeZ2MUYtOqoayqQ7pHcLm-DDEltCTzAALIGgACCg6pSAnc1i7XhjOaKQQ"
    await call.message.answer_video(
        video5, caption="Урок 25. Повторение"
    )
    video6 = "BAACAgIAAxkBAAIeZWMUYopoxabkH68czzp-kLLGzWKqAALHGgACCg6pSNK56bMY9guOKQQ"
    await call.message.answer_video(
        video6, caption="Урок 26. Размещение данных в окне приложения Delphi."
    )
    video7 = "BAACAgIAAxkBAAIeY2MUYky9R_mKwG7Y6K3eG3TWKYPTAALGGgACCg6pSDK50RcZBpK0KQQ"
    await call.message.answer_video(
        video7, caption="Урок 27. Доступность и видимость объектов управлениея"
    )
    video8 = "BAACAgIAAxkBAAIeYWMUYhCQ9Y0ToKm71U_2rNdJvnIrAALEGgACCg6pSEcM69puBJMbKQQ"
    await call.message.answer_video(
        video8,
        caption="Урок 28. Ввод данных в приложение"
    )
    video9 = "BAACAgIAAxkBAAIemWMUa3Hq5cfBDm_7408NTrfBnvPOAAL8GgACCg6pSGsXAAGO6FWGgykE"
    await call.message.answer_video(
        video9, caption="Урок 29. Изменение типа информации"
    )
    video10 = "BAACAgIAAxkBAAIeX2MUYcEf3cNkmt0Eh3OS1Dd7dmd-AALDGgACCg6pSOnU3zTGwv6YKQQ"
    await call.message.answer_video(
        video10, caption="Урок 30. Применение флажков в приложении",
        reply_markup=DavomVideo103ru
    )


@dp.callback_query_handler(text="Oldingi105ru")
@dp.callback_query_handler(text="davom103ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIeXWMUYZqug1jN0elELH9uENNXU9ZqAALCGgACCg6pSLTvSyCAxGcRKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 31. Использование групп радиокнопок в приложении")
    video2 = "BAACAgIAAxkBAAIeuWMUcA9ZAYGxTgkaZvFjaaA1_0cmAAIpGwACCg6pSAu5FTEx11zmKQQ"
    await call.message.answer_video(
        video2,
        caption="Урок 32. Приложение и окно приложения Delphi"
    )
    video3 = "BAACAgIAAxkBAAIet2MUb8bjpPjvSHLEuUC1BMTx01RNAAInGwACCg6pSE0oeY_cUIcLKQQ"
    await call.message.answer_video(
        video3, caption="Урок 33. Ввод данных в приложение"
    )
    video4 = "BAACAgIAAxkBAAIetWMUb4NkWDKvinEeonmVXZoRRwluAAIjGwACCg6pSK1r50BX3axsKQQ"
    await call.message.answer_video(
        video4, caption="Урок 34. Объекты Listbox и Combobox"
    )
    video5 = "BAACAgIAAxkBAAIes2MUbyeKkrXGBTh-0nVYlq5v3S6FAAIeGwACCg6pSHJagITkR0v4KQQ"
    await call.message.answer_video(
        video5, caption="Урок 35. Управляющий объект Memo: объект Memo и его возможности, основные свойства объекта Memo, применение простых чисел"
    )
    video6 = "BAACAgIAAxkBAAIesWMUbu4Nt7f9JWE2rQFXX1xsc3VJAAIbGwACCg6pSLSolZ4WEkhpKQQ"
    await call.message.answer_video(
        video6, caption="Урок 36. Управляющий объект Memo: объект Memo и его возможности, основные свойства объекта Memo, применение простых чисел. Практическая работа"
    )
    video7 = "BAACAgIAAxkBAAIer2MUbrP2MEyt6VHBDQ6bjdQsnz8AAxkbAAIKDqlIXje5wMg6fhspBA"
    await call.message.answer_video(
        video7,
        caption="Урок 37. Работа с графикой в Delfi: Графические возможности Delfi. Объекты Image and Shape. Свойства Pixels. Инструменты MoveTo и LineTo. Практическая работа"
    )
    video8 = "BAACAgIAAxkBAAIerWMUbmwgnD_9y1uxs7J9RVp_3zMnAAIWGwACCg6pSNei486_J44pKQQ"
    await call.message.answer_video(
        video8, caption="Урок 38. Использование групп радиокнопок в приложении. Практическая работа"
    )
    video9 = "BAACAgIAAxkBAAIeq2MUbhUbVcAg-KX-MkwAAZ27jET_SgACFBsAAgoOqUjJ2CAdP01WtykE"
    await call.message.answer_video(
        video9, caption="Урок 39. Объект Timer и его применение"
    )
    video10 = "BAACAgIAAxkBAAIeqWMUbciIXXxE1pb0JUD4uZolYZG7AAISGwACCg6pSOtNu1yauegOKQQ"
    await call.message.answer_video(
        video10, caption="Урок 40. Объект Timer и его применение. Практическая работа", reply_markup=DavomVideo104ru
    )


@dp.callback_query_handler(text="davom104ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIep2MUbYavYYNgFsz3yvKqEJ6qKlXSAAIRGwACCg6pSC27E6b12FgmKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 41. Размещение в рисунке других объектов: Размещение в рисунке текста. размещение в рисунке фигур")
    video2 = "BAACAgIAAxkBAAIepWMUbSozb3lt1Fn1fZxynMqI4hqLAAIKGwACCg6pSNsmHdwPxQiaKQQ"
    await call.message.answer_video(
        video2, caption="Урок 42. Размещение в рисунке других объектов: Размещение в рисунке текста. Размещение в рисунке фигур. Практическая работа"
    )
    video3 = "BAACAgIAAxkBAAIeo2MUbN1wTQ1Z5FkDa_at7BK2ks2fAAIGGwACCg6pSEURv1wMX7dWKQQ"
    await call.message.answer_video(
        video3, caption="Урок 43. Примеры графических анимированных приложений"
    )
    video4 = "BAACAgIAAxkBAAIeoWMUbI5vIlwB_BVhU0XTZb2ep2FoAAICGwACCg6pSFpOpDMGgoo8KQQ"
    await call.message.answer_video(
        video4, caption="Урок 44. Компьютерные вирусы и способы защиты от вирусов"
    )
    video5 = "BAACAgIAAxkBAAIen2MUbEkMASAZ7ayESw7WGPMNcJQDAAIBGwACCg6pSGnUyxKmT7PdKQQ"
    await call.message.answer_video(
        video5, caption="Урок 45. Примеры графических и анимированных приложений"
    )
    video6 = "BAACAgIAAxkBAAIenWMUa_q6NEfPIt_RHhcdV3EIMJfYAAL_GgACCg6pSP46W9Rh5KdxKQQ"
    await call.message.answer_video(
        video6, caption="Урок 46. Примеры решения выражений в Delphi"
    )
    video7 = "BAACAgIAAxkBAAIem2MUa8IbPjUMjaZvntwr2nORCKIoAAL-GgACCg6pSMn8uoFZd0JLKQQ"
    await call.message.answer_video(
        video7, caption="Урок 47. Повторение", reply_markup=DavomVideo105ru
    )

#################################################################################################################


@dp.callback_query_handler(text="5Plan")
async def KitobBesh(call: CallbackQuery):
    KitobBeshsinf = 'BQACAgIAAxkBAAIfTWMVma3TTJVZ1M9ALrXJeQnGPaT-AAIuGwACVN2YSOnZFjOhrFp1KQQ'
    await call.message.reply_document(KitobBeshsinf)


@dp.callback_query_handler(text="6Plan")
async def KitobBesh(call: CallbackQuery):
    Kitoboltisinf = 'BQACAgIAAxkBAAIfT2MVmcZs9cdMN2RNiupaXSfrdFebAAIvGwACVN2YSEssf50CNfbPKQQ'
    await call.message.reply_document(Kitoboltisinf)


@dp.callback_query_handler(text="7Plan")
async def KitobBesh(call: CallbackQuery):
    Kitobyettisinf = 'BQACAgIAAxkBAAIfUWMVmc_w5QABXI69NDfRUWK5i-wG-AACMBsAAlTdmEi69C8zASUuKCkE'
    await call.message.reply_document(Kitobyettisinf)


@dp.callback_query_handler(text="8Plan")
async def KitobBesh(call: CallbackQuery):
    Kitobsaksinf = 'BQACAgIAAxkBAAIfU2MVmdokmw4Q-mHIRAOo_haeEDodAAIxGwACVN2YSFieW7fkjSIQKQQ'
    await call.message.reply_document(Kitobsaksinf)


@dp.callback_query_handler(text="9Plan")
async def KitobBesh(call: CallbackQuery):
    Kitobtosinf = 'BQACAgIAAxkBAAIfVWMVmeTQHOU-cDzL4cIPnAaRPL6AAAIyGwACVN2YSN5letrqhOX9KQQ'
    await call.message.reply_document(Kitobtosinf)


@dp.callback_query_handler(text="10Plan")
async def KitobBesh(call: CallbackQuery):
    Kitobonsinf = 'BQACAgIAAxkBAAIfV2MVmexJHGeW3CzrTv_Z66qwk4sbAAIzGwACVN2YSMP5RlORcs00KQQ'
    await call.message.reply_document(Kitobonsinf)


@dp.callback_query_handler(text="11Plan")
async def KitobBesh(call: CallbackQuery):
    Kitobonbsinf = 'BQACAgIAAxkBAAIfWWMVmfSaAAGrH5bPcQqaRv9kmnIzPQACNBsAAlTdmEgSEt4v7vhmoSkE'
    await call.message.reply_document(Kitobonbsinf)

#################################################################################################################


@dp.callback_query_handler(text="5Planru")
async def KitobBesh(call: CallbackQuery):
    KitobBeshsinf = 'BQACAgIAAxkBAAIfW2MVmnzDmj9Rg6fJSMgtB3wNPJ-vAAKFGQACCg6xSAuHDqUHOBVTKQQ'
    await call.message.reply_document(KitobBeshsinf)


@dp.callback_query_handler(text="6Planru")
async def KitobBesh(call: CallbackQuery):
    Kitoboltisinf = 'BQACAgIAAxkBAAIfYGMVmoSuo2TTxEGg6x90VxWxu23WAAKIGQACCg6xSO_0AteIa4kEKQQ'
    await call.message.reply_document(Kitoboltisinf)


@dp.callback_query_handler(text="7Planru")
async def KitobBesh(call: CallbackQuery):
    Kitobyettisinf = 'BQACAgIAAxkBAAIf7GMVnurPBvdrxiwuZkoCuirjzcKQAAKzGQACCg6xSAFrwwETYq-XKQQ'
    await call.message.reply_document(Kitobyettisinf)


@dp.callback_query_handler(text="8Planru")
async def KitobBesh(call: CallbackQuery):
    Kitobsaksinf = 'BQACAgIAAxkBAAIfY2MVmoS_zxqC7Bp6HZAH3STfZieTAAKKGQACCg6xSIPso2cKrv1HKQQ'
    await call.message.reply_document(Kitobsaksinf)


@dp.callback_query_handler(text="9Planru")
async def KitobBesh(call: CallbackQuery):
    Kitobtosinf = 'BQACAgIAAxkBAAIf6mMVnuJADZiQbLOCRyNH6fYDKPSBAAKwGQACCg6xSHdXrQ3lr_B7KQQ'
    await call.message.reply_document(Kitobtosinf)


@dp.callback_query_handler(text="10Planru")
async def KitobBesh(call: CallbackQuery):
    Kitobonsinf = 'BQACAgIAAxkBAAIfXWMVmoQFgR8korkPSCIl_59x2BPEAAKGGQACCg6xSIPL11-5umPjKQQ'
    await call.message.reply_document(Kitobonsinf)


@dp.callback_query_handler(text="11Planru")
async def KitobBesh(call: CallbackQuery):
    Kitobonbsinf = 'BQACAgIAAxkBAAIfXmMVmoTntVCdXuoAAQoPiIDFsMMD9gAChxkAAgoOsUjVpvY0muoIUSkE'
    await call.message.reply_document(Kitobonbsinf)


#######################################################################################################################################


@dp.callback_query_handler(text="Oldingi112ru")
@dp.callback_query_handler(text="11Videoru")
async def Oltibir(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIhN2MWEsvvbMa_JU19wbIrgtb8zKRYAALNHAACCg6xSAwC80qVEONnKQQ'
    await call.message.reply_video(VDars1, caption="Урок 1. Графические объекты и способы их отображения")
    video2 = "BAACAgIAAxkBAAIhNWMWEjhnsfdqscDGtZNfUiJYVJIcAALHHAACCg6xSGKPKthDtL1pKQQ"
    await call.message.answer_video(
        video2, caption="Урок 2. Двумерная и трехмерная графика"
    )
    video3 = "BAACAgIAAxkBAAIhM2MWEbE51-7952QW8JBNAwekn6epAALEHAACCg6xSIqJefqX_RtqKQQ"
    await call.message.answer_video(
        video3, caption="Урок 3. Основы работы в растровом графическом редакторе Photoshop и его интерфейс"
    )
    video4 = "BAACAgIAAxkBAAIhMWMWEVLrrA-DfyVkAko_7FRNah58AALDHAACCg6xSPR36Oqn5CHyKQQ"
    await call.message.answer_video(
        video4, caption="Урок 4. Практическая работа"
    )
    video5 = "BAACAgIAAxkBAAIhL2MWELtvkg4NbPXGfaQDWRHsn9Y3AAK-HAACCg6xSNAjnq-wQsKRKQQ"
    await call.message.answer_video(
        video5, caption="Урок 5. Повторение"
    )
    video6 = "BAACAgIAAxkBAAIhLWMWEGfx02Pw1kJOep9lw6mdp8QEAAK4HAACCg6xSGSSrnVvK_M_KQQ"
    await call.message.answer_video(
        video6, caption="Урок 6. Панель инструментов и палитры Photoshop"
    )
    video7 = "BAACAgIAAxkBAAIhK2MWEA9QcnfiGwilDRnh4_xXCDLVAAK1HAACCg6xSBsHtGpq5dX_KQQ"
    await call.message.answer_video(
        video7, caption="Урок 7. Практическая работа"
    )
    video8 = "BAACAgIAAxkBAAIhKWMWD7mWXfUMyMu3EGajKfxrg8OnAAKxHAACCg6xSCJ-BWbJWlteKQQ"
    await call.message.answer_video(
        video8, caption="Урок 8. Работа с файлами изображений в Photoshop"
    )
    video9 = "BAACAgIAAxkBAAIhJ2MWD3aVcALQjCJhNXxNAAGkTtQHOAACrhwAAgoOsUjbkPAedVAZEikE"
    await call.message.answer_video(
        video9, caption="Урок 9. Выделение в Photoshop части изображения в виде геометрической фигуры"
    )
    video10 = "BAACAgIAAxkBAAIhJWMWDxg-zMa6ksmwU__Vx5RDyQehAAKsHAACCg6xSD7_l6lfpredKQQ"
    await call.message.answer_video(
        video10, caption="Урок 10. Другие способы выделения части изображения",
        reply_markup=DavomVideo111ru
    )


@dp.callback_query_handler(text="Oldingi113ru")
@dp.callback_query_handler(text="davom111ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIhI2MWDqP_xDB0MHN6tsU3ou4ZZQULAAKpHAACCg6xSFCsfaO-IfdyKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 11. Кодирование изображений и операции трансформирования")
    video2 = "BAACAgIAAxkBAAIhIWMWDkfwhtOro7O8UDAzoGXphPZOAAKnHAACCg6xSMdq4yQvcp_6KQQ"
    await call.message.answer_video(
        video2, caption="Урок 12. Слои в Photoshop и их применение"
    )
    video3 = "BAACAgIAAxkBAAIhH2MWDbPJxy8SLoUevr1fvbmVseaNAAKlHAACCg6xSEUZjb4hUoUnKQQ"
    await call.message.answer_video(
        video3, caption="Урок 13. Работа с цветами в Photoshop. Практическое занятие"
    )
    video4 = "BAACAgIAAxkBAAIhHWMWDVEFkts-UXZKxcOB4B2UPzMxAAKjHAACCg6xSCc2X1GJ4oYeKQQ"
    await call.message.answer_video(
        video4, caption="Урок 14. Цветовые системы в Photoshop"
    )
    video5 = "BAACAgIAAxkBAAIhG2MWDPSIEndYdZs4-IZzKAq7EZiRAAKiHAACCg6xSB-z7uK5635yKQQ"
    await call.message.answer_video(
        video5, caption="Урок 15. Цветовые системы в Фотошоп"
    )
    video6 = "BAACAgIAAxkBAAIhGWMWDKlsOlSVQOgAAQEeG7Jk3bArHwACoBwAAgoOsUgRNZw2QnEwSCkE"
    await call.message.answer_video(
        video6, caption="Урок 16. Работа с цветами в Photoshop"
    )
    video7 = "BAACAgIAAxkBAAIhF2MWDF9b4FSf_12ftjRU0J9nxv7YAAKeHAACCg6xSPTq2X9NnzW5KQQ"
    await call.message.answer_video(
        video7, caption="Урок 17. Каналы и фильтры в Photoshop. Практическая работа"
    )
    video8 = "BAACAgIAAxkBAAIhFWMWDASPRZjAidaAJjY63ZUiyqQRAAKcHAACCg6xSJGlnVG5yOB8KQQ"
    await call.message.answer_video(
        video8,
        caption="Урок 18. Работа с кистью и карандашом. Практическая работа."
    )
    video9 = "BAACAgIAAxkBAAIhE2MWC8ExWfh2hFoS8rhuky0nsw72AAKbHAACCg6xSH3X0JtApx9fKQQ"
    await call.message.answer_video(
        video9, caption="Урок 19. Вставка геометрических фигур и векторных объектов в изображение"
    )
    video10 = "BAACAgIAAxkBAAIhcGMWIqaJzA1RvMqG1S0gDuQCU00PAAImHQACCg6xSLuQkeQTT7ASKQQ"
    await call.message.answer_video(
        video10, caption="Урок 20. Вставка геометрических фигур и векторных объектов в изображение. Практическая работа",
        reply_markup=DavomVideo112ru
    )


@dp.callback_query_handler(text="Oldingi114ru")
@dp.callback_query_handler(text="davom112ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIhEWMWC4QykAi5W_aUm42ZJouIt-HpAAKZHAACCg6xSCMB5q-xt9f4KQQ'
    await call.message.reply_video(VDars1, caption="Урок 21. Вставка текста в изображение")
    video2 = "BAACAgIAAxkBAAIhD2MWCzSna0cpkpgAAUNJTk3eVRlWJwACmBwAAgoOsUgtVhaFia51pykE"
    await call.message.answer_video(
        video2, caption="Урок 22. Понятие Web- страницы, Web-сайта и Web дизайна"
    )
    video3 = "BAACAgIAAxkBAAIhDWMWCvMgEnTZrHaC2TY4SvtbN7JMAAKXHAACCg6xSP0wiM1fQ7pWKQQ"
    await call.message.answer_video(
        video3, caption="Урок 23. Понятие Web-страницы, Web-сайта и Web-дизайна. Практическая работа."
    )
    video4 = "BAACAgIAAxkBAAIhC2MWCr7LxbzODmpjCZLoDXq4Ml67AAKWHAACCg6xSILF1YpYgtTAKQQ"
    await call.message.answer_video(
        video4,
        caption="Урок 24. Web-дизайн и его программное обеспечение. Создание и редактирование Web-страниц программой Macromedia Flash"
    )
    video5 = "BAACAgIAAxkBAAIhCWMWCnB0LOq648pfNoGXSXKzN32FAAKTHAACCg6xSFgHOX_7urXeKQQ"
    await call.message.answer_video(
        video5, caption="Урок 25. Web-дизайн и его программное обеспечение. Создание и редактирование Web-страниц программой Macromedia FlashУрок 25. Web-дизайн и его программное обеспечение. Создание и редактирование Web-страниц программой Macromedia Flash. Практическая работа"
    )
    video6 = "BAACAgIAAxkBAAIhB2MWCjDKKLITVX0tM6o7qHXp3P1hAAKPHAACCg6xSJbuCE7VldByKQQ"
    await call.message.answer_video(
        video6, caption="Урок 26. Вставка в Web-страницы графической информации и их дизайн"
    )
    video7 = "BAACAgIAAxkBAAIhBWMWCdTk4Ww0dfvkKHIHMTQnrz2zAAKMHAACCg6xSK05irhKE1kSKQQ"
    await call.message.answer_video(
        video7, caption="Урок 27. Вставка геометрических фигур и векторных объектов в изображении"
    )
    video8 = "BAACAgIAAxkBAAIhA2MWCYKX-bRJKcCZ4YsqshyKX-DSAAKKHAACCg6xSG9emxP3BFaSKQQ"
    await call.message.answer_video(
        video8,
        caption="Урок 28. Повторение"
    )
    video9 = "BAACAgIAAxkBAAIhAWMWCU-cbRnYG12BbE1uupaN5I66AAKHHAACCg6xSBVkU9mP1mwmKQQ"
    await call.message.answer_video(
        video9, caption="Урок 29. Создание и редактирование форм на Web-странице и их оформление"
    )
    video10 = "BAACAgIAAxkBAAIg_2MWCQNKk3BEVonDkTlPfrbtgaLVAAKGHAACCg6xSF86XC_zTdH_KQQ"
    await call.message.answer_video(
        video10, caption="Урок 30. Повторение",
        reply_markup=DavomVideo113ru
    )


@dp.callback_query_handler(text="Oldingi115ru")
@dp.callback_query_handler(text="davom113ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIg_WMWCK7xXCxTYhPRpx3wEICQmWEHAAKDHAACCg6xSMyNAhBPwJrxKQQ'
    await call.message.reply_video(VDars1, caption="Урок 31. Создание и редактирование форм на Web-странице и их оформление")
    video2 = "BAACAgIAAxkBAAIg-2MWCH9mSi8UkQ7fdNLm_Oh2u-sbAAKCHAACCg6xSHr9rPwFMsECKQQ"
    await call.message.answer_video(
        video2,
        caption="Урок 32. Вставка геометрических фигур и векторных объектов в изображении. Практическая работа"
    )
    video3 = "BAACAgIAAxkBAAIg-WMWCCq-Jy6nsxWE2RLCP3YqNmxUAAJ_HAACCg6xSBuVFUafyddGKQQ"
    await call.message.answer_video(
        video3, caption="Урок 33. Анимация в Web-границе и способы ее размещения"
    )
    video4 = "BAACAgIAAxkBAAIg92MWCARmu5s8jRF6PH_m_ZgrzWraAAJ-HAACCg6xSDrQ4ajUFVlxKQQ"
    await call.message.answer_video(
        video4, caption="Урок 34. Повторение"
    )
    video5 = "BAACAgIAAxkBAAIg9WMWB7ihzJ9HWhyG8nO4VHp4zvOfAAJ7HAACCg6xSOuZdlmOSUtsKQQ"
    await call.message.answer_video(
        video5, caption="Урок 35. Вставка геометрических фигур и векторных объектов в изображение. Практическая работа"
    )
    video6 = "BAACAgIAAxkBAAIg82MWB2QxiCRp9f3S4qVRPdzhaqk6AAJ6HAACCg6xSMwZZh7rFgTOKQQ"
    await call.message.answer_video(
        video6, caption="Урок 36. Аудио информация и работа с ней"
    )
    video7 = "BAACAgIAAxkBAAIg8WMWBxkqf7T46lcGxOLP191d1wypAAJ5HAACCg6xSHLSJQLAj6-JKQQ"
    await call.message.answer_video(
        video7,
        caption="Урок 37. Установка ссылок между Web-страницами"
    )
    video8 = "BAACAgIAAxkBAAIRMGMB5rYR8sdhBBBmRoNP30yFzNcpAAJtGgACOUoRSKlxyurY2aY-KQQ"
    await call.message.answer_video(
        video8, caption="Урок 38. Вставка в Web-страницы графической информации и их дизайн. Повторение"
    )
    video9 = "BAACAgIAAxkBAAIg72MWBr7XVIEkLhhMePWoEurLlfFKAAJ4HAACCg6xSOTYAAFEa5sqlSkE"
    await call.message.answer_video(
        video9, caption="Урок 39. Анимация в Web-странице и способы её размещения. Повторение"
    )
    video10 = "BAACAgIAAxkBAAIg62MWBid7bizhylssFGXKGdwNeW8VAAJ2HAACCg6xSF3LPj0MvWpGKQQ"
    await call.message.answer_video(
        video10, caption="Урок 40. Понятие информационной безопасности и показатели ее эффективности",
        reply_markup=DavomVideo114ru
    )


@dp.callback_query_handler(text="Oldingi116ru")
@dp.callback_query_handler(text="davom114ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIg6WMWBelxqgkAAaEmFr0Ha69pc-w2kgACdRwAAgoOsUggd6R4dN_RECkE'
    await call.message.reply_video(VDars1,
                                   caption="Урок 41. Задачи информационной безопасности составные части и методы защиты информации")
    video2 = "BAACAgIAAxkBAAIg52MWBajxpIF8_-gn2tSmqe2dgUrgAAJzHAACCg6xSKyLQhuzmsOeKQQ"
    await call.message.answer_video(
        video2, caption="Урок 42. Задачи информационной безопасности составные части и методы защиты информации. Практическая работа"
    )
    video3 = "BAACAgIAAxkBAAIg5WMWBWcsdAhco-J89uXK8_lCWhkJAAJwHAACCg6xSBA8bj4DhPNyKQQ"
    await call.message.answer_video(
        video3, caption="Урок 43. Задачи информационной безопасности составные части и методы защиты информации"
    )
    video4 = "BAACAgIAAxkBAAIg42MWBSd-TYExxhFGeprWU3fNq27EAAJuHAACCg6xSBiJV9L2zN8BKQQ"
    await call.message.answer_video(
        video4, caption="Урок 44. Региональная и глобальная сеть и их зашита"
    )
    video5 = "BAACAgIAAxkBAAIg4WMWBM-8-bOQiIgtnEV_pmE5dhZQAAJqHAACCg6xSDhFy2upvvlZKQQ"
    await call.message.answer_video(
        video5, caption="Урок 45. Региональная и глобальная сеть и их защита. Практическая работа"
    )
    video6 = "BAACAgIAAxkBAAIg32MWBHqPb7Ch8KzFOiHsGSdTqQnyAAJjHAACCg6xSBNlE2d0KNdlKQQ"
    await call.message.answer_video(
        video6, caption="Урок 46. Проблемы безопасности информационных ресурсов в интернете"
    )
    video7 = "BAACAgIAAxkBAAIg3WMWBFKDSvWpDbtHmJNunV9AX0oZAAJdHAACCg6xSJbDS5kuNK4EKQQ"
    await call.message.answer_video(
        video7, caption="Урок 47. Проблемы безопасности информационных ресурсов в интернете. Практическая работа"
    )
    video8 = "BAACAgIAAxkBAAIg22MWBAQ8voEEe0N1FP6fUSSGvU64AAJZHAACCg6xSAlFWsgy1JMLKQQ"
    await call.message.answer_video(
        video8, caption="Урок 48. Электронное правительство"
    )
    video9 = "BAACAgIAAxkBAAIg2WMWA8jAoX8TZe9UyOrHRf2eJEyDAAJXHAACCg6xSAmWi1OdbQlOKQQ"
    await call.message.answer_video(
        video9, caption="Урок 49. Электронное правительство. Практическая работа"
    )
    video10 = "BAACAgIAAxkBAAIg12MWA4hSfumFf5ynhLbXTlUscBxqAAJSHAACCg6xSB9SS-1AUOh9KQQ"
    await call.message.answer_video(
        video10, caption="Урок 50. Структура сервиса электронной почты", reply_markup=DavomVideo115ru
    )


@dp.callback_query_handler(text="davom115ru")
async def Davom6v(call: CallbackQuery):
    VDars1 = 'BAACAgIAAxkBAAIg1WMWA1-KFMdH9vg0HcOdY07s3rcsAAJQHAACCg6xSEMPi95CQDPzKQQ'
    await call.message.reply_video(VDars1,
                                   caption="Урок 51. Структура сервиса элекронной почти. Практическая работа")
    video2 = "BAACAgIAAxkBAAIg02MWAyU5Yy8IibK3LEzA2jdh5VnrAAJOHAACCg6xSDVixXAVlN48KQQ"
    await call.message.answer_video(
        video2, caption="Урок 52. Компьютерные вирусы и способы защиты от вирусов. Практическая работа"
    )
    video3 = "BAACAgIAAxkBAAIhOWMWEumaUyu8F7saYW5MJKlnck9aAALOHAACCg6xSF3aWj7M6dGvKQQ"
    await call.message.answer_video(
        video3, caption="Урок 53. Повторение"
    )
    video4 = "BAACAgIAAxkBAAIhO2MWExln9_LxXxizWpV5mwt9W1bKAALPHAACCg6xSG2hBUoDYxz1KQQ"
    await call.message.answer_video(
        video4, caption="Урок 54. Закрепление", reply_markup=DavomVideo116ru
    )


###########################################################################################################


@dp.callback_query_handler(text="scratch")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrdGNkAr0DBP8X32MlFt4tPGTGinnQAAKkBwACU77ZSpVS9ptzYtdnKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Mo")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIreGNkAu0ykrUrsOzISIZg6htm0mn-AAJkHAACAzgRSYu9Veel9lCtKgQ"
    Program2 = "BQACAgIAAxkBAAIslmNktupZnww6oafAh7KbCvLfFq7EAAIcIAACo_gYSQ6oOMnvr4RxKgQ"
    await call.message.reply_document(Program1)
    await call.message.reply_document(Program2)
    await call.message.answer("👆🏻Programalar yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="OBS")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrgGNkAz2B24TYFqji92xdD79o5kgJAAKdIAACTv3hSLOwww0QxYfBKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Python")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrhGNkA1sVc-xZ-tqKEA5iPViuCbsCAALzEQACBNE5SRGK56lNXwQfKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Movavi")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIriGNkA3C5VBRDkthyELmglVfsvFMQAAJEFgACIP84SuWYBL9vzpgnKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="APr")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrjGNkA6DzhXlPPmWc4kL3JAU-aelrAAJ_BwACcQRZSOacm2xqg9aFKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Aae")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIr8mNkKc5obOOOwa5Xi3wAAbQwjfkvCAACaBAAAswHeEhluQHQyCaZUSoE"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Ps")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrkGNkA7h6e4ZEXFuwNNL8gcVVqGGSAAL-IAACfIkYS-rtDESUGeldKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Iobit")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrlGNkA-yIYzUFTZWIPQzl0Wf_aqYRAALWIAACfIkYS1Qqu7mfJ13wKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="AIMP")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrmWNkBAthCdtB5xun2I9X8yST2iqrAALiIAACfIkYS20Mqeq6q-x1KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Potp")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIroGNkFmWxdUt8I-hCd99tTURWIevfAALjIAACfIkYSxwhpiMkot1gKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="WhatsApp")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrpGNkFohSaO2DlG5NEWZm7APuHqQTAALkIAACfIkYS0Z86HE0MzuGKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Tools")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrqGNkFzERQzWjiH349lqcaMZbixaDAAKnDgACPY4JS3Dp7VWQ-dexKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="WebcamMax")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrrGNkF0zb2aysMFk2LU8vwA4j6C6fAAKbDQACeWGASk6LgRraZGzNKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Mp3Cut")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrsWNkF7EqQ59xw-wYUae7MvcZIVTNAAL_IAACfIkYS1_ldQxz_yHQKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Winrar")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrtmNkF9ht72-A9P3XWGp_Dwbi1v8zAAICIQACfIkYS9uCmnxE00YWKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Chrome")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrumNkGE2WTqIOEQvSdh8EafUfdaI6AAIHIQACfIkYS82_zMJWaZD2KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Torrent")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrvmNkGKvfIvCZj6_BiyF_AudDh19kAAIJIQACfIkYS-1cdBxFLZX4KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Total")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrwmNkGTi8Eh3LcOdKgU5boMDtPE2tAAILIQACfIkYS4AVPn5Ts4o5KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="FastStone")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrx2NkGWHTo0hywX98a42zAAEQ8QprRAACDSEAAnyJGEuJYPApDPwXRioE"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Foxit")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrzGNkGYvSdHj1YWHa1wW2XeKt5UkCAAIUIQACfIkYS_3yWeJeFk3UKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


@dp.callback_query_handler(text="Vuescan")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIr0GNkGak-q_EVhmukRl1PqrYXvBzVAAIWIQACfIkYSzCbzHNexjKYKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)

@dp.callback_query_handler(text="FineReader")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIr1GNkGcRZEPwoljUYU4wtbiB3QIncAAIeIQACfIkYS5haDWwS5R2SKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Programa yuqorida yuborilgan👆🏻", reply_markup=Boshmenu)


##################################################################################################


@dp.callback_query_handler(text="scratchru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrdGNkAr0DBP8X32MlFt4tPGTGinnQAAKkBwACU77ZSpVS9ptzYtdnKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Moru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIreGNkAu0ykrUrsOzISIZg6htm0mn-AAJkHAACAzgRSYu9Veel9lCtKgQ"
    Program2 = "BQACAgIAAxkBAAIslmNktupZnww6oafAh7KbCvLfFq7EAAIcIAACo_gYSQ6oOMnvr4RxKgQ"
    await call.message.reply_document(Program1)
    await call.message.reply_document(Program2)
    await call.message.answer("👆🏻Программы отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="OBSru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrgGNkAz2B24TYFqji92xdD79o5kgJAAKdIAACTv3hSLOwww0QxYfBKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Pythonru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrhGNkA1sVc-xZ-tqKEA5iPViuCbsCAALzEQACBNE5SRGK56lNXwQfKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Movaviru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIriGNkA3C5VBRDkthyELmglVfsvFMQAAJEFgACIP84SuWYBL9vzpgnKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="APrru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrjGNkA6DzhXlPPmWc4kL3JAU-aelrAAJ_BwACcQRZSOacm2xqg9aFKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Aaeru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIr8mNkKc5obOOOwa5Xi3wAAbQwjfkvCAACaBAAAswHeEhluQHQyCaZUSoE"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Psru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrkGNkA7h6e4ZEXFuwNNL8gcVVqGGSAAL-IAACfIkYS-rtDESUGeldKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Iobitru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrlGNkA-yIYzUFTZWIPQzl0Wf_aqYRAALWIAACfIkYS1Qqu7mfJ13wKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="AIMPru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrmWNkBAthCdtB5xun2I9X8yST2iqrAALiIAACfIkYS20Mqeq6q-x1KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Potpru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIroGNkFmWxdUt8I-hCd99tTURWIevfAALjIAACfIkYSxwhpiMkot1gKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="WhatsAppru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrpGNkFohSaO2DlG5NEWZm7APuHqQTAALkIAACfIkYS0Z86HE0MzuGKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Toolsru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrqGNkFzERQzWjiH349lqcaMZbixaDAAKnDgACPY4JS3Dp7VWQ-dexKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="WebcamMaxru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrrGNkF0zb2aysMFk2LU8vwA4j6C6fAAKbDQACeWGASk6LgRraZGzNKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Mp3Cutru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrsWNkF7EqQ59xw-wYUae7MvcZIVTNAAL_IAACfIkYS1_ldQxz_yHQKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Winrarru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrtmNkF9ht72-A9P3XWGp_Dwbi1v8zAAICIQACfIkYS9uCmnxE00YWKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Chromeru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrumNkGE2WTqIOEQvSdh8EafUfdaI6AAIHIQACfIkYS82_zMJWaZD2KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Torrentru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrvmNkGKvfIvCZj6_BiyF_AudDh19kAAIJIQACfIkYS-1cdBxFLZX4KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Totalru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrwmNkGTi8Eh3LcOdKgU5boMDtPE2tAAILIQACfIkYS4AVPn5Ts4o5KgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="FastStoneru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrx2NkGWHTo0hywX98a42zAAEQ8QprRAACDSEAAnyJGEuJYPApDPwXRioE"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Foxitru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIrzGNkGYvSdHj1YWHa1wW2XeKt5UkCAAIUIQACfIkYS_3yWeJeFk3UKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)


@dp.callback_query_handler(text="Vuescanru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIr0GNkGak-q_EVhmukRl1PqrYXvBzVAAIWIQACfIkYSzCbzHNexjKYKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)

@dp.callback_query_handler(text="FineReaderru")
async def Program(call: CallbackQuery):
    Program1 = "BQACAgIAAxkBAAIr1GNkGcRZEPwoljUYU4wtbiB3QIncAAIeIQACfIkYS5haDWwS5R2SKgQ"
    await call.message.reply_document(Program1)
    await call.message.answer("👆🏻Программа отправлена ​​выше👆🏻", reply_markup=ruBoshmenu)
