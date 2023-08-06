'''
PyTest: правила запуска тестов
1. Если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт
   поиск в текущей директории.
2. Как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов.
3. Дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории
   3.1. во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py
   (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py).
   3.2. внутри всех этих файлов находит тестовые функции по следующему правилу:
   - все тесты, название которых начинается с test, которые находятся вне классов.
   - все тесты, название которых начинается с test внутри классов, имя которых начинается с Test
     (и без метода __init__ внутри класса).
4. Формат запуска тестов:
   pytest -s test_user_interface.py    # найти и выполнить все тесты в файле, параметр s - вывод команд print()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'http://selenium1py.pythonanywhere.com/'

class TestMainPage1():
    # для всех тестов класса классовые методы setup_class и teardown_class запускаются 1 раз
    @classmethod
    def setup_class(self):
        print('\nstart browser for test suite 1..')
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print('quit browser for test suite 1..')
        self.browser.quit()

    def test_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

class TestMainPage2():
    # методы setup_method и teardown_method запускаются для каждой функции класса
    def setup_method(self):
        print('start browser for test 2..')
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print('quit browser for test 2..')
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
