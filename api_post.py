# import requests
# data = {
#     "title": "मेरा पहला post",
#     "body": "यह मेरी पहली API call है",
#     "userId": 1
# }



# response = requests.post("http://127.0.0.1:1234/api/v1/chat", json=data)




import requests
import json

data = {
    "title": "मेरा new  post",
    "body": "यह मेरी पहली API call है",
    "userId": 1
}

response = requests.post("http://127.0.0.1:1234", json = data)

response - requests.get("http://127.0.0.1:1234/sk-lm-V452lv6y:qRFUKn5KMW5FCElRVPnG/v1/google/gemma-3-1b")

data = response.json
print(data)