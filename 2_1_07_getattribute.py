'''
Чтобы узнать значение атрибута элемента используется метод get_attribute()
Возможные возвращаемые значения:
  значение атрибута - если атрибут присутствует в элементе
  None - если атрибута нет
  'true' - если атрибут присутствует, но у него значение не указано явно (например, checked)
  'false' - если атрибут в элементе указан без значения (например, checked='')
'''

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

try:
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()
