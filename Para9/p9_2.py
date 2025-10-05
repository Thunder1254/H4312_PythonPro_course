import requests

responce = requests.get("http://httpbin.org/get")
print(responce.content)
print(responce.text)



