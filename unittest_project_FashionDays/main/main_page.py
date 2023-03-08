import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MainPageTests(TestCase):
    AUTHENTICATION_PAGE = (By.CSS_SELECTOR, '.icon-fdux_profile')
    PROMOTION = (By.XPATH, '//*[@id="homepage"]/div[1]/div/div/div/a/div/h1')
    CAMPAIGN = (By.XPATH, '//*[@id="homepage"]/div[2]/div[2]/div/a[2]')
    MEN = (By.XPATH, '//*[text()="Barbati"]')
    GIRLS = (By.XPATH, '//*[@id="tag-menu"]/ul/li[3]/a')
    BOYS = (By.XPATH, '//*[text() = "Baieti"]')
    DISCLAIMER_TEXT = (By.XPATH, '//*[@id="lp-pom-text-1640"]/p/span/strong/span')


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
    #@unittest.skip  #!!! this skips the test if you uncomment it
    def test_promotion_display(self):
        try:
            is_promotion_displayed = self.chrome.find_element(*self.PROMOTION).is_displayed()
            self.assertTrue(is_promotion_displayed), f'ERROR, promotion not displayed'
        except:
            print('Promotion is most likely no longer available')

# This method checks if the campaign redirects the user, when clicking on info, to a new page called DISCLAIMER
    # !! REMINDER !!
    # The campaign's also under a timer, so after it expires the system wil not find it.
    # @unittest.skip
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




