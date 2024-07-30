import requests

url = "http://127.0.0.1:5000/users/12"
json = {"user_name": "Witty"}

# test POST
print(requests.post(url, json=json).text)

# test GET
# print(requests.get(url).text)

# test PUT
# json["user_name"] = "Clooney"
# print(requests.put(url, json=json).text)

# test GET
# print(requests.get(url).text)

# test DELETE
# print(requests.delete(url).text)