from selenium import webdriver

browser = webdriver.Chrome()
assert "Should be absolute value of a number", not abs(-42) != -42