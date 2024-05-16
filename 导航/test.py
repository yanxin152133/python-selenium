from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.chrome.webdriver import WebDriver

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

    # 页面交互
    # 查找元素（ID）
    element_id = driver.find_element(by=By.ID, value="my-text-id")
    element_id.send_keys("python-selenium-find_element根据ID查询元素")
    print(element_id.get_attribute("value"))
    time.sleep(5)
    element_id.clear()

    # 查找元素（CLASS_NAME）
    element_CLASS_NAME = driver.find_element(by=By.CLASS_NAME, value="form-control")
    element_CLASS_NAME.send_keys("python-selenium-find_element根据CLASS_NAME查询元素")
    print(element_CLASS_NAME.get_attribute("value"))
    time.sleep(5)
    element_id.clear()

    # 查找元素（TAG_NAME）
    # Get element with tag name 'div'
    element = driver.find_element(By.TAG_NAME, 'div')
    # Get all the elements available with tag name 'p'
    elements = element.find_elements(By.TAG_NAME, 'label')
    for e in elements:
        print(e.text)
        print(element_CLASS_NAME.get_attribute("value"))
        time.sleep(5)
    element_id.clear()

    driver.quit()


if __name__ == '__main__':
    main()
