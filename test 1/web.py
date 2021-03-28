import requests

url="https://httpbin.org/anything"
parameters = {
    "msg" : "welcomeuser",
    "isadmin" :1
}

def post_request_function(url, parameters):
    response = requests.post(url,params = parameters)
    print(response.text)

post_request_function(url, parameters)