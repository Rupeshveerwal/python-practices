# ErrorHandelingUsingAPIs.py

import requests

try:
    response = requests.get('http://10.224.199.198:1234')
    
    if response.status_code == 200:
        print("Success:", response.json())
    elif response.status_code == 404:
        print("Not Found!")
    else:
        print("Error:", response.status_code)
        
except requests.exceptions.ConnectionError:
    print("No Internet ")
except Exception as e:
    print("Any error:", e)