from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# chrome-test路径
chrome_testing_path = r"D:\chrome-test\chrome-win64\chrome.exe"

# chromedriver/
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

    # 元素定位（ID）
    element_id = driver.find_element(by=By.ID, value="my-text-id")
    element_id.send_keys("python-selenium-find_element根据ID查询元素")
    print(element_id.get_attribute("value"))
    time.sleep(5)

    # 元素定位（CLASS_NAME）
    element_CLASS_NAME = driver.find_element(by=By.CLASS_NAME, value="form-control")
    element_CLASS_NAME.send_keys("python-selenium-find_element根据CLASS_NAME查询元素")
    print(element_CLASS_NAME.get_attribute("value"))
    time.sleep(5)

    # 元素定位（TAG_NAME）
    # Get element with tag name 'div'
    element = driver.find_element(By.TAG_NAME, 'div')
    # Get all the elements available with tag name 'p'
    elements = element.find_elements(By.TAG_NAME, 'label')
    for e in elements:
        print(e.text)
        print(element_CLASS_NAME.get_attribute("value"))

    # 元素定位（NAME）
    elment_NAME = driver.find_element(By.NAME, "my-textarea")
    elment_NAME.send_keys("python-selenium-find_element根据NAME查询元素")
    print(elment_NAME.get_attribute("value"))
    time.sleep(5)

    # 元素定位（CSS）
    element_div = driver.find_element(By.TAG_NAME, value="div")
    element_CSSS = element_div.find_elements(By.CSS_SELECTOR, value='input[type="password"]')
    for element_CSS in element_CSSS:
        element_CSS.clear()
        element_CSS.send_keys("123")
    time.sleep(10)

    # 元素定位（link_text）
    element_LINK_TEXT = driver.find_element(By.LINK_TEXT, "Return to index")
    element_LINK_TEXT.click()
    driver.quit()


if __name__ == '__main__':
    main()
