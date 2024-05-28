import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v122 import page

from POM.obj_page.objPage import Page
from ddt import ddt, file_data


@ddt
class TestStringMethods(unittest.TestCase):

    def setUp(self):
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
        self.driver = webdriver.Chrome(service=service, options=options)
        self.page = Page(self.driver)

    @file_data("../case_data/case.yaml")
    def test_case(self, text, except_value):
        print('\n')
        print("-------测试-------")
        self.page.test(text)
        print(self.page.getTitle())
        self.assertEqual(self.page.getTitle(), except_value)

    def tearDown(self):
        self.page.quit()


if __name__ == '__main__':
    unittest.main()
