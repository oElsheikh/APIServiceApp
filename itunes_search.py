import requests
import json

url = 'https://itunes.apple.com/search?term=thor&media=movie'

response = requests.get(url)

if response.status_code == 200:
    json_object = json.loads(response.text)
    results_array = json_object['results']
    for result in results_array:
        name = result['trackName']
        print(name)