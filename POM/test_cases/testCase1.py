import sys

import pytest
from ddt import unpack, data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM.obj_page.objPage import Page
from POM.test_cases.testCase import load_yaml


class TestMethods():
    def setup_method(self, method):
        global chrome_testing_path, chromedriver_path

        if sys.platform.startswith('linux'):
            print("当前系统是Linux")
        elif sys.platform.startswith('win32'):
            print("当前系统是Windows")
            # chrome-test路径
            chrome_testing_path = r'D:\chrome-for-test\chrome-win64\chrome.exe'

            # chromedriver/
            chromedriver_path = r'D:\chrome-for-test\chromedriver-win64\chromedriver.exe'
        elif sys.platform.startswith('darwin'):
            print("当前系统是macOS")
            # chrome-test路径
            # Mac提示“Google Chrome for Testing.app”已损坏，无法打开。 你应该将它移到废纸篓。
            # 终端输入命令 xattr -c （拖动应用程序到终端）
            # 参考链接 https://github.com/ayangweb/BongoCat/issues/69
            # Google Chrome for Testing.app需要拉入到应用程序里
            chrome_testing_path = r'/Applications/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'

            # chromedriver/
            chromedriver_path = r'/Users/yxc/chrome-for-test/chromedriver-mac-arm64/chromedriver'
        else:
            print("当前系统是其他操作系统")

        print("chrome for testing路径已设置为：", chrome_testing_path)
        print("chrome driver路径已设置为：", chromedriver_path)

        # 设置chrome选项
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_testing_path
        options.add_experimental_option('detach', True)

        # 设置webdriver服务
        service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.page = Page(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    @data(*load_yaml("../case_data/case.yaml"))
    @unpack  # 在“脱外套”之后，针对你拿到的每一条数据根据逗号进行拆分
    def test_case_1(self, text, except_value):
        print("test_case_1")
        self.page.test(text)
        print(self.page.getTitle())
        self.assertEqual(self.page.getTitle(), except_value)


if __name__ == '__main__':
    pytest.main()
