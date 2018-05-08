from bs4 import BeautifulSoup
import time 

'''
def combat_gain(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'  
        kv = {'user-agent' :user_agent}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        content = r.text
        soup = BeautifulSoup(content,"lxml")
        left_team = soup.find('li',{'class':'team-left'}).find('span').string
        right_team = soup.find('li',{'class':'team-right tr'}).find('span').string
        print(left_team + ':' + right_team+'='+soup.p.string)
        time.sleep(5)
    except:
        print("爬去失败")
    
def main():
    for i in range(38798,39476):
        url = 'http://www.wanplus.com/schedule/'+str(i)+'.html'
        combat_gain(url)
        
main()
'''
with open('C:/Users/Administrator/Desktop/xx.html', 'r') as f: 
    content = f.read()
    with open('C:/Users/Administrator/Desktop/combat_gain.txt','w',encoding = 'utf-8') as fl:
    
    
        soup = BeautifulSoup(content,"lxml")
        for item in soup.find_all("div",{"class":"war"}):
            try:
                try:
                    left_team = item.find("div",{"class":"team"}).find('div',{'class':'teamname'}).string
                    right_team = item.find("div",{"class":"team t2"}).find('div',{'class':'teamname'}).string
                    left_num = item.find("div",{"class":"team"}).find('div',{'class':'teamcode'}).string
                    right_num = item.find("div",{"class":"team t2"}).find('div',{'class':'teamcode cred'}).string
                    print(left_team + ":"+ right_team + "=" + left_num + ":" + right_num)
                    fl.write("{} : {} = {} : {}\n".format(left_team,right_team,left_num, right_num))
                except:
                    left_team = item.find("div",{"class":"team"}).find('div',{'class':'teamname'}).string
                    right_team = item.find("div",{"class":"team t2"}).find('div',{'class':'teamname'}).string
                    left_num = item.find("div",{"class":"team"}).find('div',{'class':'teamcode cred'}).string
                    right_num = item.find("div",{"class":"team t2"}).find('div',{'class':'teamcode'}).string
                    print(left_team + ":"+ right_team + "=" + left_num + ":" + right_num)
            except:
                print('爬取实拍')
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        