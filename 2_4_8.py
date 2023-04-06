from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    txt = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.CSS_SELECTOR, '#book')
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(int(x))

    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()