import requests

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
response = requests.get(url)

print(response.status_code)
print(response.json())