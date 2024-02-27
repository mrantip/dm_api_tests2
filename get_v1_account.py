import requests

url = "http://5.63.153.31:5051/v1/account"

payload = {}
headers = {
  'X-Dm-Auth-Token': 'aliquip labore in ipsum',
  'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
  'Accept': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
