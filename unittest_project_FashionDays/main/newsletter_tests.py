import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import unittest
from main.setups import MainPageSetupAndTearDown
from main.non_functional_tests import NonFunctionalTestsMainPage


class PositiveNewsletterTests(MainPageSetupAndTearDown):

    def check_element_presence_and_text(self, element, expected_text):
        actual_text = element.text
        self.scroll_to_element(element)
        is_present: bool = element.is_displayed()
        self.assertTrue(is_present)
        self.assertIn(expected_text, actual_text)

    def test_for_women_button(self):
        button_women: WebElement = self.chrome.find_element(*self.FOR_WOMEN_SUBMIT)
        expected_text: str = 'OFERTE PENTRU FEMEI'
        self.check_element_presence_and_text(button_women, expected_text)

    def test_for_men_button(self):
        button_men: WebElement = self.chrome.find_element(*self.FOR_MEN_SUBMIT)
        expected_text: str = 'OFERTE PENTRU BARBATI'
        self.check_element_presence_and_text(button_men, expected_text)

    def test_checkbox(self):
        checkbox: WebElement = self.chrome.find_element(*self.CHECKBOX_AGE)
        expected_text: str = 'Confirm ca am peste 16 ani.'
        self.check_element_presence_and_text(checkbox, expected_text)

    def test_site_protection_and_privacy(self):
        protection: WebElement = self.chrome.find_element(*self.SITE_PROTECTION_TEXT)
        expected_text: str = 'This site is protected by reCAPTCHA and the Google'
        self.check_element_presence_and_text(protection, expected_text)


    def check_element_text_and_url_after_click(self, element, expected_text, expected_url):
        self.scroll_to_element(element)
        actual_text: str = element.text
        self.assertIn(expected_text, actual_text)
        element.click()
        actual_url: str = self.chrome.current_url
        self.assertEqual(expected_url, actual_url)

    def test_click_privacy_policy(self):
        privacy_policy_element: WebElement = self.chrome.find_element(*self.PRIVACY_POLICY)
        expected_url: str = 'https://policies.google.com/privacy'
        expected_text: str = 'Privacy Policy'
        self.check_element_text_and_url_after_click(privacy_policy_element, expected_text, expected_url)

    def test_click_terms_of_service(self):
        terms_of_service_element: WebElement = self.chrome.find_element(*self.TERMS_OF_SERVICE)
        expected_url: str = 'https://policies.google.com/terms'
        expected_text: str = 'Terms of Service'
        self.check_element_text_and_url_after_click(terms_of_service_element, expected_text, expected_url)

    def check_captcha_is_displayed(self, element, tuple_value):
        self.scroll_to_element(element)
        self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys('pythontestemail083@gmail.com')
        self.chrome.find_element(*self.CHECKBOX_AGE).click()
        self.chrome.find_element(*tuple_value).click()
        captcha_display: bool = self.chrome.find_element(*self.CAPTCHA).is_displayed()
        self.assertTrue(captcha_display, 'ERROR, CAPTCHA is not displayed')

    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_men(self):
        element = self.chrome.find_element(*self.FOR_MEN_SUBMIT)
        self.check_captcha_is_displayed(element, self.FOR_MEN_SUBMIT)

    def test_captcha_newsletter_correct_email_checkbox_on_submit_for_women(self):
        element = self.chrome.find_element(*self.FOR_WOMEN_SUBMIT)
        self.check_captcha_is_displayed(element, self.FOR_WOMEN_SUBMIT)


class NegativeNewsletterTests(MainPageSetupAndTearDown):

    def whatever4(self, expected_error, email=None, checkbox=None):
        button_women: WebElement = self.chrome.find_element(*self.FOR_WOMEN_SUBMIT)
        self.scroll_to_element(button_women)
        if email is None:
            pass
        else:
            self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys(email)
        self.chrome.find_element(*self.FOR_MEN_SUBMIT).click()
        if checkbox is None:
            pass
        else:
            self.chrome.find_element(*checkbox).click()
        actual_error: str = self.chrome.find_element(*self.MAIL_NEWSLETTER_ERROR).text
        self.assertEqual(expected_error, actual_error, f'ERROR, expected {expected_error}, but got {actual_error}')


    def test_newsletter_no_email_checkbox_off(self):
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.whatever4(expected_error)


    def test_newsletter_no_email_checkbox_on(self):
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.whatever4(expected_error, None, self.CHECKBOX_AGE)


    def test_newsletter_invalid_email_letters_only_checkbox_on(self):
        email = 'wrong-email'
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.whatever4(expected_error, email, self.CHECKBOX_AGE)

    def test_newsletter_invalid_email_letters_only_checkbox_off(self):
        self.whatever4(expected_error='Te rugam sa introduci o adresa de email valida.', email='wrong-email')


    def test_newsletter_invalid_email_special_characters_checkbox_on(self):
        self.whatever4(expected_error='Te rugam sa introduci o adresa de email valida.', email='%$#^&&%$%&>>@@@%$^7..', checkbox=self.CHECKBOX_AGE)


    def test_newsletter_invalid_email_special_characters_checkbox_off(self):
        self.whatever4(expected_error='Te rugam sa introduci o adresa de email valida.', email='%$#^&&%$%&>>@@@%$^7..')


    def test_newsletter_valid_email_checkbox_off(self):
        email = 'pythontestemail083@gmail.com'
        expected_error = 'Trebuie sa ai cel putin 16 ani pentru a te abona.'
        self.whatever4(expected_error, email)
