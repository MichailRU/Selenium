'''
Checkbox и Radiobutton создаются при помощи тега <input type='checkbox'> и <input type='radio'>
Если checkbox или radiobutton выбран, то у элемента появится новый атрибут checked без значения.
Radiobuttons объединяются в группу, где все элементы имеют одинаковые значения атрибута name,
но разные значения атрибута value:
<input type='radio' name='language' value='python' checked>
<input type='radio' name='language' value='selenium'>

Данные элементы лучше искать с помощью значения id или значения атрибута value.
Чтобы снять/поставить галочку в элементе типа checkbox или выбрать опцию из группы radiobuttons,
надо указать WebDriver метод поиска элемента и выполнить для найденного элемента метод click():
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()

Также вы можете увидеть тег label рядом с input. Этот тег используется, чтобы сделать кликабельным
текст, который отображается рядом с флажком. Этот текст заключен внутри тега label. Элемент label
связывается с элементом input с помощью атрибута for, в котором указывается значение атрибута id для элемента input:
<div>
  <input type='radio' id='python' name='language' checked>
  <label for='python'>Python</label>
</div>
<div>
  <input type='radio' id='java' name='language'>
  <label for='java'>Java</label>
</div>

В этом случае можно также отметить нужный пункт с помощью WebDriver, выполнив метод click() на элементе label.
option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
option1.click()
'''

import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By

calc = lambda x: str(log(abs(12 * sin(int(x)))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

try:
    # Считываем значение из тега span: <span class ='nowrap' id='input_value'> 631 </span>
    x = browser.find_element(By.ID, 'input_value').text
    # Записывает рассчитанное значение в поле <input id='answer' class='form-control' type='text' required>
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    # Кликаем по checkbox и radiobutton
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(5)
    browser.quit()
