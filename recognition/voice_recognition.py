from components.date import date, welcome
from components.events import read_event, save_event
from components.speak import speak
from components.voice import microphone
from components.weather import temp
import webbrowser
from speech_recognition import WaitTimeoutError, UnknownValueError



def voiceComands():
    welcome()

    while True:
        try:
            
            if microphone().lower() == 'ok assistente':
                speak("Sim. O que devo fazer?")
            #print("O que você deseja?")
            #speak("O que você deseja?")

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
                
            elif desire == 'sintomas da gripe':
                webbrowser.open("sintomas da gripe")
                speak("Aqui estão alguns resultados para os sintomas da gripe")

            elif desire == 'ligar para pronto socorro':
                webbrowser.open("pronto socorro hospitais")
                speak("Aqui estão alguns números de hospitais que você pode ligar para emergência, mas é recomendado que ligue para o Samú. Disque 1,9,2 ")

            elif desire == 'me diga como está o tempo hoje':
                print(temp())
                speak(temp())

            elif desire == 'quero escutar uma música relaxante':
                webbrowser.open("https://www.youtube.com/watch?v=Ncbm0Bqk1lk")
                print("Aqui está uma música ótima para que vc possa relaxar")
                speak("Aqui está uma música ótima para que vc possa relaxar")

            elif desire == 'acessar site de consulta':
                webbrowser.open("drconsulta.com")
                print("Dr consulta acessado.")
                speak("Dr consulta acessado.")

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


