# request
# GET https://google.com?q=CERN&time=1231
# POST
# PUT
# PATCH
# DELETE
# HEAD, OPTIONS
import requests

params = {
    "latitude": 46.2,
    "longitude": 6.1,
    "hourly": "temperature_2m",
    "timezone": "Europe/Zurich"
}

response = requests.get('https://api.open-meteo.com/v1/forecast', params=params)

data = response.json()
print(data)

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

print(list(zip(times,temps)))

with open("weather.csv", "w") as file:
    import csv
    writer = csv.writer(file)

    for row in zip(times, temps):
        writer.writerow(row)

# API
# JavaScript Object Notation


# response
# StatusCode