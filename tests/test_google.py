import pytest

from pages.google import GooglePage


class TestGoogle:
    @pytest.fixture(scope='function', autouse=True)
    def setup_test(self, web_driver):
        # Setup that gets run before every test
        self.driver = web_driver
        self.google_page = GooglePage(self.driver)

    def test_google_page_loads(self):
        self.google_page.navigate_to(self.google_page.url)
        self.google_page.wait_for_page_to_load()

    def test_google_search(self):
        self.google_page.navigate_to(self.google_page.url)
        self.google_page.wait_for_page_to_load()
        self.google_page.search_for_string('abc')
        self.google_page.assert_title_equals('abc - Google Search')
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.wiki import WikiPage
from selenium.webdriver.common.by import By
import time
search_bar = (By.CSS_SELECTOR, 'input[id="searchInput"]')

class TestWiki:
    @pytest.fixture(scope='function', autouse=True)
    def setup_test(self, web_driver):
        # Setup that gets run before every test
        self.driver = web_driver
        self.wiki_page = WikiPage(self.driver)

    def test_google_page_loads(self):
        self.wiki_page.navigate_to(self.wiki_page.url)
        self.wiki_page.wait_for_page_to_load()

    def test_wiki_search(self):
        self.wiki_page.navigate_to(self.wiki_page.url)
        self.wiki_page.wait_for_page_to_load()
        self.wiki_page.search_for_string('pizza')

    def test_links(self, web_driver):
        web_driver.get('https://en.m.wikipedia.org/wiki/Pizza')
        assert "Pizza" in web_driver.title
        listOfElements = web_driver.find_elements_by_css_selector('section > p > a')

        for i in range(len(listOfElements)):
            elem = listOfElements[i]
            assert "Pizza" in web_driver.title
            ActionChains(web_driver).move_to_element(elem).click(elem).perform()
            time.sleep(1)
            web_driver.back()
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(EC.url_matches('https://en.m.wikipedia.org/wiki/Pizza'))
            assert "Pizza" in web_driver.title
            listOfElements = web_driver.find_elements_by_css_selector('section > p > a')
