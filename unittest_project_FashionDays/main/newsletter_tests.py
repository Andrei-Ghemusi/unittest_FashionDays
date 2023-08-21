from main.setups import MainPageSetupAndTearDown
from main.utility_methods import TestUtils

# This class contains positive and usability tests for the Newsletter
class PositiveNewsletterTests(MainPageSetupAndTearDown):

    # This method checks if the 'submit_for_women' button is displayed and has the expected text
    def test_displayed_text_for_women_button(self):
        TestUtils.move_to_element(self.chrome, element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome, text_element=self.FOR_WOMEN_SUBMIT, expected_text='OFERTE PENTRU FEMEI')


    # This method checks if the 'submit_for_men' button is displayed and has the expected text
    def test_displayed_text_for_men_button(self):
        TestUtils.move_to_element(self.chrome, element=self.FOR_MEN_SUBMIT)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.FOR_MEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome, text_element=self.FOR_MEN_SUBMIT, expected_text='OFERTE PENTRU BARBATI')


    # This method checks if the checkbox is displayed and has the expected text
    def test_checkbox(self):
        TestUtils.move_to_element(self.chrome, element=self.CHECKBOX_AGE)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.CHECKBOX_AGE)
        TestUtils.assert_text_message(self.chrome, text_element=self.CHECKBOX_AGE, expected_text='Confirm ca am peste 16 ani.')


    # This method checks if the protection and privacy text is present and has the correct text
    def test_site_protection_and_privacy(self):
        TestUtils.move_to_element(self.chrome, element=self.SITE_PROTECTION_TEXT)
        TestUtils.assert_is_element_displayed(self.chrome, element=self.SITE_PROTECTION_TEXT)
        TestUtils.assert_text_message(self.chrome, text_element=self.SITE_PROTECTION_TEXT, expected_text='This site is protected by reCAPTCHA and the Google')


    # This method checks the text of the 'terms_of_service' element and after clicking on it that it sends us to the right url
    def test_click_terms_of_service(self):
        TestUtils.move_to_element(self.chrome, element=self.TERMS_OF_SERVICE)
        TestUtils.assert_text_message(self.chrome, text_element=self.TERMS_OF_SERVICE, expected_text='Terms of Service')
        TestUtils.click_element(self.chrome, element=self.TERMS_OF_SERVICE)
        TestUtils.assert_current_url(self.chrome, expected_url='https://policies.google.com/terms')


    # This method checks the text of the 'privacy_policy' element and after clicking on it that it sends us to the right url
    def test_click_privacy_policy(self):
        TestUtils.move_to_element(self.chrome, element=self.PRIVACY_POLICY)
        TestUtils.assert_text_message(self.chrome, text_element=self.PRIVACY_POLICY, expected_text='Privacy Policy')
        TestUtils.click_element(self.chrome, element=self.PRIVACY_POLICY)
        TestUtils.assert_current_url(self.chrome, expected_url='https://policies.google.com/privacy')


    # This method checks that after providing the correct email, and checkbox being on, after clicking on the 'submit_for_men' button, captcha appears
    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_men(self):
        TestUtils.move_to_element(self.chrome, self.FOR_MEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='pythontestemail083@gmail.com',
                                               login_button_element=self.FOR_MEN_SUBMIT) # this is not a login button, but a submit
        TestUtils.assert_is_element_displayed(self.chrome, self.CAPTCHA)


    # This method checks that after providing the correct email, and checkbox being on, after clicking on the 'submit_for_women' button, captcha appears
    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_women(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='pythontestemail083@gmail.com',
                                               login_button_element=self.FOR_WOMEN_SUBMIT)  # this is not a login button, but a submit
        TestUtils.assert_is_element_displayed(self.chrome, self.CAPTCHA)



class NegativeNewsletterTests(MainPageSetupAndTearDown):


    # This method tests that when having no email input and checkbox being off, after clicking on submit we receive the expected error
    def test_newsletter_no_email_checkbox_off(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')

    # This method tests that when having no email input and checkbox being on, after clicking on submit we receive the expected error
    def test_newsletter_no_email_checkbox_on(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_email_and_password_keys(self.chrome, login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')

    # This method tests that when having an invalid email input and checkbox on, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_letters_only_checkbox_on(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='wrong-email',
                                               login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_letters_only_checkbox_off(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='wrong-email',
                                               login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input with special characters only and checkbox on, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_special_characters_checkbox_on(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.click_element(self.chrome, self.CHECKBOX_AGE)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='#@$@#%^&^*&(%%#$@#12335.gf.sgs',
                                               login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having an invalid email input with special characters only and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_special_characters_checkbox_off(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='#@$@#%^&^*&(%%#$@#12335.gf.sgs',
                                               login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.MAIL_NEWSLETTER_ERROR,
                                      expected_text='Te rugam sa introduci o adresa de email valida.')


    # This method tests that when having a correct email input and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_valid_email_checkbox_off(self):
        TestUtils.move_to_element(self.chrome, self.FOR_WOMEN_SUBMIT)
        TestUtils.send_email_and_password_keys(self.chrome,
                                               email_element=self.NEWSLETTER_EMAIL,
                                               email_text='pythontestemail083@gmail.com',
                                               login_button_element=self.FOR_WOMEN_SUBMIT)
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.NO_CHECKBOX_ERROR,
                                      expected_text='Trebuie sa ai cel putin 16 ani pentru a te abona.')
