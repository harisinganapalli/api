import requests 
response=requests.get('http://127.0.0.1:8000/fruits/') 
print(response.json())
data=requests.get('http://127.0.0.1:8000/fruits/')
print(data.json())
print(data.status_code)

if data.status_code == 200:
    print('Success!')
elif data.status_code == 404:
    print('Not Found.')

print(data.content)  
print(data.text)  
print(data.headers)


### httpie,curl 