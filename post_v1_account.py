import requests
import json

url = "http://5.63.153.31:5051/v1/account"

payload = json.dumps({
  "login": "naruto_2",
  "email": "naruto_2@mail.ru",
  "password": "naruto_2_11"
})
headers = {
  'X-Dm-Auth-Token': 'aliquip labore in ipsum',
  'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
