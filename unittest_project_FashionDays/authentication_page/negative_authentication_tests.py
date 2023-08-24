from setups import AuthenticationPageSetupAndTearDown
from utility_methods import TestUtils


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
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.LOGIN_BUTTON, input_element_1=self.EMAIL,
                                        input_text_1='pythontestemail083@gmail.com')
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
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.LOGIN_BUTTON, input_element_2=self.PASSWORD,
                                        input_text_2='TestEmail123')
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
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.LOGIN_BUTTON, input_element_1=self.EMAIL,
                                        input_text_1='wrong_username', input_element_2=self.PASSWORD,
                                        input_text_2='password')
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
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.LOGIN_BUTTON, input_element_1=self.EMAIL,
                                        input_text_1='hgsyf$$%435@ii&&*)()u.com', input_element_2=self.PASSWORD,
                                        input_text_2='paerugehr#$5^.35>>>')
        # Assert error message for invalid email format
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.EMAIL_ERROR,
                                      expected_text='Adresa de email este invalida.')

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
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.LOGIN_BUTTON, input_element_1=self.EMAIL,
                                        input_text_1='pythontestemail083@gmail.com', input_element_2=self.PASSWORD,
                                        input_text_2='password')
        TestUtils.assert_text_message(self.chrome,
                                      self.EMAIL_ERROR,
                                      expected_text='Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.')

