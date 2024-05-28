from selenium import webdriver
import time


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
