from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

edge_driver = "C:\Devoplment_selenium\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
service = webdriver.EdgeService(executable_path=edge_driver)
driver = webdriver.Edge(options=options,service=service)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(url=URL)

cookie = driver.find_element(By.ID,"cookie")
money = int(driver.find_element(By.ID,"money").text)

#helpers in cookie buying
store = driver.find_element(By.ID,"store").find_elements(By.TAG_NAME,"div")
store[1].text.split("\n")[0].split("-")[1].strip(" ").replace(",","")



timeout = time.time() + 60*5   # 5 minutes from now
time_to_click = time.time() + 5
while True:
    cookie.click()
    if time.time() > time_to_click:
        store = {}
        store[int(driver.find_element(By.ID,"buyCursor").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyCursor")
        store[int(driver.find_element(By.ID,"buyGrandma").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyGrandma")
        store[int(driver.find_element(By.ID,"buyFactory").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyFactory")
        store[int(driver.find_element(By.ID,"buyMine").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyMine")
        store[int(driver.find_element(By.ID,"buyShipment").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyShipment")
        store[int(driver.find_element(By.ID,"buyAlchemy lab").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyAlchemy lab")
        store[int(driver.find_element(By.ID,"buyPortal").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyPortal")
        store[int(driver.find_element(By.ID,"buyTime machine").text.split("\n")[0].split("-")[1].strip(" ").replace(",",""))] = driver.find_element(By.ID,"buyTime machine")
        max_no = min(store.keys())
        
        for key in store:
            if key >= max_no and store[key].get_attribute("class") != "grayed":
                max_no = key

        try:
            store[max_no].click()
        except:
            pass
        time_to_click = time.time() + 5
    
    if time.time() > timeout:
        break

    
print(driver.find_element(By.ID,"cps").text)
