import requests

USERNAME = "bryansandoval"
TOKEN = "demopassword"
ENDPOINT = "https://pixe.la/v1/users"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=ENDPOINT, json=PIXELA_PARAMS)
# print(response.text)

GRAPH_ENDPOINT = f"{ENDPOINT}/{USERNAME}/graphs/graph1"

GRAPH_CONFIG = {
    "id": "graph1",
    "name": "100Days of Python",
    "type": "float",
    "unit": "Hours",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
# UPDATING GRAPH
# response = requests.put(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=headers)

PIXEL_CONFIG = {
    "date": "20220415",
    "quantity": "2"
}
response = requests.post(url=GRAPH_ENDPOINT, json=PIXEL_CONFIG, headers=headers)
print(response.text)