import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from main.setups import AuthenticationPageSetupAndTearDown
from selenium.webdriver import ActionChains


# This class has positive tests performed on the Authentication page
class PositiveTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):

    # simple method that checks that the current url is correct
    def test_url(self):
        expected_url: str = 'https://www.fashiondays.ro/customer/authentication'
        actual_url: str = self.chrome.current_url
        self.assertEqual(expected_url, actual_url)

    # This method checks that the login button is displayed
    def test_login_display(self):
        is_login_displayed: bool = self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_login_displayed, f'Error, login button is not displayed')

    # this method checks that the login with facebook button is displayed
    def test_facebook_login_display(self):
        is_facebook_displayed: bool = self.chrome.find_element(*self.FACEBOOK_LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_facebook_displayed, 'ERROR, facebook login button is not displayed')

    # this method is NOT a test, we will we calling it in tests to checks the state transition from logged in to logged out or vice versa
    def account_status_check(self):
        time.sleep(1)
        # # I added a sleep of 1 sec because neither the implicit nor explicit wait would work here
        self.chrome.find_element(*self.ACCOUNT).click()
        actual_url: str = self.chrome.current_url
        expected_url: str = 'https://www.fashiondays.ro/customer/settings/'
        self.assertEqual(expected_url, actual_url)
        # here we clicked on the account button, then we check that we are being sent on the correct link
        actual_text = self.chrome.find_element(By.XPATH, '//*[text()="Contul Meu"]').text
        expected_text: str = 'Contul Meu'
        self.assertEqual(expected_text, actual_text)
        # here we check that while here the correct text is being displayed

    # this method checks that we can log in using a correct email and password, and that we changed from not logged in => logged in
    def test_valid_credentials_login(self):
        self.chrome.find_element(*self.EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('TestEmail123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.account_status_check()
        # here we called the previous method to check the status regarding our account

    # This method checks that we cannot log in after providing an incorrect password and a correct email
    def test_correct_email_and_incorrect_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        email_error = self.wait_for_element_visibility(self.EMAIL_ERROR)
        # I added an explicit wait of 10 secs here because it would take a few seconds for the message to appear
        actual_email_error: str = email_error.text
        expected_email_error: str = 'Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.'
        self.assertEqual(expected_email_error, actual_email_error), f'ERROR, expected {expected_email_error}, but got {actual_email_error}'
        # here we check that the expected error is the same with the actual error message we receive

    # This method checks that we can log in using facebook
    def test_login_using_facebook(self):
        self.chrome.find_element(*self.FACEBOOK_LOGIN_BUTTON).click()
        all_handles = self.chrome.window_handles
        popup_window_handle = all_handles[-1]
        self.chrome.switch_to.window(popup_window_handle)
        # here we change to the newly opened window

        self.chrome.find_element(*self.FACEBOOK_COOKIES).click()
        # we accept the cookies
        self.chrome.find_element(*self.FACEBOOK_EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.FACEBOOK_PASSWORD).send_keys('TestEmail123')
        self.chrome.find_element(*self.FACEBOOK_POP_UP_LOGIN).click()
        # we input the correct credentials and click on the login button
        time.sleep(5)
        # it takes a while for the system to log us in so, up to 5 seconds, hence why I added a time.sleep(5)

        main_handle = all_handles[0]
        self.chrome.switch_to.window(main_handle)
        # we switch back to our original window
        self.account_status_check()
        # we call the method to check that we are logged in

    # This method checks that after clicking "LOGOUT" we are being logged out
    def test_logout(self):
        self.test_valid_credentials_login()
        actions = ActionChains(self.chrome)
        account_element: WebElement = self.chrome.find_element(*self.ACCOUNT)
        actions.move_to_element(account_element).perform()
        # we hover over the account element in order to display the "LOGOUT" button
        self.chrome.find_element(*self.LOGOUT).click()
        # we click on the logout button
        self.chrome.find_element(*self.ACCOUNT).click()
        self.test_url()
        # we check that we are not logged in and are on the url which asks us to log in


# This class has negative tests performed on the Authentication page
class NegativeTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):

    def check_missing_credential_error(self, error):
        missing_credential_error: str = self.chrome.find_element(*error).text
        expected_missing_credential_error: str = 'Acest camp este obligatoriu'
        self.assertEqual(missing_credential_error, expected_missing_credential_error), f'Error, expected {expected_missing_credential_error}, but got {missing_credential_error}'

    def test_no_credentials_login(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.check_missing_credential_error(self.PASSWORD_ERROR)
        self.check_missing_credential_error(self.EMAIL_ERROR)

    def test_valid_email_and_no_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.check_missing_credential_error(self.PASSWORD_ERROR)

    def test_password_only_and_no_email(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('TestEmail123')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.check_missing_credential_error(self.EMAIL_ERROR)

    def check_invalid_email_error_message(self):
        actual_email_error: str = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_email_error: str = 'Adresa de email este invalida.'
        self.assertEqual(actual_email_error,expected_email_error), f'ERROR, expected {expected_email_error}, but got {actual_email_error}'

    def test_invalid_email_and_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('wrong_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.check_invalid_email_error_message()

    def test_special_characters_email_and_password(self):
        self.chrome.find_element(*self.EMAIL).send_keys('hgsyf$$%435@ii&&*)()u.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('paerugehr#$5^.35>>>')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.check_invalid_email_error_message()

