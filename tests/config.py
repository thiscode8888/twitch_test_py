from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest
import logging
from reportportal_client import RPLogger

@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.setLoggerClass(RPLogger)
    return logger

mobile_emulation = {"deviceName": "Nexus 5"}

def config_driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("start-maximized")
    options.add_argument('log-level=3')
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(2)
    return driver