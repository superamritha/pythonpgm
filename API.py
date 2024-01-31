# import json
# import requests
#
# city_name=input("Enter the city name")
# api_key='17585b378fbce21fcb32567770ee4dcf'
# URL=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
# get_server_info=requests.get(URL)
# data=get_server_info.json()
# print(data,indent=4)
# #print(type(data))
# #weather_data = data["main"]["temp"]
# #print("weathescdr_data",weather_data)
# #pretty_data=json.dumps(data, indent=4)
# #print(pretty_data)
# #print(type(pretty_data))
#
# #pretty_data_dict = json.loads(pretty_data)
# #print(type(pretty_data_dict))
# # Now you can access the "weather" key
# #weather_data = pretty_data_dict["weather"][0]["id"]
# #print("weather_data",weather_data)