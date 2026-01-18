from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN_BOT

from handlers.start import start
from handlers.convert import handle_message

def main():
    app = Application.builder().token(TOKEN_BOT).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
