import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome(
        service=ChromeService(executable_path="/home/dmitrii/Документы/workspace/YaSel/chromedriver/chromedriver"))
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    button.click()
    time.sleep(10)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


# time.sleep(5)
# title = browser.title
#
# browser.implicitly_wait(0.5)
#
# text_box = browser.find_element(by=By.NAME, value="my-text")
# submit_button = browser.find_element(by=By.CSS_SELECTOR, value="button")
#
# text_box.send_keys("Selenium")
# submit_button.click()
#
# message = browser.find_element(by=By.ID, value="message")
# text = message.text
#
# browser.quit()