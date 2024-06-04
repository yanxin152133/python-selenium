from time import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# chrome-test路径
chrome_testing_path = r"D:\chrome-for-test\chrome-win64\chrome.exe"

# chromedriver/
chromedriver_path = r"D:\chrome-for-test\chromedriver-win64\chromedriver.exe"

# 设置chrome选项
options = webdriver.ChromeOptions()
options.binary_location = chrome_testing_path
options.add_experimental_option('detach', True)

# 设置webdriver服务
service = Service(chromedriver_path)


def main():
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://selenium.dev/selenium/web/mouse_interaction.html')

    start = time()

    clickable = driver.find_element(By.ID, "clickable")

    # move_to_element  鼠标移动到一个元素上
    # pause  停留
    # click_and_hold  按下鼠标左键在一个元素上(长按)
    # perform  执行
    ActionChains(driver) \
        .move_to_element(clickable) \
        .pause(1) \
        .click_and_hold() \
        .pause(1) \
        .send_keys("abc") \
        .perform()

    duration = time() - start
    print(duration)
    # assert 断言
    assert duration > 2
    assert duration < 3


if __name__ == '__main__':
    main()
