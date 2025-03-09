import requests
import json

js = {
    "a": 8,
    "b": 4
}
# Сериализуем JSON-объект в строку
js_str = json.dumps(js)
r = requests.get(f'http://127.0.0.1:8081/getrec?data={js_str}')

print(r.text)