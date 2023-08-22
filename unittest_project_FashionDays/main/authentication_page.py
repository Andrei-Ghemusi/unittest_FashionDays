# Import necessary modules and classes
import time
from main.setups import AuthenticationPageSetupAndTearDown
from main.utility_methods import TestUtils


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


    def test_valid_credentials_login(self):
        """
            Test case: Log in using valid email and password

            Steps:
                1. Provide a valid email and password.
                2. Click on the login button.
                3. Verify the account status after successful login.

            Expected Result:
                Logging in with valid credentials should result in a successful login and the account status should be logged in.
        """
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.LOGIN_BUTTON,
                                               email_element=self.EMAIL, email_text='pythontestemail083@gmail.com',
                                               password_element=self.PASSWORD, password_text='TestEmail123')
        self.account_status_check()


    def test_correct_email_and_incorrect_password(self):
        """
        Test case: Log in with correct email and incorrect password

        Steps:
            1. Provide a correct email and an incorrect password.
            2. Click on the login button.
            3. Verify the displayed error message.

        Expected Result:
            Logging in with correct email and incorrect password should display an error message indicating incorrect credentials.
        """
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.LOGIN_BUTTON,
                                               email_element=self.EMAIL, email_text='pythontestemail083@gmail.com',
                                               password_element=self.PASSWORD, password_text='password')
        TestUtils.assert_text_message(self.chrome,
                                      self.EMAIL_ERROR,
                                      expected_text='Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.')


    def test_login_using_facebook(self):
        """
            Test case: Log in using Facebook

            Steps:
                1. Click on the Facebook login button.
                2. Switch to the popup window.
                3. Click on the Facebook cookies confirmation.
                4. Provide Facebook email and password.
                5. Click on the login button in the popup.
                6. Switch back to the main window.
                7. Verify the account status after successful login.

            Expected Result:
                Logging in using Facebook credentials should result in a successful login and the account status should be logged in.
        """
        TestUtils.click_element(self.chrome, self.FACEBOOK_LOGIN_BUTTON)
        all_handles = self.chrome.window_handles
        popup_window_handle = all_handles[-1]
        self.chrome.switch_to.window(popup_window_handle)
        TestUtils.click_element(self.chrome, self.FACEBOOK_COOKIES)
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.FACEBOOK_POP_UP_LOGIN,
                                               email_element=self.FACEBOOK_EMAIL,
                                               email_text='pythontestemail083@gmail.com',
                                               password_element=self.FACEBOOK_PASSWORD, password_text='TestEmail123')
        time.sleep(5) # I added a sleep of 5 here because it takes a while for facebook to log in and I could not see where I could add an explicit wait
        main_handle = all_handles[0]
        self.chrome.switch_to.window(main_handle)
        self.account_status_check()


    def test_logout(self):
        """
            Test case: Log out after logging in

            Steps:
                1. Log in using valid credentials.
                2. Move to the account menu.
                3. Click on the logout option.
                4. Click on the account menu again.
                5. Verify that the user is redirected to the authentication page.

            Expected Result:
                After logging in and then logging out, the user should be successfully logged out and after clicking on account is redirected to the authentication page.
        """
        self.test_valid_credentials_login()
        TestUtils.move_to_element(self.chrome, self.ACCOUNT)
        TestUtils.click_element(self.chrome, self.LOGOUT)
        TestUtils.click_element(self.chrome, self.ACCOUNT)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/customer/authentication')



# This class has negative tests performed on the Authentication page
class NegativeTestsAuthenticationPage(AuthenticationPageSetupAndTearDown):

    def test_no_credentials_login(self):
        """
            Test case: Attempt to log in with no credentials

            Steps:
                1. Click the login button.
                2. Assert error messages for missing email and password.

            Expected Result:
                Error messages should appear for both missing email and password fields.
        """
        # Click the login button
        TestUtils.click_element(self.chrome, self.LOGIN_BUTTON)

        # Assert error messages for missing email and password
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.PASSWORD_ERROR,
                                      expected_text='Acest camp este obligatoriu')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Acest camp este obligatoriu')


    def test_valid_email_and_no_password(self):
        """
            Test case: Attempt to log in with valid email but no password

            Steps:
                1. Enter a valid email and no password.
                2. Click login.
                3. Assert error message for missing password.

            Expected Result:
                An error message should appear indicating that the password field is required.
        """
        # Enter valid email and click login
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.LOGIN_BUTTON,
                                               email_element=self.EMAIL, email_text='pythontestemail083@gmail.com')
        # Assert error message for missing password
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.PASSWORD_ERROR,
                                      expected_text='Acest camp este obligatoriu')


    def test_password_only_and_no_email(self):
        """
            Test case: Attempt to log in with password but no email
            Steps:
                1. Enter a password and click login.
                2. Assert error message for missing email.

            Expected Result:
                An error message should appear indicating that the email field is required.
        """
        # Enter password and click login
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.LOGIN_BUTTON,
                                               password_element=self.PASSWORD, password_text='TestEmail123')
        # Assert error message for missing email
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Acest camp este obligatoriu')


    def test_invalid_email_and_password(self):
        """
            Test case: Attempt to log in with invalid email and password

           Steps:
                1. Enter an invalid email and password and click login.
                2. Assert error message for invalid email format.

           Expected Result:
                An error message should appear indicating that the email format is invalid.
        """
        # Enter invalid email and password and click login
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.LOGIN_BUTTON,
                                               email_element=self.EMAIL, email_text='wrong_username',
                                               password_element=self.PASSWORD, password_text='password')
        # Assert error message for invalid email format
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Adresa de email este invalida.')


    def test_special_characters_email_and_password(self):
        """
            Test case: Attempt to log in with special characters in email and password

            Steps:
                1. Enter an email and password with special characters and click login.
                2. Assert error message for invalid email format.

            Expected Result:
                An error message should appear indicating that the email format is invalid.
        """
        # Enter email and password with special characters and click login
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.LOGIN_BUTTON,
                                               email_element=self.EMAIL, email_text='hgsyf$$%435@ii&&*)()u.com',
                                               password_element=self.PASSWORD, password_text='paerugehr#$5^.35>>>')
        # Assert error message for invalid email format
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Adresa de email este invalida.')