import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(
        service=ChromeService(executable_path="/home/dmitrii/Документы/workspace/YaSel/chromedriver/chromedriver"))
    browser.get(link)

    button = browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()