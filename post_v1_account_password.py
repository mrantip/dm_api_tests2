import requests
import json

url = "http://5.63.153.31:5051/v1/account/password"

payload = json.dumps({
  "login": "et aliquip esse",
  "email": "culpa Excepteur"
})
headers = {
  'X-Dm-Auth-Token': 'aliquip labore in ipsum',
  'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
