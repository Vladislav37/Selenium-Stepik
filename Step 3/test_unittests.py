from selenium import webdriver
import unittest
import time

class TestReg(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('//input[@class="form-control first"][@required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('//input[@class="form-control second"][@required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('//input[@class="form-control third"][@required]')
        input3.send_keys("test@test.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fail test one")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath('//input[@class="form-control first"][@required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('//input[@class="form-control second"][@required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('//input[@class="form-control third"][@required]')
        input3.send_keys("test@test.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Fail test two")

if __name__ == "__main__":
    unittest.main()