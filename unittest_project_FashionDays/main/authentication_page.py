# Import necessary modules and classes
import time
from main.setups import AuthenticationPageSetupAndTearDown
from main.test_methods import TestUtils


# This class has positive tests performed on the Authentication page
class PositiveTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):

    # Test case: Check if the current URL is correct
    def test_url(self):
        TestUtils.assert_current_url(self.chrome,
                                     expected_url='https://www.fashiondays.ro/customer/authentication')

    # Test case: Check if the login button is displayed
    def test_login_display(self):
        TestUtils.assert_is_element_displayed(self.chrome,
                                              element=self.LOGIN_BUTTON)

    # Test case: Check if the login with Facebook button is displayed
    def test_facebook_login_display(self):
        TestUtils.assert_is_element_displayed(self.chrome,
                                              element=self.FACEBOOK_LOGIN_BUTTON)

    # Test case: Check if the login with eMag button is displayed
    def test_emag_login_display(self):
         TestUtils.assert_is_element_displayed(self.chrome,
                                               element=self.EMAG_LOGIN_BUTTON)

    # Test case: Check if the login with Gmail button is displayed
    def test_gmail_login_display(self):
        TestUtils.assert_is_element_displayed(self.chrome,
                                              element=self.GMAIL_LOGIN_BUTTON)

    # Test case: Check if the login with Apple button is displayed
    def test_apple_login_display(self):
        TestUtils.assert_is_element_displayed(self.chrome,
                                              element=self.APPLE_LOGIN_BUTTON)

    # Method to check account status (logged in or logged out)
    def account_status_check(self):
        time.sleep(1)  # A small delay - neither implicit nor explicit wait would work here
        TestUtils.click_element(self.chrome,
                                element=self.ACCOUNT)
        TestUtils.assert_current_url(self.chrome,
                                     expected_url='https://www.fashiondays.ro/customer/settings/')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.CONTUL_MEU_TEXT,
                                      expected_text='Contul Meu')

    # Test case: Log in using valid email and password
    def test_valid_credentials_login(self):
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.EMAIL,
                                               password_element=self.PASSWORD,
                                               login_button_element=self.LOGIN_BUTTON,
                                               email_text='pythontestemail083@gmail.com',
                                               password_text='TestEmail123')
        self.account_status_check()

    # Test case: Log in with correct email and incorrect password
    def test_correct_email_and_incorrect_password(self):
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.EMAIL,
                                               password_element=self.PASSWORD,
                                               login_button_element=self.LOGIN_BUTTON,
                                               email_text='pythontestemail083@gmail.com',
                                               password_text='password')
        TestUtils.assert_text_message(self.chrome,
                                      self.EMAIL_ERROR,
                                      expected_text='Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.')

    # Test case: Log in using Facebook
    def test_login_using_facebook(self):
        TestUtils.click_element(self.chrome, self.FACEBOOK_LOGIN_BUTTON)
        all_handles = self.chrome.window_handles
        popup_window_handle = all_handles[-1]
        self.chrome.switch_to.window(popup_window_handle)
        TestUtils.click_element(self.chrome, self.FACEBOOK_COOKIES)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.FACEBOOK_EMAIL,
                                               password_element=self.FACEBOOK_PASSWORD,
                                               login_button_element=self.FACEBOOK_POP_UP_LOGIN,
                                               email_text='pythontestemail083@gmail.com',
                                               password_text='TestEmail123')
        time.sleep(5)
        main_handle = all_handles[0]
        self.chrome.switch_to.window(main_handle)
        self.account_status_check()

    # Test case: Log out after logging in
    def test_logout(self):
        self.test_valid_credentials_login()
        TestUtils.hover_over_element(self.chrome, self.ACCOUNT)
        TestUtils.click_element(self.chrome, self.LOGOUT)
        TestUtils.click_element(self.chrome, self.ACCOUNT)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/customer/authentication')



# This class has negative tests performed on the Authentication page
class NegativeTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):

    # Test case: Attempt to log in with no credentials
    def test_no_credentials_login(self):
        # Click the login button
        TestUtils.click_element(self.chrome, self.LOGIN_BUTTON)

        # Assert error messages for missing email and password
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.PASSWORD_ERROR,
                                      expected_text='Acest camp este obligatoriu')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Acest camp este obligatoriu')

    # Test case: Attempt to log in with valid email but no password
    def test_valid_email_and_no_password(self):
        # Enter valid email and click login
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.EMAIL,
                                               email_text='pythontestemail083@gmail.com',
                                               login_button_element=self.LOGIN_BUTTON)

        # Assert error message for missing password
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.PASSWORD_ERROR,
                                      expected_text='Acest camp este obligatoriu')

    # Test case: Attempt to log in with password but no email
    def test_password_only_and_no_email(self):
        # Enter password and click login
        TestUtils.send_email_and_password_keys(self.chrome,
                                               password_element=self.PASSWORD,
                                               password_text='TestEmail123',
                                               login_button_element=self.LOGIN_BUTTON)

        # Assert error message for missing email
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Acest camp este obligatoriu')

    # Test case: Attempt to log in with invalid email and password
    def test_invalid_email_and_password(self):
        # Enter invalid email and password and click login
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.EMAIL,
                                               email_text='wrong_username',
                                               password_element=self.PASSWORD,
                                               password_text='password',
                                               login_button_element=self.LOGIN_BUTTON)

        # Assert error message for invalid email format
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Adresa de email este invalida.')

    # Test case: Attempt to log in with special characters in email and password
    def test_special_characters_email_and_password(self):
        # Enter email and password with special characters and click login
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.EMAIL,
                                               email_text='hgsyf$$%435@ii&&*)()u.com',
                                               password_element=self.PASSWORD,
                                               password_text='paerugehr#$5^.35>>>',
                                               login_button_element=self.LOGIN_BUTTON)

        # Assert error message for invalid email format
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Adresa de email este invalida.')
