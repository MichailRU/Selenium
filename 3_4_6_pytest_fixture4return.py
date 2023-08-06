import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture (scope='class')
# фикстура может вызываться для областей “function” (1 раз для каждой функции - по умолчанию),
# “class” (1 раз для всех функций внутри класса), “module” (1 раз для всех функций всего модуля),
# “session” (1 раз для всей сессии - нескольких модулей)
def browser():
    print('\nstart browser for test..')
    driver = webdriver.Chrome()
    yield driver
    # этот код выполнится после завершения теста
    print('\nquit browser..')
    driver.quit()


@pytest.fixture(autouse=True)
# при использовании дополнительного параметра autouse=True фикстура запустится для каждого теста
# даже без ее явного вызова и выполняется перед иными фикстурами (если они не классовые)
def prepare_data():
    print()
    print('preparing some critical data for every test')


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_should_see_login_link(self, browser):
        print('start test1')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        print('finish test1')

    def test_should_see_basket_link_on_the_main_page(self, browser):
        print('start test2')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
        print('finish test2')
