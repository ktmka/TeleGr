from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    # print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f"сумма {x} + {y} = {x+y}")


app = ApplicationBuilder().token("5902874803:AAGO4WkdEEnXy8FGF14tVTneQVNFERcHeaE").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))

app.run_polling()
