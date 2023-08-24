from setups import MainPageSetupAndTearDown
from utility_methods import TestUtils

# This class contains negative tests related to the newsletter subscription on the main_page page
class NegativeNewsletterTests(MainPageSetupAndTearDown):


    # This method tests that when having no email input and checkbox being off, after clicking on submit we receive the expected error
    def test_newsletter_no_email_checkbox_off(self):
        """
            Steps:
                1. Move to the 'Submit for Women' button.
                2. Click on the 'Submit for Women' button without providing an email and with checkbox off.
                3. Verify that the error message matches the expected text 'Te rugam sa introduci o adresa de email valida.'

            Expected Result:
                Clicking on 'Submit for Women' without providing an email and with checkbox off should display the error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having no email input and checkbox being on, after clicking on submit we receive the expected error
    def test_newsletter_no_email_checkbox_on(self):
        """
            Steps:
               1. Move to the 'Submit for Women' button.
               2. Check the age confirmation checkbox.
               3. Click on the 'Submit for Women' button without providing an email.
               4. Verify that the error message matches the expected text 'Te rugam sa introduci o adresa de email valida.'

            Expected Result:
               Clicking on 'Submit for Women' without providing an email but with checkbox on should display the error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input and checkbox on, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_letters_only_checkbox_on(self):
        """
            Steps:
                1. Move to the 'Submit for Women' button.
                2. Check the age confirmation checkbox.
                3. Provide an invalid email (e.g., 'wrong-email').
                4. Click on the 'Submit for Women' button.
                5. Verify that the error message matches the expected text 'Te rugam sa introduci o adresa de email valida.'

            Expected Result:
                Providing an invalid email and clicking on 'Submit for Women' with checkbox on should display the error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL, input_text_1='wrong-email')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_letters_only_checkbox_off(self):
        """
            Steps:
                1. Move to the 'Submit for Women' button.
                2. Provide an invalid email (e.g., 'wrong-email').
                3. Click on the 'Submit for Women' button.
                4. Verify that the error message matches the expected text 'Te rugam sa introduci o adresa de email valida.'

            Expected Result:
                Providing an invalid email and clicking on 'Submit for Women' with checkbox off should display the error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL, input_text_1='wrong-email')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input with special characters only and checkbox on, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_special_characters_checkbox_on(self):
        """
            Steps:
                1. Move to the 'Submit for Women' button.
                2. Check the age confirmation checkbox.
                3. Provide an invalid email with special characters.
                4. Click on the 'Submit for Women' button.
                5. Verify that the error message matches the expected text 'Te rugam sa introduci o adresa de email valida.'

            Expected Result:
                Providing an invalid email with special characters and clicking on 'Submit for Women' with checkbox on should display the error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL,
                                        input_text_1='#@$@#%^&^*&(%%#$@#12335.gf.sgs')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input with special characters only and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_special_characters_checkbox_off(self):
        """
            Steps:
                1. Move to the 'Submit for Women' button.
                2. Provide an invalid email with special characters.
                3. Click on the 'Submit for Women' button.
                4. Verify that the error message matches the expected text 'Te rugam sa introduci o adresa de email valida.'

            Expected Result:
                Providing an invalid email with special characters and clicking on 'Submit for Women' with checkbox off should display the error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL,
                                        input_text_1='#@$@#%^&^*&(%%#$@#12335.gf.sgs')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having a correct email input and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_valid_email_checkbox_off(self):
        """
            Steps:
                1. Move to the 'Submit for Women' button.
                2. Provide a correct email.
                3. Click on the 'Submit for Women' button.
                4. Verify that the error message matches the expected text 'Trebuie sa ai cel putin 16 ani pentru a te abona.'

            Expected Result:
                Providing a correct email and clicking on 'Submit for Women' with checkbox off should display the age restriction error message.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL,
                                        input_text_1='pythontestemail083@gmail.com')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.NO_CHECKBOX_ERROR,
                                      expected_text='Trebuie sa ai cel putin 16 ani pentru a te abona.')