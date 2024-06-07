import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

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
    driver.get('file:///D:/github/python-selenium/%E8%AD%A6%E5%91%8A%E6%A1%86/test.html')

    print("Alerts 警告框")
    element = driver.find_element(By.ID, "alertButton")
    element.click()

    wait = WebDriverWait(driver, timeout=2)
    alert = wait.until(lambda d: d.switch_to.alert)
    text = alert.text
    print("text", text)
    alert.accept()

    print("Confirm 确认框")
    element1 = driver.find_element(By.ID, "confirmButton")
    driver.execute_script("arguments[0].click();", element1)

    wait1 = WebDriverWait(driver, timeout=2)
    alert1 = wait1.until(lambda d: d.switch_to.alert)
    text1 = alert1.text
    print("text1", text1)
    alert1.dismiss()
    alert1.accept()

    print("Prompt 提示框")
    element2 = driver.find_element(By.ID, "promptButton")
    driver.execute_script("arguments[0].click();", element2)

    wait2 = WebDriverWait(driver, timeout=2)
    alert2 = wait2.until(lambda d: d.switch_to.alert)
    alert2.send_keys("Selenium")
    time.sleep(2)
    text2 = alert2.text
    print("text2", text2)
    alert2.accept()
    time.sleep(2)
    text3 = alert2.text
    print("text3", text3)
    alert2.accept()


if __name__ == '__main__':
    main()
