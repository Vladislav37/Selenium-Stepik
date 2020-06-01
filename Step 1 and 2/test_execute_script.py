import selenium
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = selenium.webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text


    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value( str(int(x) + int(y)))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
