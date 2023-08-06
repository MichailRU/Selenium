'''
Тест-раннеры сами находят тестовые методы в указанных при запуске файлах, но для этого нужно
общепринятым правилам: название тестового метода должно начинаться со слова 'test_'.
Дальше может идти любой текст, который является уникальным названием для теста:
Кроме того, для unittest существуют собственные дополнительные правила:
1. Обязательно импортировать библиотеку unittest.
2. Тесты обязательно должны находиться в специальном тестовом классе.
3. Вместо assert должны использоваться специальные assertion методы.
4. Строка запуска программы выглядит как: unittest.main().
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Создаем тестовый класс, который должен наследоваться от класса TestCase
class Test_Unittest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        time.sleep(5)
        self.browser.quit()

    def test_1(self):
        self.browser.get('http://suninjuly.github.io/registration1.html')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('first')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('second')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('third')
        self.browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        time.sleep(1)
        self.assertIn('Congratulations!', self.browser.find_element(By.TAG_NAME, 'h1').text, 'Error')

    def test_2(self):
        self.browser.get('http://suninjuly.github.io/registration2.html')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('first')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('second')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('third')
        self.browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        time.sleep(1)
        self.assertIn('Congratulations!', self.browser.find_element(By.TAG_NAME, 'h1').text, 'Error')

if __name__ == '__main__':
    unittest.main()
