from api.currency_api import get_rates

user_currency = {}  # foydalanuvchi tanlagan valyuta

async def handle_message(update, context):
    text = update.message.text
    user_id = update.message.from_user.id
    rates = get_rates()

    if rates is None:
        await update.message.reply_text("API bilan muammo bor.")
        return

    # Agar valyuta tanlansa
    if text in ["USD", "EUR", "RUB"]:
        user_currency[user_id] = text
        await update.message.reply_text(f"{text} tanlandi. Endi summani kiriting:")
        return

    # Agar son kiritilsa
    if user_id in user_currency:
        try:
            amount = float(text)
            currency = user_currency[user_id]
            result = amount * rates[currency]

            await update.message.reply_text(
                f"{amount} {currency} = {round(result, 2)} so‘m"
            )
        except:
            await update.message.reply_text("Iltimos, faqat son kiriting.")
    else:
        await update.message.reply_text("Avval valyuta tanlang.")
