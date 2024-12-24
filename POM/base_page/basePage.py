from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def get(self, url):
        self.driver.get(url)
        self.sleep(2)

    def title(self):
        return self.driver.title

    def locator(self, locator):
        return self.driver.find_element(*locator)

    def getTitle(self):
        self.sleep(2)
        return self.driver.find_element(By.XPATH, '/html/head/title').get_attribute("textContent")

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
        self.sleep(1)

    def click(self, locator):
        # 防止使用click保存进而使用send_keys
        self.driver.find_element(*locator).send_keys(Keys.ENTER)
        self.sleep(2)

    def quit(self):
        self.driver.quit()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
