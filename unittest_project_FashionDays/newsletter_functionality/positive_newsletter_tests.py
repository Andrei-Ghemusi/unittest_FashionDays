from setups import MainPageSetupAndTearDown
from utility_methods import TestUtils


# This class contains positive tests related to the newsletter subscription on the main_page page
class PositiveNewsletterTests(MainPageSetupAndTearDown):

    # Test case: Check if the 'Submit for Women' button is displayed with the correct text
    def test_displayed_text_for_women_button(self):
        """
        Steps:
            1. Move to the 'Submit for Women' button.
            2. Verify that the button is displayed.
            3. Verify that the button text matches the expected text 'OFERTE PENTRU FEMEI'.

        Expected Result:
            The 'Submit for Women' button is displayed and its text matches 'OFERTE PENTRU FEMEI'.
        """

        TestUtils.move_to_element(self.chrome, element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome, text_element=self.FOR_WOMEN_SUBMIT, expected_text='OFERTE PENTRU FEMEI')

    # Test case: Check if the 'Submit for Men' button is displayed with the correct text
    def test_displayed_text_for_men_button(self):
        """
        Steps:
            1. Move to the 'Submit for Men' button.
            2. Verify that the button is displayed.
            3. Verify that the button text matches the expected text 'OFERTE PENTRU BARBATI'.

        Expected Result:
            The 'Submit for Men' button is displayed and its text matches 'OFERTE PENTRU BARBATI'.
        """
        TestUtils.move_to_element(self.chrome, element=self.FOR_MEN_SUBMIT)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.FOR_MEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome, text_element=self.FOR_MEN_SUBMIT, expected_text='OFERTE PENTRU BARBATI')

    # Test case: Check if the checkbox for confirming age is displayed with the correct text
    def test_checkbox(self):
        """
        Steps:
            1. Move to the age confirmation checkbox.
            2. Verify that the checkbox is displayed.
            3. Verify that the checkbox label text matches the expected text 'Confirm ca am peste 16 ani.'

        Expected Result:
            The age confirmation checkbox is displayed and its label text matches 'Confirm ca am peste 16 ani.'.
        """
        TestUtils.move_to_element(self.chrome, element=self.CHECKBOX_AGE)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.CHECKBOX_AGE)
        TestUtils.assert_text_message(self.chrome, text_element=self.CHECKBOX_AGE, expected_text='Confirm ca am peste 16 ani.')

    # Test case: Check if the site protection and privacy text is displayed with the correct text
    def test_site_protection_and_privacy(self):
        """
        Steps:
            1. Move to the site protection and privacy text.
            2. Verify that the text is displayed.
            3. Verify that the text content matches the expected description.

        Expected Result:
            The site protection and privacy text is displayed and its content matches the expected description.
        """
        TestUtils.move_to_element(self.chrome, element=self.SITE_PROTECTION_TEXT)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.SITE_PROTECTION_TEXT)
        expected_description = "This site is protected by reCAPTCHA and the Google"
        TestUtils.assert_text_message(self.chrome, text_element=self.SITE_PROTECTION_TEXT, expected_text=expected_description)


    # Test case: Check if clicking on 'Terms of Service' link leads to the correct URL
    def test_click_terms_of_service(self):
        """
        Steps:
            1. Move to the 'Terms of Service' link.
            2. Verify that the link text matches the expected text 'Terms of Service'.
            3. Click on the 'Terms of Service' link.
            4. Verify that the current URL matches the expected URL 'https://policies.google.com/terms'.

        Expected Result:
            Clicking on the 'Terms of Service' link should lead to the URL 'https://policies.google.com/terms'.
        """
        TestUtils.move_to_element(self.chrome, element=self.TERMS_OF_SERVICE)
        TestUtils.assert_text_message(self.chrome, text_element=self.TERMS_OF_SERVICE, expected_text='Terms of Service')
        TestUtils.click_element(self.chrome, element=self.TERMS_OF_SERVICE)
        TestUtils.assert_current_url(self.chrome, expected_url='https://policies.google.com/terms')

    # Test case: Check if clicking on 'Privacy Policy' link leads to the correct URL
    def test_click_privacy_policy(self):
        """
        Steps:
            1. Move to the 'Privacy Policy' link.
            2. Verify that the link text matches the expected text 'Privacy Policy'.
            3. Click on the 'Privacy Policy' link.
            4. Verify that the current URL matches the expected URL 'https://policies.google.com/privacy'.

        Expected Result:
            Clicking on the 'Privacy Policy' link should lead to the URL 'https://policies.google.com/privacy'.
        """
        TestUtils.move_to_element(self.chrome, element=self.PRIVACY_POLICY)
        TestUtils.assert_text_message(self.chrome, text_element=self.PRIVACY_POLICY, expected_text='Privacy Policy')
        TestUtils.click_element(self.chrome, element=self.PRIVACY_POLICY)
        TestUtils.assert_current_url(self.chrome, expected_url='https://policies.google.com/privacy')


    # Test case: Check if captcha appears after submitting correct email with checkbox checked for 'Submit for Men'
    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_men(self):
        """
        Steps:
            1. Move to the 'Submit for Men' button.
            2. Check the age confirmation checkbox.
            3. Provide a correct email.
            4. Click on the 'Submit for Men' button.
            5. Verify that captcha element is displayed.

        Expected Result:
            After submitting the correct email and checking the checkbox, clicking on 'Submit for Men' should display captcha.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_MEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_MEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL,
                                        input_text_1='pythontestemail083@gmail.com')
        TestUtils.assert_is_element_displayed(self.chrome, self.CAPTCHA)


    # Test case: Check if captcha appears after submitting correct email with checkbox checked for 'Submit for Women'
    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_women(self):
        """
        Steps:
            1. Move to the 'Submit for Women' button.
            2. Check the age confirmation checkbox.
            3. Provide a correct email.
            4. Click on the 'Submit for Women' button.
            5. Verify that captcha element is displayed.

        Expected Result:
            After submitting the correct email and checking the checkbox, clicking on 'Submit for Women' should display captcha.
        """
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_inputs_and_click(self.chrome, button_element=self.FOR_WOMEN_SUBMIT,
                                        input_element_1=self.NEWSLETTER_EMAIL,
                                        input_text_1='pythontestemail083@gmail.com')
        TestUtils.assert_is_element_displayed(self.chrome, self.CAPTCHA)