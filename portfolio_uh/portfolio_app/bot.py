from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hio ," + update.effective_user.first_name + ", I'm something like Sleepy's assistant? You can ask me anything (Well, not anything, but some are a fact)"),

async def about_artist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can watch information about artist here: http://")

async def my_works(update: Update, context: ContextTypes.DEFAULT_TYPE):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(BASE_DIR, 'static', 'img', f'SNOW.jpg')

    for filename in os.listdir(images_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(images_dir, filename)
            with open(image_path, "rb") as image_file:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=image_file,
                    caption=filename
                )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("my_works", my_works))
app.add_handler(CommandHandler("about_artist", about_artist))

app.run_polling()