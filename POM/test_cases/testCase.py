import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM.obj_page.objPage import Page
import yaml
from ddt import ddt, data, unpack


def load_yaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        try:
            datas = yaml.safe_load(f)
            print("yaml", datas)
            return datas
        except yaml.YAMLError as ex:
            print(ex)


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

    @data(*load_yaml("../case_data/case.yaml"))
    @unpack  # 在“脱外套”之后，针对你拿到的每一条数据根据逗号进行拆分
    def test_case(self, text, except_value):
        self.page.test(text)
        print(self.page.getTitle())
        self.assertEqual(self.page.getTitle(), except_value)

    def tearDown(self):
        self.page.quit()


if __name__ == '__main__':
    unittest.main()
