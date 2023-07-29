import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/simple_form_find_task.html')

# В переменную elements записываем список всех найденных элементов (существуют на странице)
elements = browser.find_elements(By.CLASS_NAME, 'form-control')
print(f'Количество найденных элементов {len(elements)}, тип переменной - {type(elements)}')
print(*elements, sep='\n')

# В переменную elements пытаемся записать список несуществующих элементов
elements = browser.find_elements(By.CLASS_NAME, 'not-form-control')
print(f'Количество найденных элементов {len(elements)}')
print(*elements, sep='\n')

time.sleep(10)
browser.quit()
