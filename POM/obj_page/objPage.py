from POM.base_page.basePage import BasePage


class Page(BasePage):
    url = "https://www.bing.com/?mkt=zh-CN"

    search = ('id', 'sb_form_q')
    submit = ('id', 'search_icon')

    def test(self, text):
        self.sleep(2)
        self.get(self.url)
        self.sleep(2)
        self.input_text(self.search, text)
        self.click(self.submit)
        self.sleep(2)
