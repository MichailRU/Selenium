import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/simple_form_find_ta_sk.html')

try:
    # Метод send_keys() заполняет форму input с type='text' указанным текстом
    browser.find_element(By.TAG_NAME, 'input').send_keys('Ivan')
    browser.find_element(By.NAME, 'last_name').send_keys('Petrov')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('Smolensk')
    browser.find_element(By.ID, 'country').send_keys('Russia')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(20)
    browser.quit()
