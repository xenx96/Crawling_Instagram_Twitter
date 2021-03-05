from urllib.request import urlopen # 인터넷 url를 열어주는 패키지
from urllib.parse import quote_plus # 한글을 유니코드 형식으로 변환해줌
from bs4 import BeautifulSoup 
from selenium import webdriver # webdriver 가져오기
import time # 크롤링 중 시간 대기를 위한 패키지
import warnings # 경고메시지 제거 패키지
from selenium.webdriver.common.keys import Keys
import os
warnings.filterwarnings(action='ignore') # 경고 메세지 제거
os.chmod('../chromedriver', 4445)    

class InstagramCrawling() :
    
    def __init__(self):
        self.sleep_time = 1.0
        self.linkarray = []
        self.search = ""
    
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: {} Forder가 존재하지않습니다. 해당 폴더를 생성합니다.'.format(directory)


    def setSearch(self,search):
        self.search = search
        
    def setCrawling(self):
    # 인스타 그램 url 생성
        baseUrl = "https://www.instagram.com/explore/tags/"
        print(" '{}' 으로 검색 하겠습니다.".format(self.search))#검색어
        url = baseUrl + quote_plus(self.search)

        driver = webdriver.Chrome(executable_path="../chromedriver/chromedriver.exe")
        driver.get(url)
    
    def startCrawling(self):
        self.setCrawling()
        SCROLL_PAUSE_TIME = self.sleep_time #Delay Time
        reallink = self.linkarray
        
        while True:
            pageString = driver.page_source
            bsObj = BeautifulSoup(pageString, 'lxml')

            for link1 in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
                for i in range(3):
                    title = link1.select('a')[i]
                    real = title.attrs['href']
                    reallink.append(real)

            last_height = driver.execute_script('return document.body.scrollHeight')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)
                new_height = driver.execute_script("return document.body.scrollHeight")

                if new_height == last_height:
                    break
                else:
                    last_height = new_height
                    continue
                    
        self.linkarray = reallink
        
    def instCrawling(self):
        self.startCrawling()
        self.createFolder('../Text')
        reallink = self.linkarray
        num_of_data = len(reallink)

        print('총 {0}개의 데이터를 수집합니다.'.format(num_of_data))
        csvtext = []

        for i in tqdm(range(num_of_data)):

            csvtext.append([])
            req = Request("https://www.instagram.com/p"+reallink[i], headers={'User-Agent': 'Mozila/5.0'})

            webpage = urlopen(req).read()
            soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8')
            soup1 = soup.find('meta', attrs={'property':"og:description"})

            reallink1 = soup1['content']
            reallink1 = reallink1[reallink1.find("@") + 1:reallink1.find(")")]
            reallink1 = reallink1[:20]

            if reallink1 == '':
                reallink1 = "Null"
            csvtext[i].append(reallink1)

            for reallink2 in soup.find_all('meta', attrs={'property':"instapp:hashtags"}):
                hashtags = reallink2['content'].rstrip(',')
                csvtext[i].append(hashtags)

            # csv로 저장

            data = pd.DataFrame(csvtext)
            data.to_csv('../Text/instagram_{}.txt'.format(self.search), encoding='utf-8')

        driver.close()

