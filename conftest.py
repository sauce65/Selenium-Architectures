import pytest
from selenium import webdriver

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1920
RESOLUTION = str(SCREEN_WIDTH) + ',' + str(SCREEN_HEIGHT)


@pytest.fixture(scope='function')
def web_driver(request):
    test_name = request.node.name
    capabilities = configure_base_capabilities(test_name, RESOLUTION)
    driver_path = "C:\\Users\\Paul\\PycharmProjects\\Sample-Selenium-Framework\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path,
                              desired_capabilities=capabilities)

    yield driver

    driver.quit()


def configure_base_capabilities(test_name, resolution):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--window-size={resolution}')
    capabilities = options.to_capabilities()
    capabilities['name'] = test_name
    return capabilities
