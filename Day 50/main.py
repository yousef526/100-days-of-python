from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "yousefalaa14.com"
PASSWORD = ""

edge_driver = "C:\Devoplment_selenium\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
service = webdriver.EdgeService(executable_path=edge_driver)
driver = webdriver.Edge(options=options,service=service)

driver.get(r"https://tinder.com")
driver.maximize_window()

logIn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
logIn.click()

time.sleep(3)
# to press login on facebookpage
driver.find_element(By.XPATH,"/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div").click()

time.sleep(3)


#login credtinals
#user name

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.NAME,"email").send_keys("01126683149")

#password
driver.find_element(By.NAME,"pass").send_keys("mrjudo123")


driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input").click()

time.sleep(4)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
driver.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]").click()

time.sleep(4)
driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
time.sleep(3)
for i in range(5):
    nope = r"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span"
    driver.find_element(By.XPATH,nope).click()
    time.sleep(2)