# Для взаимодействия с модальными окнами alert нужно сначала переключиться на окно с alert
# alert = browser.switch_to.alert
# а затем можно прочитать текст из окна: alert_text = alert.text и в дальнейшем закрыть его.
# Существуют 3 разновидности окон alert:
# 1. классическое окно с одной кнопкой OK: закрытие окна командой alert.accept().
# 2. окна confirm - предлагает пользователю выбор согласиться с сообщением или отказаться от него
# при этом подтверждение осуществляется по команде alert.accept(), отказ - alert.dismiss().
# 3. окна prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используется
# метод send_keys(): alert.send_keys('My answer') и затем закрытие окна alert.accept().
import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    browser.find_element(By.TAG_NAME, 'button').click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
