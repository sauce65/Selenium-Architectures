from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.base import BasePage


class WikiPage(BasePage):
    # URL
    url = "https://www.wikipedia.org/"
    # Elements
    logo = (By.CSS_SELECTOR, 'form[id="search-form"]')
    search_bar = (By.CSS_SELECTOR, 'input[id="searchInput"]')
    search_button = (By.CSS_SELECTOR, 'button[class="pure-button pure-button-primary-progressive"]')
    results = (By.CSS_SELECTOR, 'h1[id="section_0"]')

    # Methods
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_to_load(self):
        self.wait_for_element_to_be_visible(self.logo)
        self.wait_for_element_to_be_visible(self.search_bar)

    def search_for_string(self, string):
        search_bar = self.driver.find_element(*self.search_bar)
        search_bar.send_keys(string)
        search_bar.send_keys(Keys.ENTER)

    def assert_title_equals(self, title_string):
        self.wait_for_element_to_be_visible(self.results)
        assert self.driver.title == title_string
