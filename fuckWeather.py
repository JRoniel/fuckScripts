# FUNCIONALIDADES:
# CONSULTA DADOS METEOROLOGICOS DE UMA CIDADE INFORMADO PREVIAMENTE

import requests

# Key para acessar a API openwathermap
api_key = "API_KEY"

# Entrada com o nome da cidade
city = input("Cidade: ")
data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=pt&units=metric&APPID={api_key}"
)

# Recebendo dados
print(f"Local: {data.json().get('name')}, {data.json().get('sys').get('country')}")
print(f"Temperatura: {data.json().get('main')['temp']}°C")
print(f"Clima: {data.json().get('weather')[0].get('description')}")
print(f"Umidade: {data.json().get('main')['humidity']}%")
