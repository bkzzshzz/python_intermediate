import requests
import json

def request1():
    url = 'http://localhost:8001'
    payload = {'some' : 'data'}
    request_header = {'user-agent' : 'bkess browser'}
    response = requests.get(url, headers=request_header)
    print((response.content.decode('utf-8')))


if __name__ == '__main__' :
    request1() 
