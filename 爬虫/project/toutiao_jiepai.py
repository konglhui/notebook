import requests
import os
from hashlib import  md5
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from multiprocessing.pool import Pool

def get_url_page(offset):
    base_url = 'https://www.toutiao.com/search_content/?'
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':20,
        'cur_tab':1,
        'from':'search_tab'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
    

    
def parse_url_page(response):
    data = response.get('data')
    if data:
        for item in data:
            iamges_url = item.get('image_list')
            title = item.get('title')
            if iamges_url:
                for image_url in iamges_url:
                    yield{
                        'title':title,
                        'image':image_url.get('url')
                    }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        response = requests.get('http:'+new_image_url)
        if response.status_code == 200:
            file_path = '{}/{}.{}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download',file_path)
    except requests.ConnectionError:
        print('Failed to saved iamge!')


def main(offset):
    response = get_url_page(offset)
    for item in parse_url_page(response):
        save_image(item)
    
if __name__ == '__main__':
    pool = Pool()
    lst = [i*20 for i in range(20)]
    pool.map(main,lst)







