# Open the Browser
# Navigate to a URL
# Find the Email WebElement and put email id = “abc@gmail.com”
# Find the Password input box and enter the password = 123
# Click on the button - Sign in
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_login_VWO():
    driver=webdriver.Chrome()

    #To open url
    driver.get("https://app.vwo.com/#/login")

    driver.maximize_window()

    #Find Username and password field
    driver.find_element(By.ID,"login-username").send_keys("93npu2yyb0@esiix.com")

    driver.find_element(By.NAME,"password").send_keys("Wingify@123")

    driver.find_element(By.ID,"js-login-btn").click()

    time.sleep(10)
    #Verify dahsboard is loading

    assert "Dashboard" in driver.title