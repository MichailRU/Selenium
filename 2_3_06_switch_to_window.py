# WebDriver может работать только с одной вкладкой браузера, а при открытии новой вкладки WebDriver
# продолжит работать со старой вкладкой. Для переключения на новую вкладку надо явно указать, на
# какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:
# browser.switch_to.window(window_name)
#
# Чтобы узнать имя новой вкладки, используется метод window_handles, который возвращает массив
# имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]
#
# Также можно запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]
# После переключения на новую вкладку поиск элементов и клик по ним будут работать уже на новой странице

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
