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

# Example code to extract job details from indeed 
# You get the details in the form of a dictionary
There are three arguments in indeed_jobs method 
First: Url
Second: last page that you want to scrap the data
query: what job do you want to scrap

```
import indeed as in
dictionary=in()
data = indeed('https://ie.indeed.com', 40, 'data scientist')
```


# IMDb Class

The IMDb class enables scraping of comments from IMDb movie pages.

## Methods

### web_driver_chrome()

```python
def web_driver_chrome(self) -> webdriver.Chrome:
    """
    Initializes and returns a Selenium Chrome WebDriver with customized options for scraping IMDb comments.

    Returns:
        webdriver.Chrome: The Chrome WebDriver object.
    """
```

### comments(url: str) -> List[str]

```python
def comments(self, url: str) -> List[str]:
    """
    Scrapes comments from an IMDb movie page.

    Args:
        url (str): The URL of the IMDb movie page.

    Returns:
        List[str]: A list containing the scraped comments.
    """
```

## Example Code

Here's an example code demonstrating how to use the IMDb class to scrape comments from an IMDb movie page:

```python
import scrapset as m

df = m.imdb()
data = df.comments('https://www.imdb.com/title/tt0111161/reviews')
```

Please note that you should replace the URL `'https://www.imdb.com/title/tt0111161/reviews'` with the IMDb movie page URL you want to scrape comments from. 

Sure! Let's continue with the documentation for the `VesselFinder` class:

# VesselFinder Class

The VesselFinder class facilitates scraping vessel details and locations.

## Methods

### vessel_details(url: str) -> List[str]

```python
def vessel_details(self, url: str) -> List[str]:
    """
    Scrapes vessel details from VesselFinder.

    Args:
        url (str): The URL of the VesselFinder vessel page.

    Returns:
        List[str]: A list containing the scraped vessel details.
    """
```

### vessel_location(url: str) -> List[str]

```python
def vessel_location(self, url: str) -> List[str]:
    """
    Scrapes vessel locations from VesselFinder.

    Args:
        url (str): The URL of the VesselFinder port page.

    Returns:
        List[str]: A list containing the scraped vessel locations.
    """
```

## Example Code

Here's an example code demonstrating how to use the VesselFinder class to scrape vessel details and locations:

```python
import scrapset as m

df = m.VesselFinder()

# Scrape vessel details
vessel_details = df.vessel_details('https://www.vesselfinder.com/vessels')

# Scrape vessel locations
vessel_location = df.vessel_location('https://www.vesselfinder.com/ports')
```

Please replace the URLs `'https://www.vesselfinder.com/vessels'` and `'https://www.vesselfinder.com/ports'` with the specific VesselFinder pages you want to scrape vessel details and locations from. 
```python
import scrapset as m
import pandas as pd

# Scrape Kaggle dataset information
kaggle_df = m.KaggleDataSet()
kaggle_data = kaggle_df.data_set_page('https://kaggle.com', last_page=10, initial_page=5)
kaggle_datf = pd.DataFrame(kaggle_data)
kaggle_datf.to_csv('kaggle.csv', index=False)

# Scrape Data.gov dataset information
datagov_df = m.DataDotGov()
datagov_data = datagov_df.data_set_page('https://catalog.data.gov', last_page=10, initial_page=5)
datagov_datf = pd.DataFrame(datagov_data)
datagov_datf.to_csv('datagov.csv', index=False)

# Scrape job details from Indeed
indeed_df = m.indeed()
indeed_data = indeed_df.indeed_jobs('https://ie.indeed.com', 40, 'data scientist')
indeed_datf = pd.DataFrame(indeed_data)
indeed_datf.to_csv('indeed_jobs.csv', index=False)

# Scrape comments from IMDb movie page
imdb_df = m.imdb()
imdb_data = imdb_df.comments('https://www.imdb.com/title/tt0111161/reviews')

# Scrape vessel details and locations from VesselFinder
vesselfinder_df = m.VesselFinder()
vessel_details = vesselfinder_df.vessel_details('https://www.vesselfinder.com/vessels')
vessel_location = vesselfinder_df.vessel_location('https://www.vesselfinder.com/ports')
```



#  Note:  This is for running Scrapset in google colab : 

```

#run this command in the cell 
!apt-get update
!apt-get install chromium  chromium-driver
!pip install selenium

```


```

%%shell

# Add debian buster
cat > /etc/apt/sources.list.d/debian.list <<'EOF'
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
EOF

# Add keys
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A

apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg

# Prefer debian repo for chromium* packages only
# Note the double-blank lines between entries
cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
Package: *
Pin: release a=eoan
Pin-Priority: 500


Package: *
Pin: origin "deb.debian.org"
Pin-Priority: 300


Package: chromium*
Pin: origin "deb.debian.org"
Pin-Priority: 700
EOF

```
