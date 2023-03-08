import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class NewsletterTests(TestCase):
    NEWSLETTER_EMAIL = (By.XPATH, '//*[@id="form_email"]')
    CHECKBOX_AGE = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[1]/div/div[2]/label/span')
    SUBMIT_TO_NEWSLETTER = (By.XPATH, '//*[@id="form_saveMen"]')
    MAIL_NEWSLETTER_ERROR = (By.XPATH, '//*[@id="newsletter-form"]/div[1]/span/div[2]/span[2]')
    NO_CHECKBOX_ERROR = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[1]/div/div[1]/div[2]/span[2]')
    CAPTCHA = (By.XPATH, '//div[@class="g-recaptcha"]')


    # this is the setup method, it will run at the beginning of any test
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get('https://www.fashiondays.ro/')
        # self.chrome.find_element(By.XPATH, '//*[text()="Respinge"]').click()
        self.chrome.implicitly_wait(2)

    # this is the tearDown, it'll run at the END of any and every test
    def tearDown(self) -> None:
        self.chrome.quit()


# This method checks that if the user tries to subscribe to the newsletter without inserting an e-mail, they will receive the expected error
    def test_newsletter_no_email(self):
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="accept-cookie-policy"]').click() # if this is not implemented then it fails to click on submit
                                                                                          # after accepting once, the system might not show the cookies agreement, hence the try/except
        except:
            pass
        self.chrome.find_element(*self.SUBMIT_TO_NEWSLETTER).click()
        time.sleep(2) # the sleep gives the page time to load up the error message
        actual_error = self.chrome.find_element(*self.MAIL_NEWSLETTER_ERROR).text
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.assertEqual(actual_error, expected_error), f'ERROR, expected {expected_error}, but got {actual_error}'

# This method checks the error, if it appears, and the text, if the user inserted e-mail is invalid
    def test_newsletter_invalid_email(self):
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="accept-cookie-policy"]').click() #if this is not implemented then it fails to click on submit
        except:
            pass
        self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys('wrongemail')
        self.chrome.find_element(*self.CHECKBOX_AGE).click()
        time.sleep(2)
        self.chrome.find_element(*self.SUBMIT_TO_NEWSLETTER).click()
        actual_error = self.chrome.find_element(*self.MAIL_NEWSLETTER_ERROR).text
        expected_error = 'Te rugam sa introduci o adresa de email valida.'
        self.assertEqual(actual_error, expected_error), f'ERROR, expected {expected_error}, but got {actual_error}'

# This method checks the error, in case the inserted e-mail is valid, but the age checkbox is not checked
    def test_newsletter_valid_email_checkbox_off(self):
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="accept-cookie-policy"]').click() #if this is not implemented then it fails to click on submit
        except:
            pass
        self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys('wrongemail@test.com')
        self.chrome.find_element(*self.SUBMIT_TO_NEWSLETTER).click()
        actual_error = self.chrome.find_element(*self.NO_CHECKBOX_ERROR).text
        expected_error = 'Trebuie sa ai cel putin 16 ani pentru a te abona.'
        self.assertEqual(actual_error, expected_error), f'ERROR, expected {expected_error}, but got {actual_error}'

# This method checks that in the case the e-mail is valid and the checkbox is checked, after clicking on submit, that CAPTCHA will appear
    # !! REMINDER !!
    # There is a chance that CAPTCHA may not appear and the subscription will go through, this happened very few times
    def test_newsletter_valid_email_checkbox_on(self):
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="accept-cookie-policy"]').click() #if this is not implemented then it fails to click on submit
        except:
            pass
        self.chrome.find_element(*self.NEWSLETTER_EMAIL).send_keys('wrongemail@test.com')
        self.chrome.find_element(*self.CHECKBOX_AGE).click()
        self.chrome.find_element(*self.SUBMIT_TO_NEWSLETTER).click()
        time.sleep(5)
        captcha_display = self.chrome.find_element(*self.CAPTCHA)
        assert captcha_display.is_displayed() == True, 'ERROR, CAPTCHA is not displayed'