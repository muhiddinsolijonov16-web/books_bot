import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,FSInputFile

from buttons import button,maktab_button
from IT_course_button import IT_button

bot = Bot(token="8817651610:AAGhMH7I2YedCE94d3W9BPblQR9k6tRdwq8")

dp = Dispatcher()

@dp.message(CommandStart())
async def Start_handler(message:Message):
    await message.answer("xush kelibsiz",
                        reply_markup= button)

@dp.message(F.text == "Go Out")
async def back_menu(message:Message):
    await message.answer("asosoiy menu ga qaytildi",reply_markup=button)

@dp.message(F.contact)
async def contact_handler(message:Message):
    await message.answer("contact qabu qilindi")

@dp.message(F.location)
async def location_handler(message:Message):
    await message.answer("lokatsiya qabu qilindi")

@dp.message(F.text == "IELTS course")
async def ielts_get_info(message:Message):
    await message.answer(" bu xalqaro miqyosda ingliz tili darajasini aniqlovchi" \
    " eng mashhur imtihon tizimidir. O'zbekistonda xorijiy va mahalliy universitetlarga" \
    " kirish, magistratura, ishga joylashish yoki chet elga (AQSh, Buyuk Britaniya, Kanada," \
    " Avstraliya va h.k.) ko'chib ketish uchun asosan IELTS sertifikati talab qilinadi.")

@dp.message(F.text == "IT course")   
async def IT_course(message:Message):
    await message.answer("IT kurslar bilan tanishing",
                        reply_markup= IT_button)

@dp.message(F.text == "Python")
async def python_about(message:Message):
    await message.answer("Python — bu yuqori darajadagi, organish uchun qulay va " \
                                "keng qamrovli umumiy maqsadli dasturlash tili.")


@dp.message(F.text == "JavaScrpt")
async def JavaScrpt_about(message:Message):
    await message.answer("JavaScript — Vikipediya — bu yuqori darajali," \
    " ko'p paradigmali dasturlash tili bo'lib," \
    " veb-sahifalarga dinamiklik va interaktivlik berish uchun ishlatiladi.")


@dp.message(F.text == "C/C++")
async def C_about(message:Message):
    await message.answer("C va C++ — zamonaviy dasturlash olamidagi eng " \
    "qudratli, yuqori unumdorlikka ega va tizimli dasturlash tillaridir.")


@dp.message(F.text == "Java")
async def Java_about(message:Message):
    await message.answer("Java — bu obektsiz-yonaltirilgan, platformadan" \
    " mustaqil va yuqori darajali dasturlash tili bolib, 1995-yilda Jeyms Gosling va" \
    " uning jamoasi tomonidan Sun Microsystems kompaniyasida yaratilgan")
    

@dp.message(F.text == "Maktab darsliklari")
async def Maktab_darliklari(message:Message):
    await message.answer("maktab darsliklari",
reply_markup=maktab_button)

@dp.message(F.text == "1-sinf darsligi")
async def sinf_1_button(message: Message):
    file = FSInputFile("file/file1.pdf")
    await message.answer_document(file)
    photo = FSInputFile("file/1.png")
    await message.answer_photo(photo)

@dp.message(F.text == "2-sinf darsligi")
async def sinf_2_button(message: Message):
    file = FSInputFile("file/file2.pdf")
    await message.answer_document(file)
    photo = FSInputFile("file/2.png")
    await message.answer_photo(photo)

@dp.message(F.text == "3-sinf darsligi")
async def sinf_3_button(message: Message):
    file = FSInputFile("file/file3.pdf")
    await message.answer_document(file)
    photo = FSInputFile("file/3.png")
    await message.answer_photo(photo)

@dp.message(F.text == "4-sinf darsligi")
async def sinf_4_button(message: Message):
    file = FSInputFile("file/file4.pdf")
    await message.answer_document(file)
    photo = FSInputFile("file/4.png")
    await message.answer_photo(photo)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
