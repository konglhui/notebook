import requests
url = 'https://toutiao.com/a6576439451487044104/'
headers = {

'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

response = requests.get(url,headers = headers)
print(response.text)



