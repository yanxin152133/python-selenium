from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

# chrome-test路径
chrome_testing_path = r"D:\chrome-test\chrome-win64\chrome.exe"

# chromedriver
chromedriver_path = r"D:\chrome-test\chromedriver-win64\chromedriver.exe"

# 设置chrome选项
options = webdriver.ChromeOptions()
options.binary_location = chrome_testing_path
options.add_experimental_option('detach', True)

# 设置webdriver服务
service = Service(chromedriver_path)


def main():
    driver = webdriver.Chrome(service=service, options=options)
    # 导航
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # 请求浏览器信息
    title = driver.title
    print(title)

    # 显式等待
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "my-text-id"))
        )
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
