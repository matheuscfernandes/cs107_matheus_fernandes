from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

city_weather_prediction={}
for city in city_weather:
    weather = Markov(day_zero_weather=city_weather[city])
    pred=weather._simulate_weather_for_day(7,trials=100)
    city_weather_prediction[city]=pred

for city in city_weather_prediction:
    print(f'{city}: {city_weather_prediction[city]}')
print('\n')
print('Most likely weather in seven days\n----------------------------------')
for city in city_weather_prediction:
    likely_weather=max(city_weather_prediction[city], key=city_weather_prediction[city].get)
    print(f'{city}: {likely_weather}')