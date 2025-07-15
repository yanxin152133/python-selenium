import sys

import pytest
import yaml
from ddt import unpack, data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM.obj_page.objPage import Page


def load_yaml(yaml_file):
    with open(yaml_file, encoding='utf-8') as f:
        try:
            datas = yaml.load(f, Loader=yaml.FullLoader)
            print("yaml", datas)
            return datas
        except yaml.YAMLError as ex:
            print(ex)


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

    # 测试输出测试用例yaml文件
    @pytest.mark.parametrize("castle", load_yaml("../case_data/case.yaml"))
    def test_case_1(self, castle):
        print("测试用例：", castle)


if __name__ == '__main__':
    pytest.main()
