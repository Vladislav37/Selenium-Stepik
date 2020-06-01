import selenium
import time
import math
from selenium.webdriver.support.ui import Select
from os import path

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = selenium.webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Иванов")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Иван")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Test@test.ru")

    current_dir = path.abspath(path.dirname("file.txt"))
    file_path = path.join(current_dir, 'file.txt')
    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
