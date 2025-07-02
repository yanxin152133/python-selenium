from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chromedriver路径设置
service = Service(executable_path='/Users/yxc/chrome-for-test/chromedriver-mac-arm64/chromedriver')
options = webdriver.ChromeOptions()
# 启动的浏览器路径设置（Mac M1）要具体到软件包内的可执行文件
options.binary_location = '/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'


def main():
    driver = webdriver.Chrome(service=service, options=options)
    # 导航
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # 请求浏览器信息
    title = driver.title
    print(title)
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()