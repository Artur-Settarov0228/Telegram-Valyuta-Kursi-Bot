from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def banks_keyboard():
    keyboard = [
        [InlineKeyboardButton("🏦 Hamkorbank", url="https://hamkorbank.uz")],
        [InlineKeyboardButton("🏦 Milliy bank", url="https://nbu.uz")],
        [InlineKeyboardButton("🏦 Aloqabank", url="https://aloqabank.uz")]
    ]

    return InlineKeyboardMarkup(keyboard)
