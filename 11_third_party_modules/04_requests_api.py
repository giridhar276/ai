# Install first: pip install requests
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    response.raise_for_status()
    print(response.json())
except requests.RequestException as error:
    print("Request failed:", error)
