from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.CSS_SELECTOR, '.form-control')
    field.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
