import requests
import os
from hashlib import  md5
from urllib.parse import urlencode
from bs4 import BeautifulSoup

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
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse
    except requests.ConnectionError:
        return None
    

def get_image_page(url):
    try:
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse
    except requests.ConnectionError:
        return None

    
def parse_url_page(jsons):
    if items = jsons.get('data'):
        for item in items:
            yield{
                'title':item.get('title'),
                'url':'article_url'
            }


def get_image_page(url):
    try:
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse
    except requests.ConnectionError:
        return None


def parse_image_page(reponse):
    soup = BeautifulSoup(reponse,'lxml')

    for item in soup.find_all(li,attrs={'class':'image-item'}):
        item.a.attrs['href']




