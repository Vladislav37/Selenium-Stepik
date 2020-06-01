import selenium
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = selenium.webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")


    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()
    input3 = browser.find_element_by_id('robotsRule')
    input3.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
