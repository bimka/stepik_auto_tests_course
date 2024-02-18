import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def scroll_to_(field):
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(
        service=ChromeService(executable_path="/home/dmitrii/Документы/workspace/YaSel/chromedriver/chromedriver"))
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    scroll_to_(input_field)
    input_field.send_keys(y)



    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    scroll_to_(option1)
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    scroll_to_(option2)
    option2.click()


    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    scroll_to_(button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()