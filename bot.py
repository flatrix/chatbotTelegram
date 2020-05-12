from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    message = 'Olá, ' + firstName +' '+ lastName +'!'
    #message = "Olá, Flávioss!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def duvida(update, context):
    username = update.message.from_user.username
    firstName = update.message.from_user.first_name
    lastName = update.message.from_user.last_name
    message = 'Ok ' + firstName +', estamos aqui para esclarecer suas dúvidas, vamos iniciar?\n clique em /start!'
    #message = "Olá, Flávioss!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    token = '981937639:AAFRCmVAy-_nBVXm-iX5OMX_bJ3DSfjv-sM'
    updater = Updater(token=token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(CommandHandler('duvida', duvida))

    updater.start_polling()
    print(str(updater))
    updater.idle()

if __name__ == "__main__":
    main()