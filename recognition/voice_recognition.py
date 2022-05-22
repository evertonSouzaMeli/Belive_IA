from components.date import date, welcome
from components.events import read_event, save_event
from components.music import music
from components.speak import speak
from components.voice import microphone
from components.weather import temp
import webbrowser
from speech_recognition import WaitTimeoutError, UnknownValueError


def voiceCommands():
    welcome()

    while True:
        try:
            print("Sim. O que devo fazer?")
            speak("Sim. O que devo fazer?")

            desire = microphone().lower()
            print(desire)

            if desire == 'criar evento':
                print('Qual evento devo cadastrar?')
                speak('Qual evento devo cadastrar?')

                save_event(microphone())
                print('Evento criado com sucesso')
                speak('Evento criado com sucesso')

            elif desire == 'ler agenda':
                events = read_event().split(', ')

                for event in events:
                    print(event)
                    speak(event)

            elif desire == 'fale data e hora':
                print(date())
                speak(date())

            elif desire == 'toque uma música':
                print("tocando music")
                music()

            elif desire == 'me diga como está o tempo hoje':
                print(temp())
                speak(temp())

            elif desire == 'quero escutar uma música':
                webbrowser.open("https://www.youtube.com/watch?v=f2D2hEFnHLU")
                print("Vou te mostrar o que é musica de verdade, essa é do balácu bácu")
                speak("Vou te mostrar o que é musica de verdade, essa é do balácu bácu")

            elif desire == 'abrir youtube':
                webbrowser.open("youtube.com")
                print("Youtube aberto.")
                speak("Youtube aberto.")

            else:
                print('Desculpa, não entendi o que você está querendo dizer. Poderia repetir?')
                speak('Desculpa, não entendi o que você está querendo dizer. Poderia repetir?')

        except WaitTimeoutError:
            pass

        except UnknownValueError:
            pass

        except Exception as ex:
            print(ex)
            pass
