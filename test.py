import requests

url = 'https://teachme.jp/112126/manuals/19312576'  # replace with the URL you want to access

response = requests.get(url)

if response.status_code == 200:
    print(f'Successfully accessed {url}')
else:
    print(f'Failed to access {url} with status code {response.status_code}')
