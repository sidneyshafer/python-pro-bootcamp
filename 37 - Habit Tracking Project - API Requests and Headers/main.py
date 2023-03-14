import requests
from datetime import datetime

USERNAME = "sidneyshafer"
# you define your own token
TOKEN = "nfEi30rB2j40psn9jN15s"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_id = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ----- POST Request for creating user account ----- #
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# ----- POST Request for creating graph ----- #
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# ----- POST Request for adding a pixel to the graph ----- #
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"

today = datetime.now().strftime("%Y%m%d")
day = datetime(year=2023, month=2, day=16).strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "8.47",
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# ----- PUT Request for updating a pixel on the graph ----- #
update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{today}"

update_pixel_data = {
    "quantity": "8.2",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

# ----- DELETE Request for deleting a pixel on the graph ----- #
delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{today}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)

