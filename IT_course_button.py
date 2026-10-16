from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

IT_button = ReplyKeyboardMarkup(
   keyboard= [
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="JavaScrpt")
        ],
        [
            KeyboardButton(text="C/C++"),
            KeyboardButton(text="Java")
        ],
        [
            KeyboardButton(text="Go Out")
        ]
    ],
    resize_keyboard=True
)
