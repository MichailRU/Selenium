# Задание на уникальные селекторы
# Тест по первой ссылке должен пройти, на второй ссылке - упасть с ошибкой NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

links = ('http://suninjuly.github.io/registration1.html', 'http://suninjuly.github.io/registration2.html')
browser = webdriver.Chrome()

try:
    for link in links:
        browser.get(link)
        #        for element in browser.find_elements(By.CSS_SELECTOR, '.first_block [required]'):
        #            element.send_keys('filling')
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('first')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('second')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('third')
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        time.sleep(1)
        assert browser.find_element(By.TAG_NAME, 'h1').text == 'Congratulations! You have successfully registered!'
except NoSuchElementException:
    print(f'Ссылка {link}, ошибка NoSuchElementException')
except AssertionError:
    print(f'Ссылка {link}, ошибка AssertionError')
except Exception:
    print(f'Ссылка {link}, неизвестная ошибка')
else:
    print('Тест пройден успешно')
finally:
    time.sleep(5)
    browser.quit()
