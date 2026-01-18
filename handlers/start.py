from keyboards.menu import get_menu_keyboard
from keyboards.banks import banks_keyboard

async def start(update, context):
    await update.message.reply_text(
        "Assalomu alaykum!\n"
        "Valyuta botga xush kelibsiz.\n\n"
        "Valyutani tanlang yoki banklar ro‘yxatini ko‘ring:",
        reply_markup=get_menu_keyboard()
    )

    await update.message.reply_text(
        "🏦 Banklar havolalari:",
        reply_markup=banks_keyboard()
    )
