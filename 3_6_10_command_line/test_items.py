# Запуск: pytest -s -v --browser_name='ff' --language='fr' test_items.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def is_present_element_on_page(browser, timeout, *locator):
    # Проверка наличия элемента на странице. Возвращает элемент по заданному локатору.
    # Если элемент отсутствует или превышено время ожидания timeout - возвращается False
    try:
        out = WebDriverWait(browser, timeout).until(EC.presence_of_element_located(*(locator)))
    except (NoSuchElementException, TimeoutException):
        out = False
    return out


def test_should_see_button_add_to_cart(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    assert is_present_element_on_page(browser, 10, (By.CSS_SELECTOR, '.btn-add-to-basket')), 'Ошибка - Не найден элемент'
