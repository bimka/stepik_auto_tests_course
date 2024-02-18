import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(
        service=ChromeService(executable_path="/home/dmitrii/Документы/workspace/YaSel/chromedriver/chromedriver"))
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    val = int(num1) + int(num2)
    print(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(val))


    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
