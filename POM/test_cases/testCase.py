import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM.obj_page.objPage import Page
import yaml


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # chrome-test·??
        chrome_testing_path = r"D:\chrome-for-test\chrome-win64\chrome.exe"

        # chromedriver/
        chromedriver_path = r"D:\chrome-for-test\chromedriver-win64\chromedriver.exe"

        # ????chrome???
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_testing_path
        options.add_experimental_option('detach', True)

        # ????webdriver????
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.page = Page(self.driver)

    def test_case(self):
        with open('../case_data/case.yaml', 'r', encoding='utf-8') as stream:
            try:
                data = yaml.safe_load(stream)
                print('\n')
                print("-------????-------")
                print(data)
                print("-------????-------")
                print(data['test'])

                # self.page.test(data['test'])
                # print(self.page.getTitle())
                # self.assertEqual(self.page.getTitle(), data['except_value'])
            except yaml.YAMLError as ex:
                print(ex)

    def tearDown(self):
        self.page.quit()


if __name__ == '__main__':
    unittest.main()
