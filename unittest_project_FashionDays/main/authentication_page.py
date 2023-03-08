import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AuthenticationPage(TestCase):
    AUTHENTICATION_PAGE = (By.CSS_SELECTOR, '.icon-fdux_profile')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit" and @id="pizokel_customer_submit"]')
    EMAIL_ERROR = (By.XPATH, '//*[@id="loginform"]/div[1]/div')
    PASSWORD_ERROR = (By.XPATH, '//*[@id="loginform"]/div[2]/div')
    USERNAME = (By.XPATH, '//*[@id ="email"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')

# this is the setup method, it will run at the beginning of any test
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get('https://www.fashiondays.ro/customer/authentication')
        # self.chrome.find_element(By.XPATH, '//*[text()="Respinge"]').click()
        self.chrome.implicitly_wait(2)

# this is the tearDown, it'll run at the END of any and every test
    def tearDown(self) -> None:
        self.chrome.quit()


# This method checks that while on the authentication page, the login button is displayed
    def test_login_display(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        is_login_displayed = self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_login_displayed), f'Error, login button is not displayed'

# This method checks that we cannot login after providing no credentials and if we receive the expected errors
    def test_no_credentials_login(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        missing_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_missing_email_error = 'Acest camp este obligatoriu'
        missing_password_error = self.chrome.find_element(*self.PASSWORD_ERROR).text
        expected_missing_password_error = 'Acest camp este obligatoriu'
        self.assertEqual(missing_email_error, expected_missing_email_error), f'Error, expected {expected_missing_email_error}, but got {missing_email_error}'
        self.assertEqual(missing_password_error,
                         expected_missing_password_error), f'Error, expected {expected_missing_password_error}, but got {missing_password_error}'

# This method checks if we receive the expected error after providing an invalid email, and fill in a password
    def test_invalid_email_and_password(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.USERNAME).send_keys('wrong_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_email_error = 'Adresa de email este invalida.'
        self.assertEqual(actual_email_error,expected_email_error), f'ERROR, expected {expected_email_error}, but got {actual_email_error}'

# This method checks that after we provide a valid e-mail and a password, but no account is present on said e-mail, we receive the expected error
    def test_incorrect_email_and_password(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.USERNAME).send_keys('wrong_username@mail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
        actual_valid_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_valid_email_error = 'Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.'
        self.assertEqual(actual_valid_email_error,
                         expected_valid_email_error), f'ERROR, expected {expected_valid_email_error}, but got {actual_valid_email_error}'
