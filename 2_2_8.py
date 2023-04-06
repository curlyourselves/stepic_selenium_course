from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys('San')

    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys('Sanych')

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('test@test.com')

    sendfil = browser.find_element(By.CSS_SELECTOR, "#file")
    sendfil.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()