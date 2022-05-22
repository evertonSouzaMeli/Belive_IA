import speech_recognition as sr


def microphone():
    with sr.Microphone() as source:
        rec = sr.Recognizer()
        audio = rec.listen(source, timeout=3, phrase_time_limit=10)

        return rec.recognize_google(audio, language="pt-br")