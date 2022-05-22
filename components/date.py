from datetime import datetime
from components.speak import speak


def date():
    return datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


def welcome():
    hour = int(datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Bom dia!")

    elif hour >= 12 and hour < 18:
        speak("Boa tarde!")

    else:
        speak("Boa noite!")