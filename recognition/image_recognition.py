import cv2


def faceRecognition(image):
    loadAlgorithm = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    imagem = cv2.imread(r'./fotos/' + image)

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    faces = loadAlgorithm.detectMultiScale(imagemCinza)

    for x, y, l, a in faces:
        imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)

        return len(imagem) > 0 if True else False
    cv2.waitKey(3000)
