from selenium.webdriver.support.wait import WebDriverWait
from POM.base_page.basePage import BasePage


class Page(BasePage):
    url = "https://cn.bing.com/"

    search = ('id', 'sb_form_q')
    submit = ('id', 'search_icon')

    def test(self, text):
        self.get(self.url)
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(lambda d: self.locator(self.submit).is_displayed())
        self.input_text(self.search, text)
        self.click(self.submit)
        self.sleep(2)

