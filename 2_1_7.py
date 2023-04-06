from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(int(x))

    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
