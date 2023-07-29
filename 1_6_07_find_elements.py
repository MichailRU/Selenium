import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/huge_form.html')

try:
    for element in browser.find_elements(By.TAG_NAME, 'input'):
        element.send_keys('my_text')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(10)
    browser.quit()
