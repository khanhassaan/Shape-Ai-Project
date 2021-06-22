import requests
from datetime import datetime

api_key = '7fe3ee965561d4a90fb425df34f49fdb'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

file_name="weatherdata.txt"
f = open(file_name, "w")
f.truncate()
f.write("-------------------------------------------------------------")
f.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
f.write("\n-------------------------------------------------------------")
f.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
f.write("\nCurrent weather desc:"+str(weather_desc))
f.write("\nCurrent Humidity:"+str(hmdt)+'%')
f.write("\nCurrent wind speed:"+str(wind_spd)+'kmph')
f.close()
print ("Data sucessfully written into: ",file_name)