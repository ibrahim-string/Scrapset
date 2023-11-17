from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import pyautogui

class KaggleDataSet:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver

    def data_set_page(self, url, last_page, initial_page):
        try:
            driver = webdriver.Chrome()
            self.url = url
            time.sleep(1)
            
            list_of_dic = {'title': [], 'size': [],'all_details':[],'up_vote':[]}  # Initialize the dictionary

            while initial_page < last_page:  
                # i = i + 1
                initial_page=initial_page + 1 
                driver.get(self.url + f'/datasets?page={initial_page}')
                time.sleep(0.5)
                titles = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div[6]/div/div/div/ul/li/div[1]/a')
                for title in titles:
                    data_set_title = title.find_element(By.XPATH, './div[2]/div').text
                    try: 
                        data_set_size = title.find_element(By.XPATH, './div[2]/span[2]/span').text
                        data_set_details=title.find_element(By.XPATH,'//*[@id="site-content"]/div[6]/div/div/div/ul/li[1]/div[1]/a/div[2]/span').text
                        data_set_upvote=title.find_element(By.XPATH,'//*[@id="site-content"]/div[6]/div/div/div/ul/li/div[1]/div/div/span').text
                    except:
                        list_of_dic['size'].append("")
                        list_of_dic['title'].append(data_set_title) 
                        list_of_dic['all_details'].append(data_set_details)
                        list_of_dic['up_vote'].append(data_set_upvote)
                        continue
                    list_of_dic['size'].append(data_set_size)
                    list_of_dic['title'].append(data_set_title)
                    list_of_dic['all_details'].append(data_set_details)
                    list_of_dic['up_vote'].append(data_set_upvote)
            driver.quit()
            return list_of_dic
        except:
            logging.error("Invalid Url")
    def kaggle_discussions(self,url,initial_page,last_page):
        try:
            self.url=url
            driver=webdriver.Chrome()
            time.sleep(1)
            list_of_dic = {'title': [],'all_details':[],'up_vote':[],'comments':[]}  # Initialize the dictionary
            while initial_page <= last_page:
                driver.get(url+f'/discussions?page={initial_page}')
                initial_page=initial_page+1
                time.sleep(3)
                threads=driver.find_elements(By.XPATH,'//*[@id="site-content"]/section[2]/div[2]/div/div/div/div/div[4]/ul/li/div[1]')
                c=0
                for thread in threads:
                    c=c+1
                    try:
                        title=thread.find_element(By.XPATH,f'//*[@id="site-content"]/section[2]/div[2]/div/div/div/div/div[4]/ul/li[{c}]/div[1]/a/div/div/div').text
                        all_details=thread.find_element(By.XPATH,f'//*[@id="site-content"]/section[2]/div[2]/div/div/div/div/div[4]/ul/li[{c}]/div[1]/a/div/span').text
                        up_votes=thread.find_element(By.XPATH,f'//*[@id="site-content"]/section[2]/div[2]/div/div/div/div/div[4]/ul/li[{c}]/div[1]/div[2]/div/div[1]/span').text
                        comments=thread.find_element(By.XPATH,f'//*[@id="site-content"]/section[2]/div[2]/div/div/div/div/div[4]/ul/li[{c}]/div[1]/div[2]/div/div[2]/span/span').text
                    except:
                        list_of_dic['comments'].append("")
                        list_of_dic['title'].append("")
                        list_of_dic['all_details'].append("")
                        list_of_dic['up_vote'].append("")
                        continue
                    list_of_dic['title'].append(title)
                    list_of_dic['all_details'].append(all_details)
                    list_of_dic['up_vote'].append(up_votes)
                    list_of_dic['comments'].append(comments)
        except:
            logging.error('Invalid error')
        driver.quit()
        return list_of_dic


class DataDotGov:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver
    def data_set_page(self, url, last_page, initial_page):
        try:
            driver = self.web_driver_chrome()
            self.url = url
            time.sleep(0.7)
            list_of_datasets = {'title': [], 'author': [], 'recent_views': []}
            while initial_page <= last_page:
                driver.get(self.url + f'/dataset?page={initial_page}')
                time.sleep(0.5)
                initial_page = initial_page + 1 
                titles = driver.find_elements(By.XPATH, '//*[@id="content"]/div[2]/div/section[1]/div[2]/ul/li')
                c=0
                for title in titles:
                    c=c+1
                    data_set_title = title.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/section[1]/div[2]/ul/li[{c}]/div/h3/a').text
                        
                    data_set_views = title.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/section[1]/div[2]/ul/li[{c}]/div/h3/span').text
                
                    data_set_author = title.find_element(By.XPATH,f'//*[@id="content"]/div[2]/div/section[1]/div[2]/ul/li[{c}]/div/div[2]/p').text
            
            
                    list_of_datasets['title'].append( data_set_title)
                    list_of_datasets['recent_views'].append( data_set_views)
                    list_of_datasets['author'].append( data_set_author)
            driver.quit()
            return list_of_datasets
        except:
            logging.error("Invalid Url")
