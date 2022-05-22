import recognition.image_recognition as ir
import recognition.voice_recognition as vr


if ir.faceRecognition(image='face_1.jpeg'):
    vr.voiceCommands()
else:
    print('Não Autorizado')
