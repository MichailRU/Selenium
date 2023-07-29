import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

try:
    # Считываем значение из тега span: <span class ='nowrap' id='input_value'> 631 </span>
    x = browser.find_element(By.ID, 'input_value').text
    # Записывает рассчитанное значение в поле <input id='answer' class='form-control' type='text' required>
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    # Кликаем по checkbox и radiobutton
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()
