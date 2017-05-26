import pyowm


API_key = '49a9e6d6041beefdc6653ae8fe9a1bb7'
owm = pyowm.OWM(API_key) 


observation = owm.daily_forecast('Bamako, ML')
w = observation.get_weather()

 
print(w.get_temperature('celsius'))
print(w.get_rain())