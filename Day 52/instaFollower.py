from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException
path = "C:\Devoplment_selenium\msedgedriver.exe"






class InstaFollower():
    def __init__(self):
        self.options = webdriver.EdgeOptions()
        self.options.add_experimental_option("detach",True)
        self.services = webdriver.EdgeService(executable_path=path)
        

    
    
    def login(self,username,passcode,account):

        self.driver = webdriver.Edge(options=self.options,service=self.services)
        self.driver.get(r"https://www.instagram.com")
        self.driver.maximize_window()

        time.sleep(2)
        email =  self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(username)

        password =  self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(passcode)

        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
        time.sleep(7)
        self.driver.get(f"https://www.instagram.com/{account}")
        time.sleep(5)
        
        

    def find_followers(self):
        # to click on followers button
        self.driver.get(self.driver.current_url+"followers")
        time.sleep(3)
        
        scr1 = self.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

        

    def follow(self):
        buttons = self.driver.find_elements(By.CLASS_NAME,"_acan _acap _acat _aj1-]")
        for btn in buttons:
            try:
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]").click()
                time.sleep(1)
                
            
            