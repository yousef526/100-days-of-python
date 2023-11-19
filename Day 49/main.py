from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "yousefalaa14761@gmail.com"
PASSWORD = "7A_ruJxtNRyLvv8"

edge_driver = "C:\Devoplment_selenium\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
service = webdriver.EdgeService(executable_path=edge_driver)
driver = webdriver.Edge(options=options,service=service)

driver.get(r"https://www.linkedin.com/jobs/search/?currentJobId=3675372124&geoId=101131993&keywords=python%20developer&location=Cairo%2C%20Cairo%2C%20Egypt&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
driver.maximize_window()
time.sleep(3)
sign_in = driver.find_element(By.XPATH,"/html/body/div[4]/a[1]")
sign_in.click()

#login Creditnails

user_name = driver.find_element(By.ID,"username")
user_name.send_keys(EMAIL)

password = driver.find_element(By.ID,"password")
password.send_keys(PASSWORD)

driver.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
