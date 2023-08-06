'''
Чтобы разделять тесты не только по названиям, но и по каким-нибудь заданным категориям и в дальнейшем
иметь возможность запускать только маркированные тесты используются метки (marks).
Для маркировки теста нужно написать декоратор вида @pytest.mark.m_name, где m_name — произвольная строка.
Чтобы запустить тест с нужной маркировкой, передается в командной строке параметр -m и нужная метка.
Для исключения предупреждения при запуске тестов добавим файл pytest.ini, где зарегистрированы метки

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
    win10: marker for windows 10 tests

- запуск тестов с указанной маркировкой: pytest -s -v -m smoke 3_5_5_marks.py
- запуск тестов не имеющих указанную маркировку: pytest -s -v -m "not smoke" 3_5_5_marks.py
- запуск тестов с разными метками (логическое ИЛИ): pytest -s -v -m "smoke or regression" 3_5_5_marks.py
- запуск тестов имеющих несколько маркировок (логическое И): pytest -s -v -m "smoke and win10" 3_5_5_marks.py
- чтобы пропустить тест при запуске используется стандартная метка @pytest.mark.skip
- чтобы пометить тест как заведомо падающий используется стандартная метка @pytest.mark.xfail
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture (scope='function')
# фикстура может вызываться для областей “function” (1 раз для каждой функции - по умолчанию),
# “class” (1 раз для всех функций внутри класса), “module” (1 раз для всех функций всего модуля),
# “session” (1 раз для всей сессии - нескольких модулей)
def browser():
    print('\nstart browser for test..')
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser..')
    driver.quit()


class TestMainPage1():

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_see_login_link(self, browser):
        print('test1 - see_login_link')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    @pytest.mark.regression
    def test_see_basket_link_on_the_main_page(self, browser):
        print('test2 - see_basket_link_on_the_main_page')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    @pytest.mark.xfail
    def test_see_search_button_on_the_main_page(self, browser):
        print('test3 - отметка как заведомо падающего теста')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'button.favorite')


@pytest.mark.smoke
class TestMainPage2():

    def test_see_login_link(self, browser):
        print('test4 - see_login_link')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    @pytest.mark.skip
    def test_see_basket_link_on_the_main_page(self, browser):
        print('test5 - see_basket_link_on_the_main_page')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
