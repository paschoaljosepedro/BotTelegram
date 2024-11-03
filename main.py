from bot import TelegramBot, chaveApi
from bancoDeDados import Database
from dadosWeb import Scraping

class Commands:
    def __init__(self, bot, db,scraping):
        self.bot = bot
        self.db = db
        self.scraping = scraping

        self.bot.message_handler(commands=["opcao1"])(self.opcao1)
        self.bot.message_handler(commands=["asura"])(self.asura)
        self.bot.message_handler(commands=["mangaBuddy"])(self.mangaBuddy)
        self.bot.message_handler(commands=["opcao2"])(self.opcao2)
        self.bot.message_handler(commands=["asuraa"])(self.mostrarNomeAsura)
        self.bot.message_handler(commands=["mangaBuddyy"])(self.mostrarNomeMangaBuddy)
        self.bot.message_handler(commands=["opcao3"])(self.opcao3)
        self.bot.message_handler(commands=["listaAsura"])(self.mostrarTudoAsura)
        self.bot.message_handler(commands=["listaMangaBuddy"])(self.mostrarTudoMangaBuddy)
        self.bot.message_handler(func=self.verificar)(self.responder)

    def opcao1(self, mensagem):
        texto = """
        Onde deseja ler?
        /asura
        /mangaBuddy"""
        self.bot.reply_to(mensagem, texto)

    def asura(self, mensagem):
        self.bot.reply_to(mensagem, "Diga o nome e capítulo do manga desejado, separados por ponto final.")
        self.bot.register_next_step_handler(mensagem, self.insertAsura)

    def insertAsura(self, mensagem):
        try:
            id = mensagem.from_user.id
            nome, capitulo = mensagem.text.split(".")
            self.db.insert('asura', id, nome.strip().lower(), capitulo.strip())
            self.bot.reply_to(mensagem, "Dados armazenados com sucesso!")
        except Exception as e:
            self.bot.reply_to(mensagem, "Houve um erro ao processar seus dados. Tente novamente.")

    def mangaBuddy(self, mensagem):
        self.bot.reply_to(mensagem, "Diga o nome e capítulo do manga desejado, separados por ponto final.")
        self.bot.register_next_step_handler(mensagem, self.insertMangaBuddy)

    def insertMangaBuddy(self, mensagem):
        try:
            id = mensagem.from_user.id
            nome, capitulo = mensagem.text.split(".")
            self.db.insert('mangaBuddy', id, nome.strip().lower, capitulo.strip())
            self.bot.reply_to(mensagem, "Dados armazenados com sucesso!")
        except Exception as e:
            self.bot.reply_to(mensagem, "Houve um erro ao processar seus dados. Tente novamente.")

    def opcao2(self, mensagem):
        texto = """
         Deseja excluir de onde?
        /asuraa
        /mangaBuddyy"""
        self.bot.reply_to(mensagem, texto)

    def mostrarNomeAsura(self, mensagem):
        resultado = self.db.mostrarNomes('asura')
        if resultado:
            nomes = [linha[0] for linha in resultado]
            resposta = '\n'.join(nomes)
        else:
            resposta = "Nenhum resultado encontrado"
        self.bot.reply_to(mensagem, resposta)
        self.bot.register_next_step_handler(mensagem, self.excluirAsura)

    def excluirAsura(self, mensagem):
        try:
            nome = mensagem.text.lower()
            self.db.delete('asura', nome)
            self.bot.reply_to(mensagem, "Dado excluído com sucesso")
        except Exception as e:
            self.bot.reply_to(mensagem, "Houve um erro ao tentar excluir.")

    def mostrarNomeMangaBuddy(self, mensagem):
        resultado = self.db.mostrarNomes('mangaBuddy')
        if resultado:
            nomes = [linha[0] for linha in resultado]
            resposta = '\n'.join(nomes)
        else:
            resposta = "Nenhum resultado encontrado"
        self.bot.reply_to(mensagem, resposta)
        self.bot.register_next_step_handler(mensagem, self.excluirMangaBuddy)

    def excluirMangaBuddy(self, mensagem):
        try:
            nome = mensagem.text.lower()
            self.db.delete('mangaBuddy', nome)
            self.bot.reply_to(mensagem, "Dado excluído com sucesso")
        except Exception as e:
            self.bot.reply_to(mensagem, "Houve um erro ao tentar excluir.")

    def opcao3(self, mensagem):
        texto = """
        Deseja ver a lista de qual?
        /listaAsura
        /listaMangaBuddy"""
        self.bot.reply_to(mensagem,texto)
    
    def  mostrarTudoAsura(self,mensagem):
        try:
            resultado = self.db.mostarTudo('asura')
            if resultado:
             resposta = '\n'.join([f"Nome: {linha[0]} Capítulo: {linha[1]}" for linha in resultado])
            else:
                resposta = "Nenhum resultado encontrado"
            self.bot.reply_to(mensagem, resposta)
        except Exception as e:
            self.bot.reply_to(mensagem, f"Houve um erro ao buscar os dados.")

    def  mostrarTudoMangaBuddy(self,mensagem):
        try:
            resultado = self.db.mostarTudo('mangaBuddy')
            if resultado:
             resposta = '\n'.join([f"Nome: {linha[0]} Capítulo: {linha[1]}" for linha in resultado])
            else:
                resposta = "Nenhum resultado encontrado"
            self.bot.reply_to(mensagem, resposta)
        except Exception as e:
            self.bot.reply_to(mensagem, f"Houve um erro ao buscar os dados.")

       
    def mensagemAtualizacaoAsura(self,mensagem,nome,capitulo):
        texto = f"Novo capitulo lancado em Asura!{nome} - cap={capitulo} "
        self.bot.reply_to(mensagem,texto)


    @staticmethod
    def verificar(mensagem):
        return True

    def responder(self, mensagem):
        texto = """
        Escolha uma opção para continuar (Clique no item):
        /opcao1 para adicionar mais 
        /opcao2 para excluir
        /opcao3 pra ver lista"""
        self.bot.reply_to(mensagem, texto)

if __name__ == "__main__":
    db = Database()
    bot = TelegramBot(chaveApi)
    scraping = Scraping()
    commands = Commands(bot.bot, db,scraping)
    bot.polling()