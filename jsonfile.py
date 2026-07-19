import json
data = { "name": "ngnix", "status" : "running"}
print(data)
print(type(data))
text = json.dumps(data)
print(text)
print(type(text))
obj = json.loads(text)
print(obj)
print(type(obj))