import requests

city=input("enter Your City -->")
Api_key = "a684abc9c4e1166da08989cfdadb417a" # Paste Your API ID Here

final_URL ="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city.Api_key)

result = requests.get(final_URL)
data = result.json()

print(data)