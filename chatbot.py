
from telegram.bot import Bot
from telegram.update import Update
from telegram.ext.dispatcher import Dispatcher
from telegram.ext import (
    Updater,
CommandHandler,
ConversationHandler,
Filters,
MessageHandler
)

Name,Age,Ph_no = range(3)

def hey(update,context):
    bot = context.bot
    bot.send_message(
        update.effective_chat.id,
        "Hey, I'm the bot"
    )

def talk(update,context):
    bot = context.bot
    bot.send_message(
        update.effective_chat.id,
        "Hey, I'm the bot, What's ur name \n type /cancel to stop talking"
    )
    return Name

def name(update,context):
    print("Name :", update.message.text)
    context.user_data["userName"] = update.message.text
    bot = context.bot
    bot.send_message(
        update.effective_chat.id,
        "What's ur age \n type /cancel to stop talking"
    )
    return  Age

def age(update,context):
    print("Age :", update.message.text)
    context.user_data["userAge"] = update.message.text
    bot = context.bot
    bot.send_message(
        update.effective_chat.id,
        "What's ur ph_no \n type /cancel to stop talking"
    )
    return Ph_no

def ph_no(update,context):
    print("ph_no :", update.message.text)
    context.user_data["userPh_no"] = update.message.text
    bot = context.bot
    bot.send_message(
        update.effective_chat.id,
        "Your Details\n"+
        "NAME : "+context.user_data["userName"]+
        "\nAGE : "+context.user_data["userAge"]+
        "\nPH_NO : "+context.user_data["userPh_no"]

    )
    return ConversationHandler.END

def cancel(update,context):
    bot = context.bot
    bot.send_message(
        update.effective_chat.id,
        "ok, i will stop talking"
    )
    return ConversationHandler.END


def main():
    TOK = "1482015029:AAFV9jZHci0gS-5MrKxPVsUbfXLN46hqmKY"
    updater = Updater(TOK,use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("hey",hey))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("talk",talk)],
        states={
            Name : [MessageHandler(filters=~Filters.command,callback=name)],
            Age: [MessageHandler(filters=Filters.regex('[0-9]'), callback=age)],
            Ph_no : [MessageHandler(filters=Filters.regex('[0-9]'),callback=ph_no)]
        },
        fallbacks=[CommandHandler("cancel",cancel)]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()


main()
