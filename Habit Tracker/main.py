import requests
from datetime import datetime

USERNAME = "abcd"
TOKEN = "abcdefgh"

pixela_endpoints = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoints, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixel_endpoint}/20210226"

new_pixel_data = {
    "quantity": "7"
}
# response = requests.put(url=update_pixel_endpoint,json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = update_pixel_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response)
