from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


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
            time.sleep(2)
            
            list_of_dic = {'title': [], 'size': [],'all_details':[],'up_vote':[]}  # Initialize the dictionary

            while initial_page < last_page:  
                # i = i + 1
                initial_page=initial_page + 1 
                driver.get(self.url + f'/datasets?page={initial_page}')
                time.sleep(2)
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


class DataDotGov:
    def web_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--verbose")
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--window-size=1920,1200")
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        return driver
    def data_set_page(self, url, last_page, initial_page):
        try:
            driver = self.web_driver_chrome()
            self.url = url
            time.sleep(1)
            list_of_datasets = {'title': [], 'author': [], 'recent_views': []}
            while initial_page <= last_page:
                driver.get(self.url + f'/dataset?page={initial_page}')
                time.sleep(2)
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
