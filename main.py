from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7639062333:AAHvahCdnFXH8dkl0hxxuX4MgV4aUiapnYE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[KeyboardButton("Открыть график", web_app=WebAppInfo(url="https://myapp.vercel.app"))]]
    await update.message.reply_text("Выбирай:", reply_markup=ReplyKeyboardMarkup(kb, resize_keyboard=True))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
