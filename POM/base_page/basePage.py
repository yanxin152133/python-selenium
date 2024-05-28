from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(driver, 1)
        self.title()

    def get(self, url):
        self.driver.get(url)

    def title(self):
        return self.driver.title

    def locator(self, locator):
        return self.driver.find_element(*locator)

    def getTitle(self):
        return self.driver.find_element(By.XPATH, '/html/head/title').get_attribute("textContent")

    def input_text(self, locator, text):
        self.locator(locator).send_keys(text)

    def click(self, locator):
        self.locator(locator).click()

    def quit(self):
        self.driver.quit()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
