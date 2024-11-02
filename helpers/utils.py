from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:

    def __init__(self, browser):
        self.browser = browser

    def get(self, *locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

    def get_multiple(self, *locator):
        return self.browser.find_elements(*locator)

    def click(self, *by_locator):
        self.get(*by_locator).click()

    def remove_element(self, locator):
        self.browser.execute_script("""
        var element = document.querySelector(arguments[0]);
        if (element)
            element.parentNode.removeChild(element);
        """, locator)
        return 

    # optional click won't fail the test if its element is not found
    # waiting for 5 seconds for element to be clickable before skipping
    def optional_click(self, locator):
            try:
                WebDriverWait(self.browser,5).until(EC.element_to_be_clickable(locator)).click()
            except:
                print("\tOptional click not performed")
    
    def click_first_element_in_viewport(self, *locator):
            # click on the first stream video div that is fully in view port after scrolling
        for y in self.browser.find_elements(*locator):
            # return true when the first element in a list of elements
            # is fully visible in the view port
            x = self.browser.execute_script("var elem = arguments[0],                "
                                        "  box = elem.getBoundingClientRect(),    "
                                        "  cx = box.left + box.width / 2,         "
                                        "  cy = box.top + box.height / 2,         "
                                        "  e = document.elementFromPoint(cx, cy); "
                                        "for (; e; e = e.parentElement) {         "
                                        "  if (e === elem)                        "
                                        "    return true;                         "
                                        "}                                        "
                                        "return false;                            "
                                        , y)
                
            if x:
                y.click()
                break

    # save screenshot with timestamp in the screenshot folder
    def take_screenshot(self):
        self.browser.save_screenshot("./screenshots/" + 
            datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".png")

