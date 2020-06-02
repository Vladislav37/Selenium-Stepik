import pytest
from selenium import webdriver
import time
import math

correct = "Correct!"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_message_on_stepik_site(link, browser):
    browser.get(link)
    browser.implicitly_wait(10)

    answer = str(math.log(int(time.time())))

    input1 = browser.find_element_by_css_selector("textarea.string-quiz__textarea")
    input1.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    input2 = browser.find_element_by_css_selector("pre.smart-hints__hint")
    gettingValue = input2.text

    assert gettingValue == correct, "expected " + correct + ", but got " + gettingValue