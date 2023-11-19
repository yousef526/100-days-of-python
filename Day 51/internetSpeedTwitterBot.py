from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


edge_driver = "C:\Devoplment_selenium\msedgedriver.exe"




class InternetSpeedTwitterBot():
    def __init__(self):
        self.options = webdriver.EdgeOptions()
        self.options.add_experimental_option("detach",True)
        self.service = webdriver.EdgeService(executable_path=edge_driver)
        self.driver = webdriver.Edge(options=self.options,service=self.service)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]").click()

        time.sleep(40)
        down = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        up = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        
        time.sleep(2)
        self.driver.close()
        return down,up
    
    def start_window(self):
        self.driver = webdriver.Edge(options=self.options,service=self.service)

    def tweet_at_provider(self,speedDown,speedUp):
        self.start_window()
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div").click()
        time.sleep(2)

        #entering username then click next
        user = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        user.send_keys("yousefail.com")
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
        time.sleep(3)

        #send user name then click next
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys("ousef_y23395")
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div").click()

        time.sleep(2)
        password = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys("!Wet")

        self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div").click()

        time.sleep(2)

        post = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        post.send_keys(
            f"Hey internet provider, why my internet speed {speedDown}down/{speedUp}up when i pay for 150down/10up")
        
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div").click()



