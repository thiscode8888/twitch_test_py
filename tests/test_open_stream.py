import pytest
from pages.home_page import HomePage
from tests.config import config_driver
from helpers.utils import Utils

@pytest.fixture
def browser():
    driver = config_driver()
    yield driver
    driver.quit()

def test_open_stream(browser):
    home_page = HomePage(browser)
    utils = Utils(browser)

    # load home URL
    home_page.load()

    home_page.wait_for_home_page_to_load()
    
    utils.remove_element(home_page.CONSENT_POPUP)

    home_page.dismiss_mob_app_notification()

    home_page.search("Starcraft II")
    
    # we filter to channels section as it has a higher
    # chance of finding live streams instead of channels when scrolling
    home_page.go_to_section("channels")
    
    home_page.scroll_down(2)

    utils.click_first_element_in_viewport(*home_page.STREAMS_LIST)

    # optional click for streamers that have a mature audience warning
    home_page.optional_click(home_page.START_WATCHING_BTN)

    utils.take_screenshot()