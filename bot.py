from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8539898207:AAE7Lhaoj4aNW3Ev8VKrrgGHxAPcI8VHbV0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to XAUUSD Forex Bot!\n\n"
        "Type:\n"
        "• hi\n"
        "• price\n"
        "• signal"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hi" in text or "hello" in text:
        await update.message.reply_text(
            "👋 Welcome to XAUUSD Forex Signals!"
        )

    elif "price" in text:
        await update.message.reply_text(
            "💰 Contact the admin for the latest pricing."
        )

    elif "signal" in text:
        await update.message.reply_text(
            "📈 Daily XAUUSD signals are available."
        )

    else:
        await update.message.reply_text(
            "❓ I didn't understand.\nType: hi, price, or signal."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
