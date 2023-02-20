from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import games
file_input = "DBase.txt"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    # print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f"сумма {x} + {y} = {x+y}")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text.split()
    await update.message.reply_text(games.show_matrix())
    await update.message.reply_text(msg)
    await update.message.reply_text(games.player(int(msg[1])))

    
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text.split()
    await update.message.reply_text(games.random_string())
    # await update.message.reply_text(msg)

app = ApplicationBuilder().token("5902874803:AAGO4WkdEEnXy8FGF14tVTneQVNFERcHeaE").build()
print("start server")

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("joke", joke))
app.add_handler(MessageHandler(any, any))


app.run_polling()
