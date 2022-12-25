from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service("C:/Users/saura/Desktop/chrome driver/chromedriver.exe")
var=webdriver.Chrome(service=s)
var.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
var1=var.find_element_by_name("username").send_keys("saurabh")
var.close()
