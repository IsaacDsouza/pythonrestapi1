import requests

BASE = " http://127.0.0.1:5000/"

data = [{"likes":20, "name":"Tim", "views":12},
        {"likes":30, "name":"kim", "views":15},
        {"likes":40, "name":"Titt", "views":18}]

for i in range(len(data)):
    response = requests.put(BASE +"video/"+str(i),data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)


input()
response = requests.get(BASE +"video/2")
print(response.json())