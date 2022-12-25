import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

#from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service_log_path = os.devnull)
driver.set_window_position(0, 70)
driver.implicitly_wait(2)

driver.get('https://klik-test.ru/schetchik-klikov')

a = driver.find_element(by=By.CLASS_NAME, value='btn-left')
while True:
    time.sleep(1)
    a.click()



os.system('cls')
