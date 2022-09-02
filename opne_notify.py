import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code

while status_code == 200:
    print(f"Current Location of ISS: {response.json()['iss_position']}")
    response = requests.get("http://api.open-notify.org/iss-now.json")
    status_code = response.status_code