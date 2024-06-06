from selenium import webdriver
from time import sleep


def test_one():
    driver = webdriver.Chrome()
    driver.get("https:www.fb.com")
    sleep(3)
    driver.quit

def test_two():
    driver = webdriver.Chrome()
    driver.get("https:www.instagram.com")
    sleep(3)
    driver.quit

def test_three():
    driver = webdriver.Chrome()
    driver.get("https:www.yatra.com")
    sleep(3)
    driver.quit

