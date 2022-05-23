from components.speak import speak
import recognition.image_recognition as ir
import recognition.voice_recognition as vr

resp = ir.faceRecognition(image='face_2.jpeg')
if resp:
    vr.voiceComands()
else:
    speak('Rosto não identificado. Acesso negado.')
