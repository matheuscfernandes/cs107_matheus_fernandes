import numpy as np
from collections import Counter

class Markov:
    def __init__(self,day_zero_weather=None,number_of_days=10): # You will need to modify this header line later in Part C
        self.types={'sunny':0,'cloudy':1,'rainy':2,'snowy':3,'windy':4,'hailing':5}
        try:
            if day_zero_weather != None:
                self.types[day_zero_weather]
        except:
            raise ValueError(f'{day_zero_weather} does not exist in database.') 

        self.data = self.load_data()
        self.current_weather=day_zero_weather
        self.number_of_days=number_of_days

    def __iter__(self):
        return MarkovIterator(self)

    def load_data(self, file_path='./weather.csv'):
        return np.genfromtxt(file_path,delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather): 
        current_day_weather=current_day_weather.lower()
        next_day_weather=next_day_weather.lower()

        try:
            self.types[current_day_weather]
        except:
            raise ValueError(f'{current_day_weather} does not exist in database.') 
        try:
            self.types[next_day_weather]
        except:
            raise ValueError(f'{next_day_weather} does not exist in database.') 
        
        return self.data[self.types[current_day_weather],self.types[next_day_weather]]

    def get_weather_for_day(self, day):
        self.number_of_days = day      
        self.day_number = 0
        for day in self:
            future_day = day
        return future_day

    def _simulate_weather_for_day(self,day,trials=100):
        if day <0:
            raise ValueError(f'Argument Day:{day} is not greater than 0.')
        elif day ==0:
            return self.current_weather
        else:
            list_of_trials=[]
            for it in range(trials):
               list_of_trials.append(self.get_weather_for_day(day))
            return dict(Counter(list_of_trials))
      

class MarkovIterator:
    def __init__(self,mark):
        self.current_weather=mark.current_weather
        self.number_of_days=mark.number_of_days
        self.day_types=list(mark.types.keys())
        self.mark=mark
        self.day_number=0

    def __iter__(self):
        return self

    def __next__(self):
        day = self.current_weather
        if self.day_number > self.number_of_days:
            raise StopIteration()
        self.day_number += 1
        probabilities=[self.mark.get_prob(day, ii) for ii in self.day_types]
        next_day = np.random.choice(self.day_types, 1, p=probabilities)
        self.day = next_day[0]
        return next_day[0]




if __name__ == "__main__":
    print('-----------Part A DEMO------------')

    weather_today = Markov()
    weather_today.load_data(file_path='./weather.csv')
    print(weather_today.get_prob('sunny', 'cloudy')) # This line should print 0.3


    print('-----------Part B DEMO------------')

    weather_today = Markov(day_zero_weather='sunny')

    for i in weather_today:
        print(i)

    print('-----------Part C DEMO------------')
    weather = Markov(day_zero_weather='cloudy')
    print(weather._simulate_weather_for_day(5))




