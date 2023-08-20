from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
import requests
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUtils:

    @staticmethod
    def click_element(driver: WebDriver, element: tuple[str, str]):
        driver.find_element(*element).click()

    @staticmethod
    def assert_current_url(driver: WebDriver, expected_url: str):
        actual_url: str = driver.current_url
        assert expected_url == actual_url

    @staticmethod
    def assert_page_title(driver: WebDriver, expected_title: str):
        actual_title: str = driver.title
        assert expected_title in actual_title

    # This method checks that the actual status code is the expected one
    @staticmethod
    def assert_status_code(url: str, expected_code: int):
        response = requests.head(url)
        assert expected_code == response.status_code

    # This method checks that the element is displayed
    @staticmethod
    def assert_is_element_displayed(driver: WebDriver, element: tuple[str, str]):
        is_element_displayed: bool = driver.find_element(*element).is_displayed()
        assert is_element_displayed, f"Element {element} is not displayed"

    # This method inputs an email, a password and clicks on the login button
    @staticmethod
    def send_email_and_password_keys(driver: WebDriver, login_button_element: tuple[str, str], email_element: tuple[str, str] = None, email_text: str = None, password_element: tuple[str, str] =None, password_text: str = None):
        if email_element is not None:
            driver.find_element(*email_element).send_keys(email_text)
        if password_element is not None:
            driver.find_element(*password_element).send_keys(password_text)
        driver.find_element(*login_button_element).click()

    @staticmethod
    def wait_for_element_visibility(driver: WebDriver, element_locator: tuple[str, str]):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element_locator))


    @staticmethod
    def assert_text_message(driver: WebDriver, text_element: tuple[str, str], expected_text: str):
        element = TestUtils.wait_for_element_visibility(driver, text_element)
        actual_text: str = element.text
        assert expected_text in actual_text, f'ERROR, expected {expected_text}, but got {actual_text}'

    @staticmethod
    def hover_over_element(driver, element):
        actions = ActionChains(driver)
        account_element: WebElement = driver.find_element(*element)
        actions.move_to_element(account_element).perform()

    # this method scrolls to a certain element
    @staticmethod
    def scroll_to_element(driver, element):
        driver.action_chains = ActionChains(driver)
        driver.action_chains.move_to_element(driver.find_element(*element)).perform()

    @staticmethod
    def assert_is_promotion_displayed(driver, element):
        unavailable: str = 'Promotion is no longer available!'
        try:
            promotion_display: WebElement = driver.find_element(*element)
            promotion_display.is_displayed()
            assert promotion_display, f'{unavailable}'
        except NoSuchElementException:
            pass

    @staticmethod
    def switch_page(driver, page_index: int):
        page: str = driver.window_handles[page_index]
        driver.switch_to.window(page)























