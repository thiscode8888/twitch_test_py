# Open Twitch Stream (GIF)
![Complete front-end Twitch open stream test](py_selenium_twitch.gif)

# Structure Description
## Page Object Model
* The code related to a particular website page is organised in a class of its own (known as a Page Object Model). This helps to make each and every page logic more descriptive and re-usable. A particular website pages' specific elements are listed in the relevant page object. Functions directly related to a page are also included in the page class.
## Tests (Using PyTest)
* The actual test code, which we make as short as possible by using the helper and page classes where possible for most of the logic needed to be run during the test.
## Helper Classes
* Code that helps us shorten our page classes or tests. The utility class takes care of providing utility functions that can be used in either the page objects or tests. If a particular function uses elements or functions from more than one page object, we will include it in the helper folder under a descriptive name.

# Selenium Best Practices
## Explicit Assertions
* Favouring explicit assertions over implicit for better readability and clear test step failures.
* Favouring explicit waits to reduce the test runtime as much as possible.
* Promoting modular and reusable page objects, with the help of helper classes to further simplify pages and tests.
* Each and every test is atomic and covers one specific feature.
