from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq


base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2145291155',
    'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'X-Requested-With':' XMLHttpRequest'
}

def get_page(page):
    params = {
        'type':'uid',
        'value':'2145291155',
        'containerid':'1076032145291155',
        'page':page
    }
    url = base_url + urlencode(params)
    try :
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

if __name__ == '__main__':
    for page in range(1,15):
        json = get_page(page)
        resules = parse_page(json)
        for result in resules:
            print(result)
