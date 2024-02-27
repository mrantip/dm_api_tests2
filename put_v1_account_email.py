import requests
import json

url = "http://5.63.153.31:5051/v1/account/email"

payload = json.dumps({
  "login": "eu dolor veniam labore",
  "password": "ut consequat dolore dolore",
  "email": "fugiat consequat aute"
})
headers = {
  'X-Dm-Auth-Token': 'aliquip labore in ipsum',
  'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
