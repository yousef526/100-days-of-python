from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import lxml
import requests
from bs4 import BeautifulSoup

## befutfiul soup part
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31",
    "Accept-Language":"en-US,en;q=0.9",
}

res = requests.get(
    "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.81123959029528%2C%22east%22%3A-122.3066434038086%2C%22south%22%3A37.739326830341%2C%22west%22%3A-122.5600155961914%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1200%2C%22max%22%3A3000%7D%2C%22price%22%3A%7B%22min%22%3A221866%2C%22max%22%3A554666%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D",
    headers=header)

soup = BeautifulSoup(res.text,"lxml")

property_info = soup.find_all(name="div",class_="StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0 bKpguY property-card-data")
#print(property_info.text)
links = []
prices = []
addresses = []
for element in property_info:
    if "zillow" in element.find('a')['href']:
        links.append(element.find('a')['href'])
    else:
        links.append("https://www.zillow.com/b"+element.find('a')['href'])
    x = element.text.split("$")
    addresses.append(x[0])
    prices.append(x[1][0:5])

print(prices,"\n",links,"\n",addresses)
## selenium part

path = "C:\Devoplment_selenium\msedgedriver.exe"
options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
services = webdriver.EdgeService(executable_path=path)

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSedz72NwYea2TodcWKocRdJePXPoY2AZkOOWLnhHugLAivV2A/viewform?usp=sf_link"
driver = webdriver.Edge(options=options,service=services)

driver.get(FORM_URL)
time.sleep(5)
for i in range(len(links)):
    #to send address
    driver.maximize_window()
    address = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.click()
    address.send_keys(addresses[i])

    #to send price
    price = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.click()
    price.send_keys(prices[i])

    #to send property link
    link = driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.click()
    link.send_keys(links[i])

    #sumbit
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    driver.close()
    driver = webdriver.Edge(options=options,service=services)
    driver.get(FORM_URL)
    time.sleep(5)
    