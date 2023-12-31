from selenium import webdriver
import pytest
import logging

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    #return driver---stores a value permanetly
    yield driver  # it executes and retun valies only when function is called

# If we are using selenium>4 no need to provide webdriver path.Itautomaticallytakes

def test_open_url_verify_title(driver):
    LOGGER=logging.getLogger(__name__)
    driver.get("https://app.vwo.com/#/login")
    assert "Login - VWO"==driver.title
    LOGGER.info("This is info")
