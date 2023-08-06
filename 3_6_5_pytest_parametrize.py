'''
Для запуска одного и того же теста с разными входными параметрами используется декоратор @pytest.mark.parametrize().
В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений
параметра. В самом тесте декорируемой функции наш параметр тоже нужно передавать в качестве аргумента.
Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов
теста кавычки не нужны.

При запуске будет вызвана декорируемая функция столько раз какова длина списка заданного параметром.
При этом в названии каждого теста в квадратных скобках будет написан параметр, с которым он запущен.

Параметризацию можно задать не только для функции, а также для всего тестового класса, чтобы все тесты
в классе запустились с заданными параметрами. В таком случае отметка о параметризации должна быть
перед объявлением класса.
'''

import pytest, math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# фикстура инициализации браузера
@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# функция ожидания видимости элемента
def wait_element_visibility(driver, locator):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    return element


# функция ожидания кликабельности элемента
def wait_element_clickable(driver, locator):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
    return element


def test_authorization(browser):
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link)
    wait_element_visibility(browser, '#ember33').click()
    wait_element_visibility(browser, '#id_login_email').send_keys('E-MAIL')
    wait_element_visibility(browser, '#id_login_password').send_keys('PASSWORD')
    wait_element_visibility(browser, '.button_with-loader').click()


@pytest.mark.parametrize('page', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_open_page_read_feedback(browser, page):
    link = f'https://stepik.org/lesson/{page}/step/1'
    browser.get(link)
    input_field = wait_element_visibility(browser, 'textarea')
    input_field.send_keys(math.log(int(time.time())))
    wait_element_clickable(browser, '.submit-submission').click()
    answer = wait_element_visibility(browser, '.smart-hints__hint').text
    if len(browser.find_elements(By.CSS_SELECTOR, '.again-btn')) > 0:
        wait_element_clickable(browser, '.again-btn').click()
    assert answer == 'Correct!', f'Инопланетяне заменили фидбек на "{answer}"'
