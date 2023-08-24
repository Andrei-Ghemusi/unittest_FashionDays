from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebDriver
import requests
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUtils:


    # This method clicks on an element
    @staticmethod
    def click_element(driver: WebDriver, element: tuple[str, str]):
        driver.find_element(*element).click()


    # This method checks that the expected url is the same as the actual url
    @staticmethod
    def assert_current_url(driver: WebDriver, expected_url: str):
        actual_url: str = driver.current_url
        assert expected_url == actual_url


    # This method checks that the expected page title is in the actual page title
    @staticmethod
    def assert_page_title(driver: WebDriver, expected_title: str):
        actual_title: str = driver.title
        assert expected_title in actual_title, f'ERROR, expected {expected_title} but got {actual_title}'


    # This method checks that the expected status code is the same as the actual status code
    @staticmethod
    def assert_status_code(url: str, expected_code: int):
        response = requests.head(url)
        assert expected_code == response.status_code


    # This method checks that the element is displayed
    @staticmethod
    def assert_is_element_displayed(driver: WebDriver, element: tuple[str, str]):
        is_element_displayed: bool = driver.find_element(*element).is_displayed()
        assert is_element_displayed, f"Element {element} is not displayed"


    # This method inputs an email on an email element,
    #                a password in a password element,
    #                and clicks a (login or not) button.
    @staticmethod
    def send_inputs_and_click(driver: WebDriver, button_element: tuple[str, str] = None, input_element_1: tuple[str, str] = None, input_text_1: str = None, input_element_2: tuple[str, str] =None, input_text_2: str = None):
        if input_element_1 is not None:
            driver.find_element(*input_element_1).send_keys(input_text_1)
        if input_element_2 is not None:
            driver.find_element(*input_element_2).send_keys(input_text_2)
        if button_element is not None:
            driver.find_element(*button_element).click()


    # This method uses an explicit wait until an element is visible
    @staticmethod
    def wait_for_element_visibility(driver: WebDriver, element_locator: tuple[str, str]):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element_locator))


    # This method checks that the expected text is the same as the text on an element
    @staticmethod
    def assert_text_message(driver: WebDriver, text_element: tuple[str, str], expected_text: str):
        element = TestUtils.wait_for_element_visibility(driver, text_element)
        actual_text: str = element.text
        assert expected_text in actual_text, f'ERROR, expected {expected_text}, but got {actual_text}'


    # This method scrolls/hovers to a certain element
    @staticmethod
    def move_to_element(driver: WebDriver, element: tuple[str, str]):
        action_chains = ActionChains(driver)
        action_chains.move_to_element(driver.find_element(*element)).perform()


    # This method checks that a promotion is still available
    @staticmethod
    def assert_is_promotion_displayed(driver: WebDriver, element: tuple[str, str]):
        unavailable: str = 'Promotion is no longer available!'
        try:
            promotion_display: WebElement = driver.find_element(*element)
            promotion_display.is_displayed()
            assert promotion_display, f'{unavailable}'
        except NoSuchElementException:
            pass


    # This method switches the browser window to a desired one
    @staticmethod
    def switch_window(driver: WebDriver, page_index: int):
        page: str = driver.window_handles[page_index]
        driver.switch_to.window(page)


    # this method asserts two values (integers)
    @staticmethod
    def assert_values(driver: WebDriver, element: tuple[str, str], expected_value: int):
        actual_value = int(driver.find_element(*element).text)
        assert expected_value == actual_value, f'ERROR, expected value {expected_value}, but got {actual_value} instead'


    # this method presses enter
    @staticmethod
    def press_enter(driver: WebDriver, element: tuple[str, str]):
        driver.find_element(*element).send_keys(Keys.ENTER)





















