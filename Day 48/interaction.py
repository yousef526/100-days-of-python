from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_driver = "C:\Devoplment_selenium\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
service = webdriver.EdgeService(executable_path=edge_driver)
driver = webdriver.Edge(options=options,service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

fname = driver.find_element(By.NAME,"fName")
fname.send_keys("Ahmed")

lname = driver.find_element(By.NAME,"lName")
lname.send_keys("Ahmed")

email = driver.find_element(By.NAME,"email")
email.send_keys("Ahmed@asd.com")

signUp = driver.find_element(By.XPATH,"/html/body/form/button")
signUp.click()

#driver.close()






"""
Work on wikipedia items
 #btn = driver.find_element(By.XPATH,"//*[@id='articlecount']/a[1]")
#btn = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
#print(btn.text)
#btn.click()

#portals = driver.find_element(By.LINK_TEXT,"encyclopedia")
#portals.click()

search = driver.find_element(By.NAME,"search")
search.send_keys("Hello")
search.send_keys(Keys.ENTER)
#driver.close() """