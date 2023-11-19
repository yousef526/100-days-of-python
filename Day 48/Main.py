from selenium import webdriver
from selenium.webdriver.common.by import By
edge_driver = "C:\Devoplment_selenium\msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)


service = webdriver.EdgeService(executable_path=edge_driver)
driver = webdriver.Edge(options=options,service=service)
driver.maximize_window()
driver.get("https://www.python.org/")

#first sol.
""" events = driver.find_element(By.XPATH,"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul").text
x = events.split("\n")
events_dict = {}
item_number = 0
for i in range(0,len(x) - 1,2):
    event_dict = {
        "time":x[i],
        "name":x[i+1],
    }
    events_dict[item_number] = event_dict
    item_number+=1

print(events_dict) """

#another sol.
""" times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

events_dict = {}

for x in range(len(times)):
    dict22 = {
        "time":times[x].text,
        "name":names[x].text,
    }
    events_dict[x] = dict22

print(events_dict) """

driver.close()
""" #another ways to get element
(By.NAME,"q")# using name on check box
(By.CLASS_NAME,"python-logo") # using a class name                  (.document a)
(By.CSS_SELECTOR,".document a")# using CSS selector which looks for document class then an anchor tag 
and last way is using Xpath"""




#driver.close() 