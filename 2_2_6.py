from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(int(x))

    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()