from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    butt = browser.find_element(By.CSS_SELECTOR, 'button')
    butt.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(int(x))

    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()