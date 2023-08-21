from unittest import TestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests


# This class has the setup and teardown methods used for the tests on the Main Page
# It also contains all the tuples used for the tests on the Main Page
class MainPageSetupAndTearDown(TestCase):
    chrome: WebDriver
    AUTHENTICATION_PAGE: tuple[str, str] = (By.CSS_SELECTOR, '.icon-fdux_profile')
    CLOTHING: tuple[str, str] = (By.XPATH, '//*[@id="main-menu"]/div[2]/nav[1]/ul/li[2]/span')
    DRESSES: tuple[str, str] = (By.XPATH, '//*[@id="main-menu"]/div[2]/nav[1]/ul/li[2]/div/div[2]/a[2]/span[1]')
    SHOES: tuple[str, str] = (By.XPATH, '//*[@id="main-menu"]/div[2]/nav[1]/ul/li[3]/span')
    SANDALS: tuple[str, str] = (By.XPATH, '//*[@id="main-menu"]/div[2]/nav[1]/ul/li[3]/div/div[2]/a[3]/span[1]')
    OUTLET: tuple[str, str] = (By.XPATH, '//*[@id="main-menu"]/div[2]/nav[1]/ul/li[8]/span')
    OUTLET_PRICES: tuple[str, str] = (By.XPATH, '//span[@class="sale-price new-price"]')
    UNDER50: tuple[str, str] = (By.XPATH, '//*[@id="main-menu"]/div[2]/nav[1]/ul/li[8]/div/div[2]/a[15]/span')
    END_OF_SEASON_PROMOTION: tuple[str, str] = (By.XPATH, '//*[@id="homepage"]/div[2]/div[2]/div/a[1]/div/div[1]/h1')
    GARAGE_SALE_PROMOTION: tuple[str, str] = (By.XPATH, '//*[@id="homepage"]/div[3]/div/div/div/div/a/img[1]')
    GOODBYE_SUMMER_PROMOTION: tuple[str, str] = (By.XPATH, '//*[@id="homepage"]/div[8]/div/div/div/div/a/img[1]')
    ANPC: tuple[str, str] = (By.XPATH, '//*[@id="support-links"]/div[1]/ul/li[10]/a')
    MEN: tuple[str, str] = (By.XPATH, '//*[text()="Barbati"]')
    WOMEN: tuple[str, str] = (By.XPATH, '//*[@id="tag-menu"]/ul/li[1]/a')
    GIRLS: tuple[str, str] = (By.XPATH, '//*[@id="tag-menu"]/ul/li[3]/a')
    BOYS: tuple[str, str] = (By.XPATH, '//*[text() = "Baieti"]')
    ANPC_TEXT: tuple[str, str] = (By.XPATH, '//*[text()="Soluționarea Alternativă a Litigiilor"]')
    FACEBOOK: tuple[str, str] = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/ul/li[1]/a')
    INSTAGRAM: tuple[str, str] = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/ul/li[2]/a')
    TIKTOK: tuple[str, str] = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/ul/li[3]/a')
    NEWSLETTER_EMAIL: tuple[str, str]  = (By.XPATH, '//*[@id="form_email"]')
    CHECKBOX_AGE: tuple[str, str]  = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[1]/div/div[2]/label/span')
    FOR_MEN_SUBMIT: tuple[str, str]  = (By.XPATH, '//*[@id="form_saveMen"]')
    FOR_WOMEN_SUBMIT: tuple[str, str]  = (By.XPATH, '//*[@id="form_saveWomen"]')
    MAIL_NEWSLETTER_ERROR: tuple[str, str]  = (By.XPATH, '//*[@id="newsletter-form"]/div[1]/span/div[2]/span[2]')
    NO_CHECKBOX_ERROR: tuple[str, str]  = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[1]/div/div[1]/div[2]/span[2]')
    CAPTCHA: tuple[str, str]  = (By.XPATH, '//div[@class="g-recaptcha"]')
    SITE_PROTECTION_TEXT: tuple[str, str]  = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[3]/div[3]/small')
    PRIVACY_POLICY: tuple[str, str]  = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[3]/div[3]/small/a[1]')
    TERMS_OF_SERVICE: tuple[str, str]  = (By.XPATH, '//*[@id="newsletter-form"]/div[2]/div[3]/div[3]/small/a[2]')
    ANPC_COOKIES: tuple[str, str] = (By.XPATH, '//*[text()="Acceptă"]')

    # this is the setup method, it will run at the beginning of any test
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        url = 'https://www.fashiondays.ro/'
        self.chrome.get(url)
        response = requests.head(url)
        self.assertEqual(200, response.status_code,
                         f'ERROR, was expecting status code 200 but got {response.status_code}')
        try:
            self.chrome.find_element(By.XPATH, '//*[text()="Accept"]').click()
        except NoSuchElementException:
            pass
        self.chrome.implicitly_wait(2)


    # this is the tearDown, it'll run at the END of any and every test
    def tearDown(self) -> None:
        self.chrome.quit()



# This class has the setup and teardown methods used for the tests on the Authentication Page
# It also contains all the tuples used for the tests on the Authentication Page
class AuthenticationPageSetupAndTearDown(TestCase):
    LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//input[@type="submit" and @id="pizokel_customer_submit"]')
    EMAG_LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="login"]/div[4]/div[1]/button/div/span[2]')
    GMAIL_LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="login"]/div[4]/div[3]/button')
    APPLE_LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="login"]/div[4]/div[4]/button')
    EMAIL_ERROR: tuple[str, str] = (By.XPATH, '//*[@id="loginform"]/div[1]/div')
    PASSWORD_ERROR: tuple[str, str] = (By.XPATH, '//*[@id="loginform"]/div[2]/div')
    EMAIL: tuple[str, str] = (By.XPATH, '//*[@id ="email"]')
    PASSWORD: tuple[str, str] = (By.XPATH, '//*[@id="password"]')
    ACCOUNT: tuple[str, str] = (By.XPATH, '//*[@id="customer-account"]/div[1]/i')
    FACEBOOK_LOGIN_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="login"]/div[4]/div[2]/button/div/span[2]')
    FACEBOOK_COOKIES: tuple[str, str] = (By.XPATH, '//button[text()="Allow all cookies"]')
    FACEBOOK_EMAIL: tuple[str, str] = (By.XPATH, '//*[@id="email"]')
    FACEBOOK_PASSWORD: tuple[str, str] = (By.XPATH, '//*[@id="pass"]')
    FACEBOOK_POP_UP_LOGIN: tuple[str, str] = (By.XPATH, '//*[@id="loginbutton"]')
    LOGOUT: tuple[str, str] = (By.XPATH, '//*[text()="Logout"]')
    CONTUL_MEU_TEXT: tuple[str, str] = (By.XPATH, '//*[text()="Contul Meu"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        url: str = 'https://www.fashiondays.ro/customer/authentication'
        self.chrome.get(url)
        response = requests.head(url)
        self.assertEqual(200, response.status_code,
                         f'ERROR, was expecting status code 200 but got {response.status_code}')
        try:
            self.chrome.find_element(By.XPATH, '//*[text()="Accept"]').click()
        except NoSuchElementException:
            pass
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()


