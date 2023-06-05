# Dataset Scraper (Scrapset)



Scrapset is a Python module specifically created for web scraping data from websites like Kaggle and Data.gov. It simplifies the task of extracting dataset information such as titles, upvotes (for Kaggle), and recent views (for Data.gov).

By utilizing the Scrapset module, you can automate the retrieval of dataset details from these platforms. This can be beneficial for various purposes such as data analysis, research, or developing machine learning models. The module employs the Selenium library to interact with the websites and extract the desired data.

With Scrapset, you can quickly and easily scrape dataset information, empowering you to work with valuable data from Kaggle, Data.gov, and similar websites.


# KaggleDataSet Class
The KaggleDataSet class enables scraping of dataset information from Kaggle.

Methods:
web_driver_chrome(): Initializes and returns a Selenium Chrome WebDriver with customized options for scraping Kaggle datasets.

data_set_page(url, last_page, initial_page): Scrapes the titles, upvotes, and additional details of datasets from Kaggle. The method takes the url of the Kaggle datasets page, the last_page number to scrape up to, and the initial_page number to start scraping from. It returns a dictionary containing the scraped dataset information.


# DataDotGov Class
The DataDotGov class facilitates scraping of dataset information from Data.gov.

Methods:
web_driver_chrome(): Initializes and returns a Selenium Chrome WebDriver with customized options for scraping Data.gov datasets.

data_set_page(url, last_page, initial_page): Scrapes the titles, recent views, and authors of datasets from Data.gov. The method takes the url of the Data.gov datasets page, the last_page number to scrape up to, and the initial_page number to start scraping from. It returns a dictionary containing the scraped dataset information.

# Example code to extract titles of datasets from Data.gov


```

import kaggle_datasets as m
import pandas as pd
df=m.DataDotGov()
data=df.data_set_page('https://catalog.data.gov',last_page=10,initial_page=5)
datf=pd.DataFrame(data)
datf.to_csv('datagov.csv',index=False)

```

# Example code to extract titles, upvote, Usability index  of datasets from kaggle


```

import kaggle_datasets as m
import pandas as pd
df=m.KaggleDataSet()
data=df.data_set_page('https://kaggle.com',last_page=10,initial_page=5)
datf=pd.DataFrame(data)
datf.to_csv('kaggle.csv',index=False)


```