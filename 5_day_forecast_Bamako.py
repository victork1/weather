import pyowm

API_key = '49a9e6d6041beefdc6653ae8fe9a1bb7'
owm = pyowm.OWM(API_key) 

fc = owm.daily_forecast('Bamako, ML', limit=5)
f = fc.get_forecast()

for weather in f:
      print (weather.get_reference_time('date'),weather.get_status(),weather.get_temperature())
      