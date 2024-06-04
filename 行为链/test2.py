import sys
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
    driver.get('https://www.selenium.dev/selenium/web/formPage.html')

    textinput = driver.find_element(By.ID, "email")
    cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    textinput.send_keys("email")
    # 复制粘贴
    ActionChains(driver) \
        .move_to_element(textinput) \
        .send_keys(Keys.ARROW_LEFT) \
        .key_down(Keys.SHIFT) \
        .send_keys(Keys.ARROW_UP) \
        .key_up(Keys.SHIFT) \
        .key_down(cmd_ctrl) \
        .send_keys("xvv") \
        .key_up(cmd_ctrl) \
        .perform()

    print(driver.find_element(By.ID, "email").get_attribute('value'))
    assert driver.find_element(By.ID, "email").get_attribute('value') == "emaiemail"


if __name__ == '__main__':
    main()
