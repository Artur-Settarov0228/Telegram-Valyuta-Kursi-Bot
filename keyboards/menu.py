from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# tugmalar menyusi 
def get_menu_keyboard():
    keyboard = [
        ["USD", "EUR", "RUB"],
        ["📋 Barcha kurslar"]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)



