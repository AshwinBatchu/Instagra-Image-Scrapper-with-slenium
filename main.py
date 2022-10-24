# Ashwin's Code Instagram Image Scraper 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os 
import wget

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/ashwi/Desktop/django/pythonproject/chromedriver.exe')
driver.get("https://www.instagram.com/")

user = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name=username]")))
pass1 = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name=password]")))

user.clear()
user.send_keys("gakuro_kun")
pass1.clear()
pass1.send_keys("noob1234")

log_in = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type= 'submit']"))).click()
next_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))).click()
next_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))).click()
next_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))

next_3.clear()
keyword = "#naruto"
next_3.send_keys(keyword)
next_3.send_keys(Keys.ENTER)
time.sleep(3)
next_3.send_keys(Keys.ENTER)
next_3.send_keys(Keys.ENTER)

time.sleep(5)
images = driver.find_elements(By.TAG_NAME,'img')
print(images)
images = [image.get_attribute('src')for image in images]
print(images)

path = os.getcwd()
path = os.path.join(path, keyword[1:] + " images")

os.mkdir(path)
print(path)

count = 0
for image in images:
    save_name = os.path.join(path,keyword[1:]+str(count)+'.jpg')
    wget.download(image, save_name)
    count = count + 1

