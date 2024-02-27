import requests

url = "http://5.63.153.31:5051/v1/account/urn:uuid:51761a6a-f495-8b8a-3332-d7364dcaf9ce"

payload = {}
headers = {
  'X-Dm-Auth-Token': 'aliquip labore in ipsum',
  'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
  'Accept': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
