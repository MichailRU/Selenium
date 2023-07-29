import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    # Считываем два значения из тега span и записываем в out их сумму
    out = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)

    # Инициализируем новый объект, передав в него WebElement с тегом 'select'
    select = Select(browser.find_element(By.TAG_NAME, 'select'))

    # Далее можно найти любой вариант из списка с помощью методов:
    # select_by_value('1') - найти элемент соответствующий <option value='1'>значение</option>
    # select.select_by_visible_text('значение') - найти элемент по видимому тексту
    # select.select_by_index(1) - найти элемент по его индексу или порядковому номеру (индексация начинается с нуля)
    select.select_by_visible_text(str(out))

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()
