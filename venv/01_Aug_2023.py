from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    #return driver---stores a value permanetly
    yield driver  # it executes and retun valies only when function is called

# If we are using selenium>4 no need to provide webdriver path.Itautomaticallytakes

def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com/#/login")
    assert "Login - VWO"==driver.title
