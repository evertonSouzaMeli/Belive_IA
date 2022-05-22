import pyttsx3 as tts


def speak(msg):
    bot = tts.init()
    bot.setProperty('voice', b'brasil')
    bot.say(msg)
    bot.runAndWait()