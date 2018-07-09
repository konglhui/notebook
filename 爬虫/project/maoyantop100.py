import requests
import json
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from multiprocessing import Pool 


def get_one_page(url):
    try:
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse.text
        return None

    except RequestException:
        return None

def parse_one_page(html):
    content = []
    soup = BeautifulSoup(html,'lxml')
    for item in soup.select('div ol li '):
        name = item.find('span',attrs = {'class':'title'}).get_text()
        star = item.find('span',attrs = {'class':'rating_num'}).get_text()
        content.append([name,star])
    return content


def write_to_content(content):
    with open('douban250.txt','a',encoding = 'utf-8') as f:
        f.write(json.dumps(content,ensure_ascii = False) + '\n')
        f.close()


def main(i):
    url = 'https://movie.douban.com/top250?start='+ i + '&filter='
    html = get_one_page(url)
    print(html)
    content = parse_one_page(html)
    for item in content:
        text = item[0] + ':' + item[1]
        write_to_content(text)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[str(i*25) for i in range(10)])    
