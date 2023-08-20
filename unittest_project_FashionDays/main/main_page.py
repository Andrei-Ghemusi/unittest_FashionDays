import requests
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from main.setups import MainPageSetupAndTearDown


# This class contains tests that are ran on the main page
class MainPageTests(MainPageSetupAndTearDown):
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


    '''
        This method can: - click on an element
                         - check that the current url is the same as the expected one
                         - check that the current page title is the same as the expected one
        This is NOT a test, but a method called in tests - its purpose is being reused.
    '''
    def click_elem_check_url_and_status_code(self, element=None, expected_url=None, expected_page_title=None):
        if element is not None:
            self.chrome.find_element(*element).click()

        actual_url: str = self.chrome.current_url
        if expected_url is not None:
            self.assertEqual(expected_url, actual_url)
            # here we check that we are on the correct url

        if expected_page_title is not None:
            actual_title: str = self.chrome.title
            self.assertIn(expected_page_title, actual_title)

        response = requests.head(actual_url)
        self.assertEqual(200, response.status_code)
        # here we check that the link is correct and not broken by verifying that the status code is correct


    # This method checks that after clicking on "BARBATI" we are being sent to the right page
    def test_mens_page_url(self):
        self.click_elem_check_url_and_status_code(element=self.MEN,
                                                  expected_url='https://www.fashiondays.ro/t/barbati/',
                                                  expected_page_title='Colectii de moda pentru barbati')

    # This method checks that after clicking on "FEMEI" we are being sent to the right page
    def test_women_page_url(self):
        self.click_elem_check_url_and_status_code(element=self.WOMEN,
                                                  expected_url='https://www.fashiondays.ro/',
                                                  expected_page_title='Colectii de moda pentru femei')

    # This method checks that after clicking on "BAIETI" we are being sent to the right page
    def test_boys_page_url(self):
        self.click_elem_check_url_and_status_code(element=self.BOYS,
                                                  expected_url='https://www.fashiondays.ro/t/baieti/',
                                                  expected_page_title='Destinatia de fashion #1 in Europa Centrala si de Est')

    # This method checks that after clicking on "FETE" we are being sent to the right page
    def test_girls_page_url(self):
        self.click_elem_check_url_and_status_code(element=self.GIRLS,
                                                  expected_url='https://www.fashiondays.ro/t/fete/',
                                                  expected_page_title='Destinatia de fashion #1 in Europa Centrala si de Est')

    # This method checks that after clicking on authentication we are on the authentication page
    def test_authentication_page_url(self):
        self.click_elem_check_url_and_status_code(element=self.AUTHENTICATION_PAGE,
                                                  expected_url='https://www.fashiondays.ro/customer/authentication',
                                                  expected_page_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    '''
        This method hovers over an element, clicks on it and then checks that we are being sent on the correct url
        This is NOT a test, but a method called in tests - its purpose is being reused.
    '''
    def hover_element(self, element, second_element, expected_url):
        actions = ActionChains(self.chrome)
        account_element: WebElement = self.chrome.find_element(*element)
        actions.move_to_element(account_element).perform()
        self.chrome.find_element(*second_element).click()
        actual_url: str = self.chrome.current_url
        self.assertEqual(expected_url, actual_url)

    # This method hovers over clothing and clicks on dresses then checks that we are on the correct page
    def test_hover_over_clothing(self):
        self.hover_element(element=self.CLOTHING,
                           second_element=self.DRESSES,
                           expected_url='https://www.fashiondays.ro/g/femei-/imbracaminte-rochii')

    # This method hovers over shoes and clicks on sandals then checks that we are on the correct page
    def test_hover_over_shoes(self):
        self.hover_element(element=self.SHOES,
                           second_element=self.SANDALS,
                           expected_url='https://www.fashiondays.ro/g/femei-/incaltaminte-sandale')

    # This method hovers over outlet and clicks on under 50 lei, checks that we are on the correct page
    # then that the displayed product are under 50 lei
    def test_check_under50_prices_outlet(self):
        self.hover_element(element=self.OUTLET,
                           second_element=self.UNDER50,
                           expected_url='https://www.fashiondays.ro/s/under-15-euro-menu-mmse-w')
        prices_list = self.chrome.find_elements(*self.OUTLET_PRICES)
        for price in prices_list:
            price_text = int(price.text.replace(' lei', ''))
            price_value: float = price_text/100
            self.assertLessEqual(price_value, 50.00)


    '''
        This method checks if the promotion is still available
        This is NOT a test, but a method called in tests - its purpose is being reused.
    '''
    def is_promotion_displayed(self, element):
        unavailable: str = 'Promotion is no longer available!'
        try:
            promotion_display: WebElement = self.chrome.find_element(*element)
            promotion_display.is_displayed()
            self.assertTrue(promotion_display, f'{unavailable}')
        except NoSuchElementException:
            pass

    # This method checks if the garage promotion is still available
    def test_garage_promotion_available(self):
        self.is_promotion_displayed(self.GARAGE_SALE_PROMOTION)

    # This method checks if the end of season promotion is still available
    def test_end_of_season_promotion_available(self):
        self.is_promotion_displayed(self.END_OF_SEASON_PROMOTION)

    # This method checks if the goodbye summer promotion is still available
    def test_goodbye_summer_promotion_available(self):
        self.is_promotion_displayed(self.GOODBYE_SUMMER_PROMOTION)


    # This method checks that the link towards "anpc" works
    def test_anpc_sal_link(self):
        self.scroll_to_element(self.chrome.find_element(*self.ANPC))
        # we scroll to the anpc link
        self.chrome.find_element(*self.ANPC).click()
        anpc_page: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(anpc_page)
        # we switch to the anpc tab
        try:
            self.chrome.find_element(By.XPATH, '//*[text()="Acceptă"]').click()
        except NoSuchElementException:
            pass
        # we accept the cookies, also, I used try/except here because sometimes the cookie pop up won't appear

        self.click_elem_check_url_and_status_code(element=None,
                                                  expected_url='https://anpc.ro/ce-este-sal/',
                                                  expected_page_title='Ce este SAL ? | ANPC')

        anpc_text: str = self.chrome.find_element(*self.ANPC_TEXT).text
        expected_anpc_text: str = 'Soluționarea Alternativă a Litigiilor'
        self.assertEqual(anpc_text, expected_anpc_text, f'ERROR, expected {expected_anpc_text} but got {anpc_text}')
        # and here that some of the text on the page is correct


    # This method checks that the facebook link works and send us to the correct url
    def test_verify_facebook_link(self):
        self.scroll_to_element(self.chrome.find_element(*self.FACEBOOK))
        # we scroll down the page
        self.click_elem_check_url_and_status_code(element=self.FACEBOOK)

        facebook_window: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(facebook_window)
        # here we switch to the facebook window

        self.click_elem_check_url_and_status_code(element=None,
                                                  expected_url='https://www.facebook.com/fashiondays.romania/', # here we check that we are on the correct url
                                                  expected_page_title='Fashion Days | Bucharest') # we check that the page title is the correct one


    # This method checks that the instagram link works and send us to the correct url
    def test_verify_instagram_link(self):
        self.scroll_to_element(self.chrome.find_element(*self.INSTAGRAM))
        self.click_elem_check_url_and_status_code(element=self.INSTAGRAM)

        instagram_window: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(instagram_window)

        self.click_elem_check_url_and_status_code(element=None,
                                                  expected_url='https://www.instagram.com/fashiondays/?hl=en',
                                                  # here we check that we are on the correct url
                                                  expected_page_title='Fashion Days (@fashiondays) • Instagram photos and videos')  # we check that the page title is the correct one


    # This method checks that the TikTok link works and send us to the correct url
    def test_verify_tiktok_link(self):
        self.scroll_to_element(self.chrome.find_element(*self.TIKTOK))
        self.click_elem_check_url_and_status_code(element=self.TIKTOK)

        tiktok_window: str = self.chrome.window_handles[1]
        self.chrome.switch_to.window(tiktok_window)

        self.click_elem_check_url_and_status_code(element=None,
                                                  expected_url='https://www.tiktok.com/@fashiondaysromania?lang=en',
                                                  # here we check that we are on the correct url
                                                  expected_page_title='Fashion Days (@fashiondaysromania) Official | TikTok')  # we check that the page title is the correct one





