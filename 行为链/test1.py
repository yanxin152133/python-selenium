from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
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
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    clickable = driver.find_element(By.ID, "clickable")

    # key_down 键盘操作-修饰键
    # perform  执行
    ActionChains(driver) \
        .click_and_hold(clickable) \
        .key_down(Keys.SHIFT) \
        .key_down("a") \
        .pause(10) \
        .perform()

    # 释放所有Actions
    ActionBuilder(driver).clear_actions()

    ActionChains(driver).key_down('a').perform()

    assert clickable.get_attribute('value')[0] == "A"
    assert clickable.get_attribute('value')[1] == "a"


if __name__ == '__main__':
    main()
