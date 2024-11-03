import telebot
import os
caminhoChave = os.environ['Chave_Bot']  #aqui pega a variavel do sistema que contem a chave api do bot
chaveApi = caminhoChave  
class TelegramBot:
    def __init__(self, chaveApi):
        self.bot = telebot.TeleBot(chaveApi)
        

    def reply_to(self, mensagem, texto):
        self.bot.reply_to(mensagem, texto)

    def register_next_step_handler(self, mensagem, func):
        self.bot.register_next_step_handler(mensagem, func)

    def polling(self):
        self.bot.polling()