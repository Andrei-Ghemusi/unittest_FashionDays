import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from main.setups import AuthenticationPageSetupAndTearDown
from selenium.webdriver import ActionChains

class PositiveTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):
    LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//input[@type="submit" and @id="pizokel_customer_submit"]')
    EMAIL_ERROR: tuple[str, str] = (By.XPATH, '//*[@id="loginform"]/div[1]/div')
    PASSWORD_ERROR: tuple[str, str] = (By.XPATH, '//*[@id="loginform"]/div[2]/div')
    EMAIL: tuple[str, str] = (By.XPATH, '//*[@id ="email"]')
    PASSWORD: tuple[str, str] = (By.XPATH, '//*[@id="password"]')
    ACCOUNT: tuple[str, str] = (By.XPATH, '//*[@id="customer-account"]/div[1]/i')
    FACEBOOK_LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="login"]/div[4]/div[2]/button/div/span[2]')
    FACEBOOK_COOKIES: tuple[str, str] = (By.XPATH, '//button[text()="Allow all cookies"]')
    FACEBOOK_EMAIL = (By.XPATH, '//*[@id="email"]')
    FACEBOOK_PASSWORD = (By.XPATH, '//*[@id="pass"]')
    FACEBOOK_POP_UP_LOGIN = (By.XPATH, '//*[@id="loginbutton"]')
    LOGOUT = (By.XPATH, '//*[text()="Logout"]')


    def test_url(self):
        expected_url = 'https://www.fashiondays.ro/customer/authentication'
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url, actual_url)

    # This method checks that while on the authentication page, the login button is displayed
    def test_login_display(self):
        is_login_displayed = self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_login_displayed, f'Error, login button is not displayed')

    def test_facebook_login_display(self):
        is_facebook_displayed = self.chrome.find_element(*self.FACEBOOK_LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_facebook_displayed, 'ERROR, facebook login button is not displayed')

    def account_status_check(self):
        time.sleep(1)
        # I added a sleep of 1 sec because neither the implicit nor explicit wait would work here
        self.chrome.find_element(*self.ACCOUNT).click()
        actual_url: str = self.chrome.current_url
        expected_url: str = 'https://www.fashiondays.ro/customer/settings/'
        self.assertEqual(expected_url, actual_url)
        actual_text = self.chrome.find_element(By.XPATH, '//*[text()="Contul Meu"]').text
        expected_text: str = 'Contul Meu'
        self.assertEqual(expected_text, actual_text)


    def test_valid_credentials_login(self):
        self.chrome.find_element(*self.EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('TestEmail123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.account_status_check()

        # This method checks that after we provide a valid e-mail and a password, but no account is present on said e-mail, we receive the expected error
    def test_valid_email_and_incorrect_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_valid_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_valid_email_error = 'Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.'
        self.assertEqual(actual_valid_email_error, expected_valid_email_error), f'ERROR, expected {expected_valid_email_error}, but got {actual_valid_email_error}'

    def test_login_using_facebook(self):
        self.chrome.find_element(*self.FACEBOOK_LOGIN_BUTTON).click()
        all_handles = self.chrome.window_handles
        popup_window_handle = all_handles[-1]
        self.chrome.switch_to.window(popup_window_handle)
        self.chrome.find_element(*self.FACEBOOK_COOKIES).click()
        self.chrome.find_element(*self.FACEBOOK_EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.FACEBOOK_PASSWORD).send_keys('TestEmail123')
        self.chrome.find_element(*self.FACEBOOK_POP_UP_LOGIN).click()
        time.sleep(5)
        main_handle = all_handles[0]
        self.chrome.switch_to.window(main_handle)
        self.account_status_check()

    def test_logout(self):
        self.test_valid_credentials_login()
        actions = ActionChains(self.chrome)
        account_element = self.chrome.find_element(*self.ACCOUNT)
        actions.move_to_element(account_element).perform()
        self.chrome.find_element(*self.LOGOUT).click()
        self.chrome.find_element(*self.ACCOUNT).click()
        self.test_url()



class NegativeTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):
    # This method checks that we cannot log in after providing no credentials and if we receive the expected errors
    def test_no_credentials_login(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        missing_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        missing_password_error = self.chrome.find_element(*self.PASSWORD_ERROR).text
        expected_missing_credential_error = 'Acest camp este obligatoriu'
        self.assertEqual(missing_email_error, expected_missing_credential_error), f'Error, expected {expected_missing_credential_error}, but got {missing_email_error}'
        self.assertEqual(missing_password_error,expected_missing_credential_error), f'Error, expected {expected_missing_credential_error}, but got {missing_password_error}'

    def test_valid_email_and_no_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected_error_message = 'Acest camp este obligatoriu'
        actual_error_message = self.chrome.find_element(*self.PASSWORD_ERROR).text
        self.assertEqual(expected_error_message,actual_error_message)

    def test_password_only_and_no_email(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('TestEmail123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected_error_message = 'Acest camp este obligatoriu'
        actual_error_message = self.chrome.find_element(*self.EMAIL_ERROR).text
        self.assertEqual(expected_error_message, actual_error_message)


# This method checks if we receive the expected error after providing an invalid email, and fill in a password
    def test_invalid_email_and_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('wrong_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_email_error = 'Adresa de email este invalida.'
        self.assertEqual(actual_email_error,expected_email_error), f'ERROR, expected {expected_email_error}, but got {actual_email_error}'



