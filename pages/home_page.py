from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from helpers.utils import Utils


class HomePage(Utils):
    URL = 'https://m.twitch.tv/'
    CONSENT_POPUP = "#root > div.Layout-sc-1xcs6mc-0.eTiaZz > div"
    CONSENT_ACCEPT_BTN = (By.XPATH, '//*[@data-a-target="consent-banner-accept"]')
    MOBILE_APP_BANNER_DISMISS_BTN = (By.CSS_SELECTOR, '.ScCoreButton-sc-ocjdkq-0.kHcUBg')
    SEARCH_BTN = (By.CSS_SELECTOR, '[aria-label="Search"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '[type="search"]')
    BODY = (By.CSS_SELECTOR, 'body')
    CHANNELS_CATEGORY = (By.CSS_SELECTOR, '.Layout-sc-1xcs6mc-0.juXjJY')
    STREAMS_LIST = (By.CSS_SELECTOR, '.Layout-sc-1xcs6mc-0.ieOTqj')
    START_WATCHING_BTN = (By.CSS_SELECTOR, '[data-a-target="content-classification-gate-overlay-start-watching-button"]')

    def load(self):
        self.browser.get(self.URL)

    def wait_for_element_to_load(self, element):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(element))

    def wait_for_home_page_to_load(self):
        self.wait_for_element_to_load(self.CONSENT_ACCEPT_BTN)

    def search(self, term):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SEARCH_FIELD)).click()

        self.get(*self.SEARCH_FIELD).send_keys(term)

        SEARCH_TITLE = (By.CSS_SELECTOR, '[title="' + term + '"]')
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(SEARCH_TITLE)
            ).click()

    def scroll_down(self, timesToScroll):
        for x in range(timesToScroll):
            self.get(*self.BODY).send_keys(Keys.PAGE_DOWN)

    def dismiss_mob_app_notification(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.MOBILE_APP_BANNER_DISMISS_BTN)).click()

    def go_to_section(self, section):
        input_fields = {
            "top": (By.CSS_SELECTOR, '[data-index="0"]'),
            "channels": (By.CSS_SELECTOR, '[data-index="1"]'),
            "categories": (By.CSS_SELECTOR, '[data-index="2"]'),
            "videos": (By.CSS_SELECTOR, '[data-index="3"]'),
        }

        self.get(*input_fields.get(section, "Tab list section chosen does not exist")).click()