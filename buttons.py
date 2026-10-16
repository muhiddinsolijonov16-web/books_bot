from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

button = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="IT course")],[
            KeyboardButton(text="IELTS course")],[
        
        
            KeyboardButton(text="Maktab darsliklari")],[
            KeyboardButton(text="Kontakt yuborish",style="danger",request_contact=True)],[
            KeyboardButton(text="Lokatsiya yuborish",style="danger",request_location=True)]
           
        
    ],
    resize_keyboard=True
)
buttons = []
for i in range(1,5):
    a = [KeyboardButton(text=f"{i}-sinf darsligi")]
    buttons.append(a)
buttons.append([ KeyboardButton(text="Go Out")])
maktab_button = ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)
