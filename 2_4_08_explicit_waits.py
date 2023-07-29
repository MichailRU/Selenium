# В Selenium существует неявный (Implicit wait) способ ожидания, который позволяет задать ожидание
# при инициализации драйвера, чтобы применить его ко всем тестам, например: browser.implicitly_wait(5)
# Т.е. каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице
# (но проверять наличие элемента - каждые 500 мс и как только элемент будет найден, мы сразу перейдем к
# следующему шагу в тесте). Через 5 секунд будет выброшено исключение NoSuchElementException.
#
# Кроме того в Selenium WebDriver существуют явные ожидания (Explicit Waits), которые позволяют задать
# ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью expected_conditions.
# Примеры ожиданий:
# title_is, title_contains (проверка заголовка)
# presence_of_element_located, presence_of_all_elements_located (проверка, что элементы появились)
# visibility_of_element_located, invisibility_of_element_located, visibility_of (проверки видимости элементов)
# text_to_be_present_in_element, text_to_be_present_in_element_value (проверка существования определенного текста в определенном элементе)
# alert_is_present (условие существования модального окна)
# element_to_be_clickable (проверка возможности нажатия элемента)
# element_to_be_selected (определяет выбран или нет элемент)

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    # проверять в течение 12 секунд, пока текст элемента не будет равен заданному значению
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()
