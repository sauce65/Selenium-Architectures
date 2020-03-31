from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    ACCEPTABLE_LOADING_TIME = 15  # seconds

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element_to_be_present(self, element_locator, wait=ACCEPTABLE_LOADING_TIME):
        try:
            WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(element_locator))
        except TimeoutException:
            raise Exception(f'Element with locator: {element_locator} was not in the DOM after {wait} seconds')

    def wait_for_element_to_be_visible(self, element_locator, wait=ACCEPTABLE_LOADING_TIME):
        self.wait_for_element_to_be_present(element_locator, wait=wait)
        WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(element_locator))
