from unittest import TestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests

class MainPageSetupAndTearDown(TestCase):
    chrome: WebDriver

    # this is the setup method, it will run at the beginning of any test
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        url = 'https://www.fashiondays.ro/'
        self.chrome.get(url)
        response = requests.head(url)
        self.assertEqual(200, response.status_code,
                         f'ERROR, was expecting status code 200 but got {response.status_code}')
        try:
            self.chrome.find_element(By.XPATH, '//*[text()="Accept"]').click()
        except NoSuchElementException:
            pass
        self.chrome.implicitly_wait(2)


    # this is the tearDown, it'll run at the END of any and every test
    def tearDown(self) -> None:
        self.chrome.quit()


class AuthenticationPageSetupAndTearDown(TestCase):
    LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//input[@type="submit" and @id="pizokel_customer_submit"]')
    EMAIL_ERROR: tuple[str, str] = (By.XPATH, '//*[@id="loginform"]/div[1]/div')
    PASSWORD_ERROR: tuple[str, str] = (By.XPATH, '//*[@id="loginform"]/div[2]/div')
    EMAIL: tuple[str, str] = (By.XPATH, '//*[@id ="email"]')
    PASSWORD: tuple[str, str] = (By.XPATH, '//*[@id="password"]')
    ACCOUNT: tuple[str, str] = (By.XPATH, '//*[@id="customer-account"]/div[1]/i')
    FACEBOOK_LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="login"]/div[4]/div[2]/button/div/span[2]')
    FACEBOOK_COOKIES: tuple[str, str] = (By.XPATH, '//button[text()="Allow all cookies"]')
    FACEBOOK_EMAIL: tuple[str, str] = (By.XPATH, '//*[@id="email"]')
    FACEBOOK_PASSWORD: tuple[str, str] = (By.XPATH, '//*[@id="pass"]')
    FACEBOOK_POP_UP_LOGIN: tuple[str, str] = (By.XPATH, '//*[@id="loginbutton"]')
    LOGOUT: tuple[str, str] = (By.XPATH, '//*[text()="Logout"]')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        url: str = 'https://www.fashiondays.ro/customer/authentication'
        self.chrome.get(url)
        response = requests.head(url)
        self.assertEqual(200, response.status_code,
                         f'ERROR, was expecting status code 200 but got {response.status_code}')
        try:
            self.chrome.find_element(By.XPATH, '//*[text()="Accept"]').click()
        except NoSuchElementException:
            pass
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

