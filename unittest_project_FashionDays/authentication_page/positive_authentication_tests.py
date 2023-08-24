# Import necessary modules and classes
import time
from setups import AuthenticationPageSetupAndTearDown
from utility_methods import TestUtils


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
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.LOGIN_BUTTON, input_element_1=self.EMAIL,
                                        input_text_1='pythontestemail083@gmail.com', input_element_2=self.PASSWORD,
                                        input_text_2='TestEmail123')
        self.account_status_check()


    def test_login_using_facebook(self):
        """
            Test case: Log in using Facebook

            Steps:
                1. Click on the Facebook login button.
                2. Switch to the popup window.
                3. Click on the Facebook cookies confirmation.
                4. Provide Facebook email and password.
                5. Click on the login button in the popup.
                6. Switch back to the main_page window.
                7. Verify the account status after successful login.

            Expected Result:
                Logging in using Facebook credentials should result in a successful login and the account status should be logged in.
        """
        TestUtils.click_element(self.chrome, self.FACEBOOK_LOGIN_BUTTON)
        all_handles = self.chrome.window_handles
        popup_window_handle = all_handles[-1]
        self.chrome.switch_to.window(popup_window_handle)
        TestUtils.click_element(self.chrome, self.FACEBOOK_COOKIES)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FACEBOOK_POP_UP_LOGIN,
                                        input_element_1=self.FACEBOOK_EMAIL,
                                        input_text_1='pythontestemail083@gmail.com',
                                        input_element_2=self.FACEBOOK_PASSWORD, input_text_2='TestEmail123')
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