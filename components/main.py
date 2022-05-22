from date import date, welcome
from events import read_event, save_event
from music import music
from speak import speak
from voice import microphone
from weather import temp
import webbrowser
from speech_recognition import WaitTimeoutError, UnknownValueError


def main():
    welcome()

    while True:
        try:
            if microphone().lower() == 'ok sexta-feira':
                speak("Sim, mestre. O que devo fazer?")

                desire = microphone().lower()
                print(desire)

                if desire == 'criar evento':
                    speak('Qual evento devo cadastrar, mestre?')
                    save_event(microphone())
                    speak('Evento criado com sucesso')

                elif desire == 'ler agenda':
                    events = read_event().split(', ')

                    for event in events:
                        speak(event)

                elif desire == 'fale data e hora':
                    speak(date())

                elif desire == 'toque uma música':
                    music()

                elif desire == 'me diga como está o tempo hoje':
                    speak(temp())

                elif desire == 'quero escutar uma música':
                    webbrowser.open("https://www.youtube.com/watch?v=f2D2hEFnHLU")
                    speak("Vou te mostrar o que é musica de verdade, essa é do balácu bácu")

                elif desire == 'abrir youtube':
                    webbrowser.open("youtube.com")
                    speak("Youtube aberto, mestre")

                else:
                    speak('Desculpa, não entendi o que você está querendo dizer. Poderia repetir?')


        except WaitTimeoutError:
            pass

        except UnknownValueError:
            pass

        except Exception as ex:
            print(ex)
            pass

if __name__ == "__main__":
    main()