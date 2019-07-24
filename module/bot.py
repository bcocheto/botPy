from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from Projetos.robo.module.voz import Audio


class Bot:
    def treino(self):

        bot = ChatBot('Teste')
        # Criando um treinador para o chatbot
        trainer = ChatterBotCorpusTrainer(bot)
        # Treino baseado no corpus em Portugues
        trainer.train("chatterbot.corpus.portuguese")
        # Treino baseado no corpus de saudações em Português
        trainer.train("chatterbot.corpus.portuguese.greetings")
        # Treino baseado no corpus de conversação em Português
        trainer.train("chatterbot.corpus.portuguese.conversations")
        # # Dá boas vindas e inicia o programa
        # en.say('Olá, diga alguma coisa.')
        # en.runAndWait()
        frase = Audio.ouvir_microfone().lower()

        while frase != 'sair da conversação':

            pergunta = Audio.ouvir_microfone().lower()
            resposta = bot.get_response(pergunta)
            a = Audio()
            if float(resposta.confidence) > 0.5:
                print('Bot :' + resposta)
                Audio.cria_audio(a, resposta)

            else:
                print('Bot:', str(resposta))
                Audio.cria_audio(a, 'Ainda não sei responder esta pergunta')

