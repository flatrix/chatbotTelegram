from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

 
STATE1 = 1
STATE2 = 2

def welcome(update, context):
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    message = 'Olásss, ' + firstName +' '+ lastName +'!'
    #message = "Olá, Flávioss!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def duvida(update, context):
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    message = 'Ok ' + firstName +', estamos aqui para esclarecer suas dúvidas, vamos iniciar?\nClique em /start!'
    #message = "Olá, Flávioss!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def feedback(update, context):
    message = 'Por favor, digite um feedback para o nosso tutorial:'
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def mensagem(update, context):
    message = 'Por favor, digite uma mensagem para enviar:'
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE3

def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = """Seu feedback foi muito curtinho... 
                        \nInforma mais pra gente, por favor?"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigada pelo seu feedback!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return ConversationHandler.END


def inputFeedback2(update, context):
    feedback = update.message.text
    message = "Muito obrigada pelo seu feedback!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def inputMensagem(update, context):
    mensagem = update.message.text
    message = "Muito obrigada pela sua mensagem!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

def askForNota(update, context):
    question = 'Qual nota você dá para o tutorial?'
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("👎 1", callback_data='1'),
          InlineKeyboardButton("2", callback_data='2'),
          InlineKeyboardButton("🤔 3", callback_data='3'),
          InlineKeyboardButton("4", callback_data='4'),
          InlineKeyboardButton("👍 5", callback_data='5')]])
    update.message.reply_text(question, reply_markup=keyboard)

def getNota(update, context):
    query = update.callback_query
    print(str(query.data))
    message = 'Obrigada pela sua nota: ' + str(query.data) 
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '981937639:AAFRCmVAy-_nBVXm-iX5OMX_bJ3DSfjv-sM'
    updater = Updater(token=token, use_context=True)

    conversation_handler = ConversationHandler(
        #entry_points=[CommandHandler('feedback', feedback)],
        entry_points=[CommandHandler('mensagem', mensagem)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)],
            STATE3: [MessageHandler(Filters.text, inputMensagem)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])

    updater.dispatcher.add_handler(conversation_handler)
    updater.dispatcher.add_handler(CommandHandler('nota', askForNota))
    updater.dispatcher.add_handler(CallbackQueryHandler(getNota))
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(CommandHandler('duvida', duvida))

    updater.start_polling()
    print(str(updater))
    updater.idle()

if __name__ == "__main__":
    main()