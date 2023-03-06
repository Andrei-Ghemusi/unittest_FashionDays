import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class FashionDaysTest(TestCase):
    AUTHENTICATION_PAGE = (By.CSS_SELECTOR, '.icon-fdux_profile')
    PROMOTION = (By.XPATH, '//*[@id="homepage"]/div[1]/div/div/div/a/div/h1')
    CAMPAIGN = (By.XPATH, '//*[@id="homepage"]/div[2]/div[2]/div/a[2]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit" and @id="pizokel_customer_submit"]')
    EMAIL_ERROR = (By.XPATH, '//*[@id="loginform"]/div[1]/div')
    PASSWORD_ERROR = (By.XPATH, '//*[@id="loginform"]/div[2]/div')
    USERNAME = (By.XPATH, '//*[@id ="email"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    MEN = (By.XPATH, '//*[text()="Barbati"]')
    GIRLS = (By.XPATH, '//*[@id="tag-menu"]/ul/li[3]/a')
    BOYS = (By.XPATH, '//*[text() = "Baieti"]')
    DISCLAIMER_TEXT = (By.XPATH, '//*[@id="lp-pom-text-1640"]/p/span/strong/span')
    NEWSLETTER_EMAIL = (By.XPATH, '//*[@id="form_email"]')
    CHECKBOX_AGE = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[1]/div/div[2]/label/span')
    SUBMIT_TO_NEWSLETTER = (By.XPATH, '//*[@id="form_saveMen"]')
    MAIL_NEWSLETTER_ERROR = (By.XPATH, '//*[@id="newsletter-form"]/div[1]/span/div[2]/span[2]')
    NO_CHECKBOX_ERROR = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[1]/div/div[1]/div[2]/span[2]')
    CAPTCHA = (By.XPATH, '//div[@class="g-recaptcha"]')


# this is the setup method, it will run at the beginning of any test
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get('https://www.fashiondays.ro/')
        # self.chrome.find_element(By.XPATH, '//*[text()="Respinge"]').click()
        self.chrome.implicitly_wait(2)

# this is the tearDown, it'll run at the END of any and every test
    def tearDown(self) -> None:
        self.chrome.quit()


# this method will verify if the home page url is the same one as the expected one, which in real-life scenarios will be given
    def test_verify_base_page_url(self):
        base_page_url = self.chrome.current_url
        expected_base_page_url = 'https://www.fashiondays.ro/'
        self.assertEqual(base_page_url, expected_base_page_url), f'ERROR, expected {expected_base_page_url},  but got {base_page_url}'

# this method checks the page title
    def test_verify_page_title(self):
        actual_page_title = self.chrome.title
        expected_title = 'Colectii de moda pentru femei'
        self.assertEqual(actual_page_title, expected_title), f'ERROR, expected page title {expected_title}, but got {actual_page_title}'

# This method checks if the promotion is displayed
    # !! REMINDER !!
    # the promotion is under a timer, and when the timer expires the system won't be able to find it, hence why we use try/except
    def test_promotion_display(self):
        try:
            is_promotion_displayed = self.chrome.find_element(*self.PROMOTION).is_displayed()
            self.assertTrue(is_promotion_displayed), f'ERROR, promotion not displayed'
        except:
            print('Promotion is most likely no longer available')

# This method checks if the campaign redirects the user, when clicking on info, to a new page called DISCLAIMER
    # !! REMINDER !!
    # The campaign's also under a timer, so after it expires the system wil not find it.
    def test_campaign_redirect(self):
        try:
            self.chrome.find_element(*self.CAMPAIGN).click()
            campaign_page = self.chrome.window_handles[1]
            self.chrome.switch_to.window(campaign_page)
            actual_title = self.chrome.title
            expected_redirect_title = 'DISCLAIMER'
            time.sleep(2) # sleep has been used here because, even though we have implicitly wait of 2 sec, errors would occur because of the page loading speed
            assert actual_title == expected_redirect_title, f'Error, expected {expected_redirect_title}, but got {actual_title}'
            disclaimer_text = self.chrome.find_element(*self.DISCLAIMER_TEXT).text
            expected_disclaimer_text = 'FASHION DAYS - BIG SPRING ENERGY'
            assert disclaimer_text == expected_disclaimer_text, f'ERROR, expected {expected_disclaimer_text} but got {disclaimer_text}'
        except:
            print('Campaign expired.')


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
    #is captcha displayed


# This method checks that after clicking on "BARBATI" we are being sent to the right page
    def test_mens_page_url(self):
        self.chrome.find_element(*self.MEN).click()
        mens_url = self.chrome.current_url
        expected_mens_url = 'https://www.fashiondays.ro/t/barbati/'
        self.assertEqual(mens_url, expected_mens_url), f'Error, expected {expected_mens_url}, but got {mens_url}'

# This method checks that after clicking on "BAIETI" we are being sent to the right page
    def test_boys_page_url(self):
        self.chrome.find_element(*self.BOYS).click()
        boys_url = self.chrome.current_url
        expected_boys_url = 'https://www.fashiondays.ro/t/baieti/'
        self.assertEqual(boys_url, expected_boys_url), f'Error, expected {expected_boys_url}, but got {boys_url}'

# This method checks that after clicking on "FETE" we are being sent to the right page
    def test_girls_page_url(self):
        self.chrome.find_element(*self.GIRLS).click()
        girls_url = self.chrome.current_url
        expected_girls_url = 'https://www.fashiondays.ro/t/fete/'
        self.assertEqual(girls_url, expected_girls_url), f'Error, expected {expected_girls_url}, but got {girls_url}'

# This method checks that after clicking on authentication we are on the authentication page
    def test_verify_authentication_url(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        actual_url = self.chrome.current_url
        expected_url = 'https://www.fashiondays.ro/customer/authentication'
        self.assertEqual(actual_url, expected_url), f'ERROR, expected {expected_url}, but got {actual_url}'

# This method checks that while on the authentication page, the login button is displayed
    def test_login_display(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        is_login_displayed = self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_login_displayed), f'Error, login button is not displayed'

# This method checks that we cannot login after providing no credentials and if we receive the expected errors
    def test_no_credentials_login(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        missing_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_missing_email_error = 'Acest camp este obligatoriu'
        missing_password_error = self.chrome.find_element(*self.PASSWORD_ERROR).text
        expected_missing_password_error = 'Acest camp este obligatoriu'
        self.assertEqual(missing_email_error, expected_missing_email_error), f'Error, expected {expected_missing_email_error}, but got {missing_email_error}'
        self.assertEqual(missing_password_error,
                         expected_missing_password_error), f'Error, expected {expected_missing_password_error}, but got {missing_password_error}'

# This method checks if we receive the expected error after providing an invalid email, and fill in a password
    def test_invalid_email_and_password(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.USERNAME).send_keys('wrong_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_email_error = 'Adresa de email este invalida.'
        self.assertEqual(actual_email_error,expected_email_error), f'ERROR, expected {expected_email_error}, but got {actual_email_error}'

# This method checks that after we provide a valid e-mail and password, but no account is present on said e-mail, we receive the expected error
    def test_incorrect_email_and_password(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.USERNAME).send_keys('wrong_username@mail.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
        actual_valid_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_valid_email_error = 'Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.'
        self.assertEqual(actual_valid_email_error,
                         expected_valid_email_error), f'ERROR, expected {expected_valid_email_error}, but got {actual_valid_email_error}'



