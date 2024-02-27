import requests
import json

url = "http://5.63.153.31:5051/v1/account/password"

payload = json.dumps({
  "login": "eiusmo",
  "token": "urn:uuid:b822a57b-067b-9f63-59ad-0663a5e0486e",
  "oldPassword": "est consectetur",
  "newPassword": "officia aliquip id ut"
})
headers = {
  'X-Dm-Auth-Token': 'aliquip labore in ipsum',
  'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