class indeed:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver 
    def indeed_jobs(self,url,last_page,query):
        try:
            driver = self.web_driver_chrome()
            self.url=url
            time.sleep(1)
            list_of_dic = {'title': [],'all_details':[],'salary':[]}  
            initial_page=0
            while initial_page < last_page:
                time.sleep(2)
                driver.get(url + f'/jobs?q={query}'+f'&start={initial_page}')
                initial_page+=10
                cards=driver.find_elements(By.XPATH,'.//*[@id="mosaic-provider-jobcards"]/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2')
                details=driver.find_elements(By.XPATH,'.//*[@id="mosaic-provider-jobcards"]/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]')    
                salaries=driver.find_elements(By.XPATH,'.//*[@id="mosaic-provider-jobcards"]/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[3]/div/div')             
                for card in cards:
                        try:
                                list_of_dic['title'].append(card.text)
                        except:
                                list_of_dic['title'].append(" ")
                for detail in details:
                        try:
                                list_of_dic['all_details'].append(detail.text)
                        except:
                                list_of_dic['all_details'].append(" ")

                for salary in salaries:
                        try: 
                                list_of_dic['salary'].append(salary.text)
                        except:
                                list_of_dic['salary'].append(" ")
            driver.quit()
            return list_of_dic  
        except:
             logging.error("Invalid url") 
class AI:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver 
    def ai_jobs_net(self,url):
            try:
            
                driver = self.web_driver_chrome()
                self.url=url
                time.sleep(1)
                corpus=list()
                driver.get(url)
                while True:
                    cards=driver.find_elements(By.XPATH,'.//*[@id="job-list"]/li')
                    
                    try:
                        load_more_elements=driver.find_element(By.XPATH,'.//*[@id="load-more-jobs"]/a/h5')
                        for card in cards:
                            corpus.append(card.text+'<>?')
                        driver.execute_script("arguments[0].scrollIntoView();", load_more_elements)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", load_more_elements)
                        time.sleep(1)
                    except:
                        break
                    
                driver.quit()
                return corpus  
            except:
                 logging.error("Invalid url")
class imdb:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver
    def comments(self,url):
        try:
            driver = webdriver.Chrome()
            self.url=url

            driver.get(url)

            time.sleep(1)
            corpus=[]
            while True:
                try:
                    cards=driver.find_elements(By.XPATH,'//*[@id="main"]/section/div[2]/div[2]/div')
                    for card in cards:
                        corpus.append(card.text+'<>?')
                    
                    load_more_element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="load-more-trigger"]'))
                    )
                    load_more_element.click()

                    time.sleep(1)  # Adjust this delay as needed

                except:
                     break
            driver.quit()
            return corpus  
        except:
                logging.error("Invalid url")
class vesselfinder:
    def vessel_details(self,url):
        try:
            driver=webdriver.Chrome()
            c=1
            company=list()
            ship_name=list()
            built_year=list()
            gt=list()
            dwt=list()
            size=list()
            details={'Company_Name':company,'ship_name':ship_name,'built_year':built_year,'gt':gt,'dwt':dwt,'size':size}
            while c<=200:
                driver.get(url+f'/vessels?page={c}')
                time.sleep(0.8)
                cards=driver.find_elements(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr')
                for card in cards:
                    company.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr/td[1]/a/div[3]/div[1]').text)
                    ship_name.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr/td[1]/a/div[3]/div[2]').text)
                    built_year.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr/td[2]').text)
                    gt.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr/td[3]').text)
                    dwt.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr/td[4]').text)
                    size.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div/table/tbody/tr/td[5]').text)

                c=c+1
            driver.quit()
            return details
        except:
            driver.quit()
            logging.error('Invalid Url')
    def vessel_location(self,url):
        try:
            driver=webdriver.Chrome()
            c=1
            country=list()
            port_name=list()
            locode=list()
            location={'country':country,'port_name':port_name,'locode':locode}
            while c<=293:
                driver.get(url+f'/ports?page={c}')
                time.sleep(0.4)
                cards=driver.find_elements(By.XPATH,'/html/body/div[1]/div/main/div[1]/table/tbody/tr')
                for card in cards:
                    # text.append(card.text+'<>')
                    country.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div[1]/table/tbody/tr/td[1]/div/a/div[2]').text)
                    port_name.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div[1]/table/tbody/tr/td[1]/div/a/div[1]').text)
                    locode.append(card.find_element(By.XPATH,'/html/body/div[1]/div/main/div[1]/table/tbody/tr/td[2]').text)
                    
                c=c+1
            driver.quit()
            return location
        except:
            driver.quit()
            logging.error('Invalid Url')

# API for scraping g2.com
class g2:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver
    def reviews(self,page_no,search_query):
        
        driver=self.web_driver_chrome()
        
        initial_page=1
        reviews=[]
        try:
            while initial_page<=page_no:
                
                    driver.get(f'https://fatmongoose.staging.g2.com/products/{search_query}/reviews?page={initial_page}')
                    initial_page=initial_page+1
                    time.sleep(2)
                    cards=driver.find_elements(By.CLASS_NAME,'paper__bd')
                    for card in cards:
                        reviews.append(card.text)
            rv={'reviews':reviews}
            return rv
        except:
            logging.error("Invalid Url")
# Actual IP of g2.com
# fatmongoose.staging.g2.com
class Angel:
    def scroll_using_mouse(self,duration=10, scroll_amount=1):
        end_time = time.time() + duration

        while time.time() < end_time:
            pyautogui.scroll(-scroll_amount)
            time.sleep(0.1)
    def Map(self,query):
        query=query.replace(" ","+")
        
        driver=webdriver.Chrome()
        time.sleep(2)
        driver.get(f"https://www.google.com/maps/search/{query}")
        self.scroll_using_mouse(duration=60, scroll_amount=100)

        time.sleep(6)
        cards=driver.find_elements(By.CLASS_NAME,'lI9IFe ')
        company=list()
        num=list()
       
        
        for card in cards:
            try:
                company.append(card.find_element(By.CLASS_NAME,'NrDZNb').text)
            except:
                company.append(False)
            try:
                num.append(card.find_element(By.CLASS_NAME,'UsdlK').text)
            except:
                num.append(False)
        driver.quit()
        dic={'Company_Name':company,'Phone_no':num}
        return dic
