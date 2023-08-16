import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import unittest
from main.setups import MainPageSetupAndTearDown



class MainPageTests(MainPageSetupAndTearDown):
    AUTHENTICATION_PAGE = (By.CSS_SELECTOR, '.icon-fdux_profile')
    PROMOTION = (By.XPATH, '//*[@id="homepage"]/div[2]/div[2]/div/a[1]/div')
    ANPC = (By.XPATH, '//*[@id="support-links"]/div[1]/ul/li[10]/a')
    MEN = (By.XPATH, '//*[text()="Barbati"]')
    GIRLS = (By.XPATH, '//*[@id="tag-menu"]/ul/li[3]/a')
    BOYS = (By.XPATH, '//*[text() = "Baieti"]')
    ANPC_TEXT = (By.XPATH, '//*[text()="Soluționarea Alternativă a Litigiilor"]')
    FACEBOOK = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/ul/li[1]/a')
    INSTAGRAM = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/ul/li[2]/a')
    TIKTOK = (By.XPATH, '//*[@id="footer"]/div[1]/div/div/div[3]/div[2]/div[2]/div[1]/ul/li[3]/a')


# this method checks the page title
    def test_verify_page_title(self):
        actual_page_title: str = self.chrome.title
        expected_title: str = 'Colectii de moda pentru femei'
        self.assertEqual(actual_page_title, expected_title, f'ERROR, expected page title {expected_title}, but got {actual_page_title}')


### hover tests!!!




# This method checks if the promotion is displayed
    # !! REMINDER !!
    # the promotion is under a timer, and when the timer expires the system won't be able to find it, hence why we use try/except
    #@unittest.skip  #!!! this skips the test if you uncomment it
    def test_promotion_display(self):
        unavailable: str = 'Promotion is no longer available!'
        try:
            promotion_display: WebElement = self.chrome.find_element(*self.PROMOTION)
            promotion_display.is_displayed()
            self.assertTrue(promotion_display, f'{unavailable}')
        except:
            pass

    # this method checks that the link towards anpc works
    def test_anpc_redirect(self):
            self.chrome.execute_script("window.scrollTo(0,500);")
            # we scroll to the anpc link
            self.chrome.find_element(*self.ANPC).click()
            # we click on the link
            anpc_page: str = self.chrome.window_handles[1]
            self.chrome.switch_to.window(anpc_page)
            # we switch to the anpc tab
            anpc_url = self.chrome.current_url
            response = requests.head(anpc_url)
            # we use HEAD instead of GET to save resources because we are only checking if the link is broken
            self.assertEqual(200, response.status_code, f'expected status code is 200 but got {response.status_code}')
            # we check that we are getting the correct status code and that the link is not broken
            try:
                self.chrome.find_element(By.XPATH, '//*[text()="Acceptă"]').click()
            except:
                pass
            # we accept the cookies, also, I used try/except here because sometimes the cookie pop up won't appear
            actual_title: str = self.chrome.title
            expected_redirect_title: str = 'Ce este SAL ? | ANPC'
            time.sleep(3) # sleep has been used here because, even though we have an implicit wait of 2 sec, errors would occur because of the page loading speed
            self.assertEqual(actual_title, expected_redirect_title, f'Error, expected {expected_redirect_title}, but got {actual_title}')
            # here I verify that the page title is correct
            anpc_text: str = self.chrome.find_element(*self.ANPC_TEXT).text
            expected_anpc_text: str = 'Soluționarea Alternativă a Litigiilor'
            self.assertEqual(anpc_text, expected_anpc_text, f'ERROR, expected {expected_anpc_text} but got {anpc_text}')
            # and here that some of the text on the page is correct


# This method checks that after clicking on "BARBATI" we are being sent to the right page
    def test_mens_page_url(self):
        self.chrome.find_element(*self.MEN).click()
        mens_url: str = self.chrome.current_url
        expected_mens_url: str = 'https://www.fashiondays.ro/t/barbati/'
        self.assertEqual(mens_url, expected_mens_url, f'Error, expected {expected_mens_url}, but got {mens_url}')

