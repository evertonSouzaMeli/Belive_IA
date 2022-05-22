import requests
import math
#chave para utilizar a API
API_KEY = "176b40bb0116b301c025c65f1a45fd78"

city = 'são paulo'
#link utilizado para puxar os dados da API
link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br'


def temp():
    request = requests.get(link)
    request_dic = request.json()
    description = request_dic['weather'][0]['description']
    weather = request_dic['main']['temp'] - 273.15
    return description, str(math.ceil(weather)) + 'graus celsius'