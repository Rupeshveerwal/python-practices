# import requests

# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# data = response.json()

# print("Title : ", data['title'])
# print("Body : ", data['body'])
# print("User Id : ", data["userId"])




import requests


# api = (curl http://localhost:1234/api/v1/models \  -H "Authorization: Bearer $LM_API_TOKEN")


response = requests.get("curl http://localhost:1234/api/v1/google/gemma-3-1b ")
data = response.json()


# print("Title: ", data["title"])
# print("Body: ", data['body'])
# print("UserID: ", data['userId'])
# print(data)
