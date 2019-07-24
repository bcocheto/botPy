import speech_recognition as sr
import pyttsx3

i = 0


class Audio:

    # Funcao responsavel por ouvir e reconhecer a fala
    def ouvir_microfone():
        # inicia sintetizador de voz
        en = pyttsx3.init()
        en.setProperty('voice', 'brazil', )
        # Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()

        with sr.Microphone() as source:
            try:
                # Avisa ao usuario que esta pronto para ouvir
                print("Diga alguma coisa: ")
                # Chama a funcao de reducao de ruido disponivel na speech_recognition
                microfone.adjust_for_ambient_noise(source)
                # Tenta ouvir o microfone
                audio = microfone.listen(source)
                # Passa o audio para o reconhecedor de padroes do speech_recognition
                frase = microfone.recognize_google(audio, language='pt-BR')
                # Após alguns segundos, retorna a frase falada
                print("Você disse: " + frase)
                return frase
            # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
            except sr.UnknownValueError:
                en.say("Desculpe, não entendi.")
                en.runAndWait()
                print('erro')
                frase = Audio.ouvir_microfone().lower()

                return frase

    def cria_audio(self, resposta):
        en = pyttsx3.init()
        en.setProperty('voice', 'brazil', )
        en.say(resposta)
        en.runAndWait()
