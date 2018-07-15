from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import pymongo
import multiprocessing 


def get_page(page):
    print(page)
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser,10)
    keyword = 'ipad'

    try:
        url = 'https://s.taobao.com/search?q='+ quote(keyword)
        browser.get(url)
        
        if page > 1:
            page_input = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            click_common = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            page_input.clear()
            page_input.send_keys(page)
            click_common.click()

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span')))
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist div.items .item')))
        html = browser.page_source
        
        return html
    except TimeoutException:
        
        get_page(page)



def parse_page(html):
    doc = pq(html)
    items = doc('.m-itemlist .items .item').items()
    for item in items:
        product = {
            'url':item.find('.title .J_ClickStat').attr('href'),
            'title':item.find('.row.row-2.title').text(),
            'price':item.find('.price ').text(),
            'deal':item.find('.deal-cnt').text(),
            'shop':item.find('.shop').text(),
            'local':item.find('.location').text()
        }
        print(product)


mongo_url = 'localhost'
mongo_db = 'ipad_list'
mongo_collection = 'ipad_product'
client = pymongo.MongoClient(mongo_url)
db = client[mongo_db]


def save_mongo(product):
    try:
        db[mongo_collection].insert(product)
        print('successful saved')
    except Exception:
        print('mongo failed save')    
    

def main(page):
    html = get_page(page)
    parse_page(html)



if __name__ == "__main__":
    #pool = multiprocessing.Pool()
    #pool.map(main,[i for i in range(20)])
    #for i in range(1,20):
    main(1)
