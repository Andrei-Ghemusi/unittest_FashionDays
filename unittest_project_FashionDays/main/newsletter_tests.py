from selenium.webdriver.remote.webelement import WebElement
from main.setups import MainPageSetupAndTearDown
from main.test_methods import TestUtils

# This class contains positive and usability tests for the Newsletter
class PositiveNewsletterTests(MainPageSetupAndTearDown):

    """
        The following checks if a chosen element is displayed and if it has the chosen expected text.
        This is NOT a test, but a method called in tests - its purpose is being reused.
    """
    def check_element_presence_and_text(self, element, expected_text):
        actual_text = element.text
        self.scroll_to_element(element)
        # here we call the 'scroll_to_element' method from MainPageSetupAndTearDown
        is_present: bool = element.is_displayed()
        self.assertTrue(is_present)
        self.assertIn(expected_text, actual_text)


    # This method checks if the 'submit_for_women' button is displayed and has the expected text
    def test_displayed_text_for_women_button(self):
        button_women: WebElement = self.chrome.find_element(*self.FOR_WOMEN_SUBMIT)
        self.check_element_presence_and_text(button_women,
                                             expected_text='OFERTE PENTRU FEMEI') # this is just preference if we want to create the variable before or create it inside the argument
        # we add the desired arguments and call the method


    # This method checks if the 'submit_for_men' button is displayed and has the expected text
    def test_displayed_text_for_men_button(self):
        button_men: WebElement = self.chrome.find_element(*self.FOR_MEN_SUBMIT)
        self.check_element_presence_and_text(button_men,
                                             expected_text='OFERTE PENTRU BARBATI')


    # This method checks if the checkbox is displayed and has the expected text
    def test_checkbox(self):
        checkbox: WebElement = self.chrome.find_element(*self.CHECKBOX_AGE)
        expected_text: str = 'Confirm ca am peste 16 ani.'
        self.check_element_presence_and_text(checkbox, expected_text) # here we use the already made "expected_text" variable


    # This method checks if the protection and privacy text is present and has the correct text
    def test_site_protection_and_privacy(self):
        protection: WebElement = self.chrome.find_element(*self.SITE_PROTECTION_TEXT)
        expected_text: str = 'This site is protected by reCAPTCHA and the Google'
        self.check_element_presence_and_text(protection, expected_text)


    """
        The following method checks the text of an element, then after clicking on it if the url we are being sent to is the chosen-expected one.
        This is NOT a test, but a method called in tests - its purpose is being reused.
    """
    def check_element_text_and_url_after_click(self, element_data):
        for element_locator, expected_text, expected_url in element_data:
            element: WebElement = self.chrome.find_element(*element_locator)
            self.scroll_to_element(element)
            actual_text: str = element.text
            self.assertIn(expected_text, actual_text)
            element.click()
            actual_url: str = self.chrome.current_url
            self.assertEqual(expected_url, actual_url)


    # This method checks the text of the 'terms_of_service' element and after clicking on it that it sends us to the right url
    def test_click_terms_of_service(self):
        element_data_terms: list[tuple[tuple[str, str], str, str]] = [(self.TERMS_OF_SERVICE, 'Terms of Service', 'https://policies.google.com/terms')]
        self.check_element_text_and_url_after_click(element_data_terms)


    # This method checks the text of the 'privacy_policy' element and after clicking on it that it sends us to the right url
    def test_click_privacy_policy(self):
        element_data_terms: list[tuple[tuple[str, str], str, str]] = [(self.PRIVACY_POLICY, 'Privacy Policy', 'https://policies.google.com/privacy')]
        self.check_element_text_and_url_after_click(element_data_terms)


    """
        The following method checks that after adding a correct email, and having the checkbox on and clicking on submit, captcha appears
        This is NOT a test, but a method called in tests - its purpose is being reused
    """
    def check_captcha_is_displayed(self, element, tuple_value):
        self.scroll_to_element(element)
        self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.CHECKBOX_AGE).click()
        self.chrome.find_element(*tuple_value).click()
        # when calling this method, the tuple argument will go here
        captcha_display: bool = self.chrome.find_element(*self.CAPTCHA).is_displayed()
        self.assertTrue(captcha_display, 'ERROR, CAPTCHA is not displayed')


    # This method checks that after providing the correct email, and checkbox being on, after clicking on the 'submit_for_men' button, captcha appears
    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_men(self):
        element: WebElement = self.chrome.find_element(*self.FOR_MEN_SUBMIT)
        self.check_captcha_is_displayed(element, self.FOR_MEN_SUBMIT)
        # here we called the 'check_captcha_is_displayed' with the desired arguments


    # This method checks that after providing the correct email, and checkbox being on, after clicking on the 'submit_for_women' button, captcha appears
    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_women(self):
        element = self.chrome.find_element(*self.FOR_WOMEN_SUBMIT)
        self.check_captcha_is_displayed(element, self.FOR_WOMEN_SUBMIT)



