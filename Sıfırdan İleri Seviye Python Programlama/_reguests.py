import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos/1")
result = json.loads(result.text) 

print(result)
