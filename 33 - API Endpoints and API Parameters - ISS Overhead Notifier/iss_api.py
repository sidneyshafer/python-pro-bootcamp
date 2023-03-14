# requests documentation: https://docs.python-requests.org/en/latest/
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code) --> returns 200 = successful

# if response.status_code == 404:
#     raise Exception("404 Error: that resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("401 Error: you are not authorised to access this data.")

response.raise_for_status()

# get JSON data
data = response.json()
timestamp = data["timestamp"]
iss_position = response.json()["iss_position"]
longitude = iss_position["longitude"]
latitude = iss_position["latitude"]

# tuple of iss position
iss = (longitude, latitude)

print(data)
print(timestamp)
print(iss_position)
print(longitude)
print(latitude)
print(iss)