class NegativeNewsletterTests(MainPageSetupAndTearDown):

    """
        This following method checks the newsletter subscription with various inputs
        It has 3 params, 2 which I set to "None" in case I do not want them used
        This is NOT a test, but a method called in tests - its purpose is being reused
    """
    def submission_with_various_inputs(self, expected_error, error_locator, email=None, checkbox=None):
        button_women: WebElement = self.chrome.find_element(*self.FOR_WOMEN_SUBMIT)
        self.scroll_to_element(button_women)

        if email is not None: # if as an argument the email is set to 'None', or omitted then 'if' goes to 'pass'
            self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys(email)

        if checkbox is not None: # if as an argument the checkbox is set to 'None', or omitted then 'if' goes to 'pass'
            self.chrome.find_element(*checkbox).click()

        self.chrome.find_element(*self.FOR_WOMEN_SUBMIT).click()
        error_message_element = self.chrome.find_element(*error_locator)
        actual_error: str = error_message_element.text
        self.assertEqual(expected_error, actual_error, f'ERROR, expected {expected_error}, but got {actual_error}')
        # this asserts that the expected error is the same with the actual_error


    # This method tests that when having no email input and checkbox being off, after clicking on submit we receive the expected error
    def test_newsletter_no_email_checkbox_off(self):
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.submission_with_various_inputs(expected_error, self.MAIL_NEWSLETTER_ERROR)
        # here we only used one argument when we called the 'submission_with_various_inputs'


    # This method tests that when having no email input and checkbox being on, after clicking on submit we receive the expected error
    def test_newsletter_no_email_checkbox_on(self):
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.submission_with_various_inputs(expected_error, self.MAIL_NEWSLETTER_ERROR, None, self.CHECKBOX_AGE)
        # here we used 2 arguments and set email to None, because we are not using it


    # This method tests that when having an invalid email input and checkbox on, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_letters_only_checkbox_on(self):
        email = 'wrong-email'
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.submission_with_various_inputs(expected_error, self.MAIL_NEWSLETTER_ERROR, email, self.CHECKBOX_AGE)
        # here we used all 3 arguments


    # This method tests that when having an invalid email input and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_letters_only_checkbox_off(self):
        self.submission_with_various_inputs(expected_error='Te rugam sa introduci o adresa de email valida.',
                                            error_locator=self.MAIL_NEWSLETTER_ERROR ,
                                            email='wrong-email')


    # This method tests that when having an invalid email input with special characters only and checkbox on, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_special_characters_checkbox_on(self):
        self.submission_with_various_inputs(expected_error='Te rugam sa introduci o adresa de email valida.',
                                            error_locator=self.MAIL_NEWSLETTER_ERROR,
                                            email='%$#^&&%$%&>>@@@%$^7..', checkbox=self.CHECKBOX_AGE)


    # This method tests that when having an invalid email input with special characters only and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_invalid_email_special_characters_checkbox_off(self):
        self.submission_with_various_inputs(expected_error='Te rugam sa introduci o adresa de email valida.',
                                            error_locator=self.MAIL_NEWSLETTER_ERROR,
                                            email='%$#^&&%$%&>>@@@%$^7..')


    # This method tests that when having a correct email input and checkbox off, after clicking on submit we receive the expected error
    def test_newsletter_valid_email_checkbox_off(self):
        self.submission_with_various_inputs(expected_error='Trebuie sa ai cel putin 16 ani pentru a te abona.',
                                            error_locator=self.NO_CHECKBOX_ERROR,
                                            email='pythontestemail083@gmail.com')
