import requests
import json

url = 'http://127.0.0.1:5000/predict?level=Junior&lang=Java&tweets=yes&phd=yes'

response = requests.get(url)

if response.status_code == 200:
    json_object = json.loads(response.text)
    print(json_object)
    prediction = json_object["prediction"]
    print(prediction)
    