from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hio ," + update.effective_user.first_name + ", I'm something like Sleepy's assistant? You can ask me anything (Well, not anything, but some are a fact)"),

async def about_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can watch information about artist here: http://")

async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm just a assistant bot?")

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    number = random.randint(1, 6)
    await update.message.reply_text(f"wow! U got: {number}, actually, i don't care")

async def my_works(update: Update, context: ContextTypes.DEFAULT_TYPE):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(BASE_DIR, 'static', 'img')

    for filename in os.listdir(images_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(images_dir, filename)
            with open(image_path, "rb") as image_file:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=image_file
                )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("my_works", my_works))
app.add_handler(CommandHandler("about_artist", about_artist))
app.add_handler(CommandHandler("about_me", about_me))
app.add_handler(CommandHandler("roll", roll))

app.run_polling()