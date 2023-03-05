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


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get('https://www.fashiondays.ro/')
        # self.chrome.find_element(By.XPATH, '//*[text()="Respinge"]').click()
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()



    def test_verify_base_page_url(self):
        base_page_url = self.chrome.current_url
        expected_base_page_url = 'https://www.fashiondays.ro/'
        self.assertEqual(base_page_url, expected_base_page_url), f'ERROR, expected {expected_base_page_url},  but got {base_page_url}'

    def test_verify_page_title(self):
        actual_page_title = self.chrome.title
        expected_title = 'Colectii de moda pentru femei'
        self.assertEqual(actual_page_title, expected_title), f'ERROR, expected page title {expected_title}, but got {actual_page_title}'

    def test_promotion_display(self):
        try:
            is_promotion_displayed = self.chrome.find_element(*self.PROMOTION).is_displayed()
            self.assertTrue(is_promotion_displayed), f'ERROR, promotion not displayed'
        except:
            print('Promotion is most likely no longer available')

    def test_campaign_redirect(self):
        try:
            self.chrome.find_element(*self.CAMPAIGN).click()
        except:
            print('Campaign expired.')
        campaign_page = self.chrome.window_handles[1]
        self.chrome.switch_to.window(campaign_page)
        actual_title = self.chrome.title
        expected_redirect_title = 'DISCLAIMER'
        time.sleep(2)
        assert actual_title == expected_redirect_title, f'Error, expected {expected_redirect_title}, but got {actual_title}'
        disclaimer_text = self.chrome.find_element(*self.DISCLAIMER_TEXT).text
        expected_disclaimer_text = 'FASHION DAYS - BIG SPRING ENERGY'
        assert disclaimer_text == expected_disclaimer_text, f'ERROR, expected {expected_disclaimer_text} but got {disclaimer_text}'

    def test_newsletter_invalid_email(self):
        pass

    def test_newsletter_valid_email_checkbox_off(self):
        pass

    def test_newsletter_valid_email_checkbox_on(self):
        pass
    #is captcha displayed


    def test_mens_page_url(self):
        self.chrome.find_element(*self.MEN).click()
        mens_url = self.chrome.current_url
        expected_mens_url = 'https://www.fashiondays.ro/t/barbati/'
        self.assertEqual(mens_url, expected_mens_url), f'Error, expected {expected_mens_url}, but got {mens_url}'

    def test_boys_page_url(self):
        self.chrome.find_element(*self.BOYS).click()
        boys_url = self.chrome.current_url
        expected_boys_url = 'https://www.fashiondays.ro/t/baieti/'
        self.assertEqual(boys_url, expected_boys_url), f'Error, expected {expected_boys_url}, but got {boys_url}'

    def test_girls_page_url(self):
        self.chrome.find_element(*self.GIRLS).click()
        girls_url = self.chrome.current_url
        expected_girls_url = 'https://www.fashiondays.ro/t/fete/'
        self.assertEqual(girls_url, expected_girls_url), f'Error, expected {expected_girls_url}, but got {girls_url}'

    def test_verify_authentication_url(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        actual_url = self.chrome.current_url
        expected_url = 'https://www.fashiondays.ro/customer/authentication'
        self.assertEqual(actual_url, expected_url), f'ERROR, expected {expected_url}, but got {actual_url}'

    def test_login_display(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        is_login_displayed = self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()
        self.assertTrue(is_login_displayed), f'Error, login button is not displayed'

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

    def test_invalid_email_and_password(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        self.chrome.find_element(*self.USERNAME).send_keys('wrong_username')
        self.chrome.find_element(*self.PASSWORD).send_keys('password')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_email_error = self.chrome.find_element(*self.EMAIL_ERROR).text
        expected_email_error = 'Adresa de email este invalida.'
        self.assertEqual(actual_email_error,expected_email_error), f'ERROR, expected {expected_email_error}, but got {actual_email_error}'

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



