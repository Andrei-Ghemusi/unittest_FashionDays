from selenium.common import NoSuchElementException
from main.setups import MainPageSetupAndTearDown
from main.utility_methods import TestUtils


# This class contains tests that are ran on the main page
class MainPageTests(MainPageSetupAndTearDown):


    def test_mens_page_url(self):
        """
            Test case to verify that clicking on "BARBATI" redirects to the correct page and displays appropriate content.

            Steps:
                1. Click on the "BARBATI" link.
                2. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the men's fashion page with the correct URL and page title.
        """
        TestUtils.click_element(self.chrome, element=self.MEN)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/t/barbati/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/t/barbati/')
        TestUtils.assert_page_title(self.chrome, expected_title='Colectii de moda pentru barbati')

    # Test case: Click on "WOMEN" and verify the page URL
    def test_women_page_url(self):
        TestUtils.click_element(self.chrome, element=self.WOMEN)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/')
        TestUtils.assert_page_title(self.chrome, expected_title='Colectii de moda pentru femei')

    # Test case: Click on "BOYS" and verify the page URL
    def test_boys_page_url(self):
        TestUtils.click_element(self.chrome, element=self.BOYS)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/t/baieti/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/t/baieti/')
        TestUtils.assert_page_title(self.chrome, expected_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    # Test case: Click on "FETE" and verify the page URL
    def test_girls_page_url(self):
        TestUtils.click_element(self.chrome, element=self.GIRLS)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/t/fete/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/t/fete/')
        TestUtils.assert_page_title(self.chrome, expected_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    # Test case: Click on "AUTHENTICATION" and verify the page URL
    def test_authentication_page_url(self):
        TestUtils.click_element(self.chrome, element=self.AUTHENTICATION_PAGE)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/customer/authentication', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/customer/authentication')
        TestUtils.assert_page_title(self.chrome, expected_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    # Test case: Hover over clothing, click on dresses and verify the page URL
    def test_hover_over_clothing(self):
        TestUtils.move_to_element(self.chrome, element=self.CLOTHING)
        TestUtils.click_element(self.chrome, element=self.DRESSES)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/g/femei-/imbracaminte-rochii')


    # Test case: Hover over shoes, click on sandals and verify the page URL
    def test_hover_over_shoes(self):
        TestUtils.move_to_element(self.chrome, element=self.SHOES)
        TestUtils.click_element(self.chrome, element=self.SANDALS)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/g/femei-/incaltaminte-sandale')


    def test_check_under50_prices_outlet(self):
        """
            Test case to verify that products under 50 lei are displayed when clicking on "UNDER 50 LEI" in the outlet section.

            Steps:
                1. Hover over the "OUTLET" section.
                2. Click on the "UNDER 50 LEI" link.
                3. Verify the URL and check that product prices are under 50 lei.

            Expected Result:
                The user is redirected to the outlet page with products displayed, and all prices are under 50 lei.
        """
        TestUtils.move_to_element(self.chrome, element=self.OUTLET)
        TestUtils.click_element(self.chrome, element=self.UNDER50)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/s/under-15-euro-menu-mmse-w')
        prices_list = self.chrome.find_elements(*self.OUTLET_PRICES)
        for price in prices_list:
            price_text = int(price.text.replace(' lei', ''))
            price_value: float = price_text/100
            max_price: float = 50.00
            self.assertLessEqual(price_value, max_price)
            # This checks that the displayed products are under 50 lei


    # Test case: Check the availability of the garage promotion
    def test_garage_promotion_available(self):
        TestUtils.assert_is_promotion_displayed(self.chrome, element=self.GARAGE_SALE_PROMOTION)

    # Test case: Check the availability of the end of season promotion
    def test_end_of_season_promotion_available(self):
        TestUtils.assert_is_promotion_displayed(self.chrome, element=self.END_OF_SEASON_PROMOTION)

    # Test case: Check the availability of the goodbye summer promotion
    def test_goodbye_summer_promotion_available(self):
        TestUtils.assert_is_promotion_displayed(self.chrome, element=self.GOODBYE_SUMMER_PROMOTION)


    # Test case: Verify the "anpc" link
    def test_anpc_sal_link(self):
        """
            Test case to verify that the "ANPC" link redirects to the correct page and displays accurate information about "SAL".

            Steps:
                1. Scroll to the "ANPC" link on the main page.
                2. Click on the "ANPC" link.
                3. Switch to the new browser tab that opens (page index 1).
                4. Accept cookies if the pop-up appears (hence why I used try/except).
                5. Verify the URL, status code, and page title.
                6. Verify that the text "Soluționarea Alternativă a Litigiilor" is present.

            Expected Result:
                The user is redirected to the "ANPC" page explaining "SAL" with the correct URL, page title, and relevant text.
        """
        TestUtils.move_to_element(self.chrome, element=self.ANPC)
        TestUtils.click_element(self.chrome, self.ANPC)
        TestUtils.switch_window(self.chrome, page_index=1)
        try:
            TestUtils.click_element(self.chrome, element=self.ANPC_COOKIES)
        except NoSuchElementException:
            pass # I used try/except here because sometimes the cookie pop up won't appear
        TestUtils.assert_status_code(url='https://anpc.ro/ce-este-sal/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://anpc.ro/ce-este-sal/')
        TestUtils.assert_page_title(self.chrome, expected_title='Ce este SAL ? | ANPC')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.ANPC_TEXT,
                                      expected_text='Soluționarea Alternativă a Litigiilor')


    # Test case: Verify the Facebook link
    def test_verify_facebook_link(self):
        TestUtils.move_to_element(self.chrome, element=self.FACEBOOK)
        TestUtils.click_element(self.chrome, element=self.FACEBOOK)
        TestUtils.switch_window(self.chrome, page_index=1)
        TestUtils.assert_status_code(url='https://www.facebook.com/fashiondays.romania/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.facebook.com/fashiondays.romania/')
        TestUtils.assert_page_title(self.chrome, expected_title='Fashion Days | Bucharest')


    # Test case: Verify the Instagram link
    def test_verify_instagram_link(self):
        TestUtils.move_to_element(self.chrome, element=self.INSTAGRAM)
        TestUtils.click_element(self.chrome, element=self.INSTAGRAM)
        TestUtils.switch_window(self.chrome, page_index=1)
        TestUtils.assert_status_code(url='https://www.instagram.com/fashiondays/?hl=en', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.instagram.com/fashiondays/?hl=en')
        TestUtils.assert_page_title(self.chrome, expected_title='Fashion Days (@fashiondays) • Instagram photos and videos')


    # Test case: Verify the TikTok link
    def test_verify_tiktok_link(self):
        TestUtils.move_to_element(self.chrome, element=self.TIKTOK)
        TestUtils.click_element(self.chrome, element=self.TIKTOK)
        TestUtils.switch_window(self.chrome, page_index=1)
        TestUtils.assert_status_code(url='https://www.tiktok.com/@fashiondaysromania?lang=en', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.tiktok.com/@fashiondaysromania?lang=en')
        TestUtils.assert_page_title(self.chrome, expected_title='Fashion Days (@fashiondaysromania) Official | TikTok')
