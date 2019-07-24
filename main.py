import pyttsx3
from Projetos.robo.module.controller import Controlador as c
from Projetos.robo.module.voz import Audio
from Projetos.robo.module.bot import Bot

en = pyttsx3.init()
en.setProperty('voice', 'brazil', )
rate = en.getProperty('rate')
en.setProperty('rate', rate + 1)
voices = en.getProperty('voices')
en.setProperty('voice', voices[20].id)

frase = Audio.ouvir_microfone()

while frase != 'teminar o programa':

    if frase == 'que horas são':
        en.say(c.hora_atual())
        en.runAndWait()
        frase = Audio.ouvir_microfone().lower()

    elif frase == 'que dia é hoje':
        en.say(c.data_atual())
        en.runAndWait()
        frase = Audio.ouvir_microfone().lower()


    elif frase == 'tudo bem':
        en.say('tudo ótimo e com você')
        en.runAndWait()
        frase = Audio.ouvir_microfone().lower()

    elif frase == 'o que é engenharia de software':
        en.say('a profissão do futuro')
        en.runAndWait()
        frase = Audio.ouvir_microfone().lower()

    elif frase == 'como é o mercado de trabalho para essa área':
        en.say('você pode trabalhar como você quiser, com quem você quiser, onde você quiser e na hora que você quiser')
        en.runAndWait()
        frase = Audio.ouvir_microfone().lower()

    elif frase == 'repolho':
        en.say('roxo')
        en.runAndWait()
        frase = Audio.ouvir_microfone().lower()

    elif frase == 'vamos conversar':
        bot = Bot()
        Bot.treino(bot)


    else:
        frase = Audio.ouvir_microfone().lower()