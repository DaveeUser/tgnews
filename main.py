from telegram import Bot, Filters, MessageTypes, ParseMode, Update, InlineKeyboardButton
from news import gets

TOKENKEY = ""

bot = Bot(token=TOKENKEY)


@bot.message(content_types=[MessageTypes.TEXT], filters=Filters.command('help'))
async def help_command(update: Update):
    # Obtener el mensaje original
    message = await update.get_message()
    if not message:
        return
    # Convertir el mensaje a mayúsculas
    new_text = message.Text.upper()

    # Mandar el nuevo mensaje
    await update.send_message(new_text)


async def news_button(update: Update):

    data = update.callback_query.data[0].split()

    news = await gets.getbutton(data[0], int(data[1]) + 1)

    buttons = []
    button1 = InlineKeyboardButton(text="Next", callback_data=f"{data[0]} {int(data[1]) + 1}")
    button2 = InlineKeyboardButton(text="url", url=news["url"])
    buttons.append([button1, button2])

    # Enviamos los botones
    await update.answer(
        text=news["title"],
        inline_query=buttons
    )


@bot.message(content_types=[MessageTypes.TEXT], filters=Filters.command('news'))
async def news_command(update: Update):
    # Obtener el mensaje original
    message = await update.get_message()
    if not message:
        return

    try:
        notices = await gets.get_noticias(message.Text)
    except:
        pass

    buttons = []
    button1 = InlineKeyboardButton(text="Next", callback_data=f"{message.Text} 1")
    button2 = InlineKeyboardButton(text="URL", url=notices[0]["url"])
    buttons.append([button1, button2])

    # Enviamos los botones
    await update.answer(
        text=notices[0]["title"],
        inline_query=buttons
    )


if __name__ == "__main__":

    bot.add_handler(help_command, Filters.incoming_message())
    bot.add_handler(news_command, Filters.incoming_message())
    bot.add_handler(news_button, Filters.button())

    while True:
        try:
            bot.start_polling()
            bot.stop_polling()
        except KeyboardInterrupt:
            break
