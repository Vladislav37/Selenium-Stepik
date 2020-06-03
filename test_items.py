import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_fint_button_on_site(browser):
    # переход на нужную страницу
    browser.get(link)

    time.sleep(30)
    # поиск кнопки добавления товара в корзину
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        "No find button on page"