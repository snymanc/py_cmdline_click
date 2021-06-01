import requests

# json = requests.get('http://api.openweathermap.org/data/2.5/weather?q=london&appid=c36164e51783d1af218c9b21e554625b').json()
# print(json['weather'][0]['description'])

SAMPLE_API_KEY = 'c36164e51783d1af218c9b21e554625b'

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'http://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

print(current_weather('london'))