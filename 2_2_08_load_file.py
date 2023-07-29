# Для загрузки файла на веб-странице, можно использовать уже знакомый метод send_keys.
# Для этого в качестве аргумента передается путь к файлу на диске вместо простого текста.
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('123@yandex.ru')

    # Объединяем путь к директории текущего исполняемого файла и имя файла
    name_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ff.txt')
    browser.find_element(By.ID, 'file').send_keys(name_file)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
