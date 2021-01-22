from urllib import request
import json

res = request.urlopen("https://foodish-api.herokuapp.com/api/")

data = res.read()
print(data)

file = json.loads(data.decode())
print(file["image"])
