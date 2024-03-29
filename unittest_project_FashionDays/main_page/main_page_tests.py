import time

from selenium.common import NoSuchElementException
from setups import MainPageSetupAndTearDown
from utility_methods import TestUtils


# This class contains tests that are ran on the main_page page
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


    def test_women_page_url(self):
        """
            Test case to verify that clicking on "FEMEI" redirects to the correct page and displays appropriate content.

            Steps:
                1. Click on the "FEMEI" link.
                2. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the women's fashion page with the correct URL and page title.
        """
        TestUtils.click_element(self.chrome, element=self.WOMEN)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/')
        TestUtils.assert_page_title(self.chrome, expected_title='Colectii de moda pentru femei')


    def test_boys_page_url(self):
        """
            Test case to verify that clicking on "BAIETI" redirects to the correct page and displays appropriate content.

            Steps:
                1. Click on the "BAIETI" link.
                2. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the boys fashion page with the correct URL and page title.
        """
        TestUtils.click_element(self.chrome, element=self.BOYS)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/t/baieti/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/t/baieti/')
        TestUtils.assert_page_title(self.chrome, expected_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    def test_girls_page_url(self):
        """
            Test case to verify that clicking on "FETE" redirects to the correct page and displays appropriate content.

            Steps:
                1. Click on the "FETE" link.
                2. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the girls fashion page with the correct URL and page title.
        """
        TestUtils.click_element(self.chrome, element=self.GIRLS)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/t/fete/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/t/fete/')
        TestUtils.assert_page_title(self.chrome, expected_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    def test_authentication_page_url(self):
        """
            Test case to verify that clicking on "AUTHENTICATION" redirects to the correct p age and displays appropriate content.

            Steps:
                1. Click on the "AUTHENTICATION" link.
                2. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the authentication page with the correct URL and page title.
        """
        TestUtils.click_element(self.chrome, element=self.AUTHENTICATION_PAGE)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/customer/authentication', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/customer/authentication')
        TestUtils.assert_page_title(self.chrome, expected_title='Destinatia de fashion #1 in Europa Centrala si de Est')


    def test_hover_over_clothing(self):
        """
            Test case to verify that hovering over "CLOTHING" and clicking on "DRESSES" redirects to the correct page and displays appropriate content.

            Steps:
                1. Hover over the "CLOTHING" section.
                2. Click on the "DRESSES" link.
                3. Verify the URL, page title and status code.

            Expected Result:
                The user is redirected to the dresses page with the correct URL, page title and status code.
        """
        TestUtils.move_to_element(self.chrome, element=self.CLOTHING)
        TestUtils.click_element(self.chrome, element=self.DRESSES)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/g/femei-/imbracaminte-rochii', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/g/femei-/imbracaminte-rochii')
        TestUtils.assert_page_title(self.chrome, expected_title='Rochii Dama')


    # Test case: Hover over shoes, click on sandals and verify the page URL
    def test_hover_over_shoes(self):
        """
            Test case to verify that hovering over "SHOES" and clicking on "SANDALS" redirects to the correct page and displays appropriate content.

            Steps:
                1. Hover over the "SHOES" section.
                2. Click on the "SANDALS" link.
                3. Verify the URL, page title and status code.

            Expected Result:
                The user is redirected to the sandals page with the correct URL, page title and status code.
        """
        TestUtils.move_to_element(self.chrome, element=self.SHOES)
        TestUtils.click_element(self.chrome, element=self.SANDALS)
        TestUtils.assert_status_code(url='https://www.fashiondays.ro/g/femei-/incaltaminte-sandale', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/g/femei-/incaltaminte-sandale')
        TestUtils.assert_page_title(self.chrome, expected_title='Sandale')

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
        TestUtils.assert_page_title(self.chrome, expected_title='Articole sub 50 lei')
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


    def test_anpc_sal_link(self):
        """
            Test case to verify that the "ANPC" link redirects to the correct page and displays accurate information about "SAL".

            Steps:
                1. Scroll to the "ANPC" link on the main_page page.
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
        time.sleep(1) # I added a sleep of 1 sec here because without it we get an error regarding performance
                      # the implicit or explicit wait does not solve this issue, hence why we use time.sleep
        try:
            TestUtils.wait_for_element_visibility(self.chrome, element_locator=self.ANPC_COOKIES)
            TestUtils.click_element(self.chrome, element=self.ANPC_COOKIES)
        except NoSuchElementException:
            pass # I used try/except here because sometimes the cookie pop up won't appear
        TestUtils.assert_status_code(url='https://anpc.ro/ce-este-sal/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://anpc.ro/ce-este-sal/')
        TestUtils.assert_page_title(self.chrome, expected_title='Ce este SAL ? | ANPC')
        TestUtils.assert_text_message(self.chrome,
                                      text_element=self.ANPC_TEXT,
                                      expected_text='Soluționarea Alternativă a Litigiilor')


    def test_verify_facebook_link(self):
        """
            Test case to verify that the "FACEBOOK" link redirects to the correct page.

            Steps:
                1. Scroll to the "FACEBOOK" link on the main_page page.
                2. Click on the "FACEBOOK" link.
                3. Switch to the new browser tab that opens (page index 1).
                4. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the "FACEBOOK" page with the correct URL, page title, and status code.
        """
        TestUtils.move_to_element(self.chrome, element=self.FACEBOOK)
        TestUtils.click_element(self.chrome, element=self.FACEBOOK)
        TestUtils.switch_window(self.chrome, page_index=1)
        TestUtils.assert_status_code(url='https://www.facebook.com/fashiondays.romania/', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.facebook.com/fashiondays.romania/')
        TestUtils.assert_page_title(self.chrome, expected_title='Fashion Days | Bucharest')


    def test_verify_instagram_link(self):
        """
            Test case to verify that the "INSTAGRAM" link redirects to the correct page.

            Steps:
                1. Scroll to the "INSTAGRAM" link on the main_page page.
                2. Click on the "INSTAGRAM" link.
                3. Switch to the new browser tab that opens (page index 1).
                4. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the "INSTAGRAM" page with the correct URL, page title, and status code.
        """
        TestUtils.move_to_element(self.chrome, element=self.INSTAGRAM)
        TestUtils.click_element(self.chrome, element=self.INSTAGRAM)
        TestUtils.switch_window(self.chrome, page_index=1)
        TestUtils.assert_status_code(url='https://www.instagram.com/fashiondays/?hl=en', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.instagram.com/fashiondays/?hl=en')
        TestUtils.assert_page_title(self.chrome, expected_title='Fashion Days (@fashiondays) • Instagram photos and videos')


    def test_verify_tiktok_link(self):
        """
            Test case to verify that the "TIKTOK" link redirects to the correct page.

            Steps:
                1. Scroll to the "TIKTOK" link on the main_page page.
                2. Click on the "TIKTOK" link.
                3. Switch to the new browser tab that opens (page index 1).
                4. Verify the URL, status code, and page title.

            Expected Result:
                The user is redirected to the "TIKTOK" page with the correct URL, page title, and status code.
        """
        TestUtils.move_to_element(self.chrome, element=self.TIKTOK)
        TestUtils.click_element(self.chrome, element=self.TIKTOK)
        TestUtils.switch_window(self.chrome, page_index=1)
        TestUtils.assert_status_code(url='https://www.tiktok.com/@fashiondaysromania?lang=en', expected_code=200)
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.tiktok.com/@fashiondaysromania?lang=en')
        TestUtils.assert_page_title(self.chrome, expected_title='Fashion Days (@fashiondaysromania) Official | TikTok')