# This method checks that after clicking on "BAIETI" we are being sent to the right page
    def test_boys_page_url(self):
        self.chrome.find_element(*self.BOYS).click()
        boys_url: str = self.chrome.current_url
        response = requests.head(boys_url)
        self.assertEqual(200, response.status_code)
        # here we check that the link is correct and not broken by verifying that the status code is correct

# This method checks that after clicking on "FETE" we are being sent to the right page
    def test_girls_page_url(self):
        self.chrome.find_element(*self.GIRLS).click()
        girls_url: str = self.chrome.current_url
        expected_girls_url: str = 'https://www.fashiondays.ro/t/fete/'
        self.assertEqual(girls_url, expected_girls_url, f'Error, expected {expected_girls_url}, but got {girls_url}')

# This method checks that after clicking on authentication we are on the authentication page
    def test_verify_authentication_url(self):
        self.chrome.find_element(*self.AUTHENTICATION_PAGE).click()
        actual_url: str = self.chrome.current_url
        expected_url: str = 'https://www.fashiondays.ro/customer/authentication'
        self.assertEqual(actual_url, expected_url, f'ERROR, expected {expected_url}, but got {actual_url}')

    # this method checks that the facebook link works fine
    def test_verify_facebook_link(self):
        self.chrome.execute_script('window.scrollTo(0, 500);')
        # we scroll down the page
        facebook_link: WebElement = self.chrome.find_element(*self.FACEBOOK)
        facebook_expected_href: str = 'https://www.facebook.com/fashiondays.romania/'
        facebook_actual_href: str = facebook_link.get_attribute('href')
        # from the element we get the attribute 'href' which contains the url
        self.assertEqual(facebook_expected_href, facebook_actual_href)
        # we check that the expected href is the same as the actual one
        facebook_link.click()
        facebook_window: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(facebook_window)
        # here we switch to the facebook window
        actual_url: str = self.chrome.current_url
        expected_url: str = 'https://www.facebook.com/fashiondays.romania/'
        self.assertEqual(expected_url,actual_url)
        # here we check that we are on the correct url
        actual_title: str = self.chrome.title
        expected_title: str = 'Fashion Days | Bucharest'
        self.assertEqual(expected_title, actual_title)
        # we check that the page title is the correct one

    # this method checks that the instagram link works fine
    def test_verify_instagram(self):
        self.chrome.execute_script('window.scrollTo(0,500);')
        instagram_link: WebElement = self.chrome.find_element(*self.INSTAGRAM)
        instagram_expected_href: str = "https://www.instagram.com/fashiondays/?hl=en"
        instagram_actual_href: str = instagram_link.get_attribute('href')
        self.assertEqual(instagram_expected_href, instagram_actual_href)
        instagram_link.click()
        instagram_window: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(instagram_window)
        actual_url: str = self.chrome.current_url
        expected_url = 'https://www.instagram.com/fashiondays/?hl=en'
        self.assertEqual(expected_url, actual_url)
        actual_title: str = self.chrome.title
        expected_title: str = 'Fashion Days (@fashiondays) • Instagram photos and videos'
        self.assertEqual(expected_title, actual_title)

    # this method checks that the TikTok link works fine
    def test_verify_tiktok(self):
        self.chrome.execute_script('window.scrollTo(0,500);')
        tiktok_link: WebElement = self.chrome.find_element(*self.TIKTOK)
        expected_href: str = "https://www.tiktok.com/@fashiondaysromania?lang=en"
        actual_href: str = tiktok_link.get_attribute('href')
        self.assertEqual(expected_href, actual_href)
        tiktok_link.click()
        tiktok_window: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(tiktok_window)
        expected_url: str = 'https://www.tiktok.com/@fashiondaysromania?lang=en'
        actual_url: str = self.chrome.current_url
        self.assertEqual(expected_url, actual_url)
        expected_title: str = 'Fashion Days (@fashiondaysromania) Official | TikTok'
        actual_title = self.chrome.title
        self.assertEqual(expected_title, actual_title)




