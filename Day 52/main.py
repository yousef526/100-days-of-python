from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from instaFollower import InstaFollower

ID = "01126683149"
PASSCODE = "mrjudo123"
SIMILAR_ACCOUNT = "chefsteps"

insta = InstaFollower()
insta.login(username=ID,passcode=PASSCODE,account=SIMILAR_ACCOUNT)

insta.find_followers()
insta.follow()