import tensorflow as tf

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# On AWS CAPTCHA test
# id="captcha_image"
# id="captchaGuess"

with webdriver.Firefox() as driver:
    # wait a bit before starting
    wait = WebDriverWait(driver, 10)
    # get a link
    driver.get("https://python.org/")

    # get element by name and pass keys to that element
    driver.find_element(By.NAME, "q").send_keys("input" + Keys.RETURN)

    # find elements on the page based on tag
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))

    # output the first result
    print(first_result.get_attribute("textContent"))

