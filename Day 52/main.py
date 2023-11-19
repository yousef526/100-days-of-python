from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from instaFollower import InstaFollower

ID = "01129"
PASSCODE = "mr23"
SIMILAR_ACCOUNT = "cheps"

insta = InstaFollower()
insta.login(username=ID,passcode=PASSCODE,account=SIMILAR_ACCOUNT)

insta.find_followers()
insta.follow()
