# С помощью метода execute_script можно выполнить программу, написанную на языке JavaScript,
# как часть сценария автотеста в запущенном браузере.
import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

try:
    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')

    # Скроллинг страницы вниз - прокрутка в область видимости элементов, перекрытых футером
    browser.execute_script('arguments[0].scrollIntoView(true);', answer)

    answer.send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
