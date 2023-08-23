import time

from selenium.webdriver.common.by import By
from main.setups import MainPageSetupAndTearDown
from selenium.webdriver import ActionChains
from main.utility_methods import TestUtils


class PositiveSearchFunctionalityTests(MainPageSetupAndTearDown):

    """ BUG
    if we search for something (i.e. nike) and then after 1 second press back, the site does not load any promotions or campaigns,
    it completely fails and shows the code of the application
    In the bug report you will find screenshots """
    def test_search_then_press_back(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT, input_text_1='nike')
        self.chrome.back()


    # this method checks that the suggestion in the search bar is correct with what we wrote
    def test_suggestions_in_search_bar(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT, input_text_1='nike')
        TestUtils.assert_text_message(self.chrome, self.SUGGESTION, expected_text='nike')


    # this method checks that when we set the price filter to 0, there are no products shown
    def test_price_filter_set_to_zero(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT, input_text_1='nike')
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)

        actions = ActionChains(self.chrome)
        first_handle = self.chrome.find_element(*self.FIRST_HANDLE)
        second_handle = self.chrome.find_element(*self.SECOND_HANDLE)
        actions.drag_and_drop(second_handle, first_handle).perform()
        # we use action chains here to drag and drop the second handle

        TestUtils.assert_is_element_displayed(self.chrome, self.NO_PRODUCTS)
        TestUtils.assert_values(self.chrome, element=self.FILTER_VALUE, expected_value=1500)
        # I left it here at 1500, theoretically it should fail, but it actually passes
        """ BUG HERE 
        If the value is set to 0 real fast, the application itself changes the number to 0, but on the GUI it does not, so we will have no products found for 0, 
        but the display will show any other number between 1 - 1500 (in this case, because selenium is so fast, it will show 1500, but when doing manual testing the number shown varies)
        """

    # this method checks that after searching a valid product, the first 5 products with that name will be displayed
    def test_search_valid_product(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT, input_text_1='nike')
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        results_list = self.chrome.find_elements(*self.RESULTS)
        # here we made a list of the products shown after the search using the class they all use so that we can iterate through them and see if the text is as expected
        for i in range(5):
            # we use the range of 5 as I feel it is enough for the test
            results = results_list[i].text.lower()
            # we use lowercase as to avoid random uppercases or lowercases
            expected_text = 'nike'
            self.assertIn(expected_text, results, f'Error, {expected_text} does not appear in {results} at product number {i}')
            # in case the name of the product is not the expected one this assertion points where the issue is


    # this method checks that all filters are deleted when clicking on 'delete all filters'
    def test_delete_all_filters(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT, input_text_1='nike')
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        TestUtils.click_element(self.chrome, element=self.SLIPPERS)
        # here we choose one filter "slippers"
        time.sleep(1)
        TestUtils.wait_for_element_visibility(self.chrome, element_locator=self.DRESSES_CATEGORY)
        TestUtils.click_element(self.chrome, element=self.DRESSES_CATEGORY)
        # here we choose another filter called 'dresses'
        TestUtils.click_element(self.chrome, element=self.DELETE_ALL_CATEGORIES)
        filter1 = TestUtils.wait_for_element_visibility(self.chrome, element_locator=self.SLIPPERS)
        filter2 = TestUtils.wait_for_element_visibility(self.chrome, element_locator=self.DRESSES_CATEGORY)
        self.assertNotIn("active-filter", filter1.get_attribute('class'))
        self.assertNotIn("active-filter", filter2.get_attribute('class'))
        # we verify that the filters have been removed


class NegativeSearchFunctionalityTests(MainPageSetupAndTearDown):

    # here we search with an empty searchbar
    def test_empty_search_enter(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        # we click on the search so that it opens up and lets us type
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        # we press 'ENTER'
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/') # after pressing enter we are still on the main page, hence why I check if this still happens
        """ POSSIBLE ISSUE """
        # this apparently refreshes the page,
        # I would ask if this is intended as I would consider that a message box should appear explaining that there needs to be a text input in order for the search to work

    def test_empty_search_click(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        # we click on the search so that it opens up and lets us type
        TestUtils.click_element(self.chrome, self.SEARCH_ICON)
        # we could also press the magnifying glass icon to search, and we test it too.
        # this does not refresh the page, it actually does nothing, the button search does not work if there is no text in the search bar
        # Again I would consider this an issue that needs to be addressed


    # this method checks that the first message, when there are no products, is correct
    def test_searching_random_characters_no_results(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT,
                                        input_text_1='hgeuhe343%%%%#%@Grisrfhuisgo3252')
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        TestUtils.assert_text_message(self.chrome, text_element=self.NO_RESULTS, expected_text='Ne pare rau, niciun rezultat gasit pentru:')
        TestUtils.assert_text_message(self.chrome, text_element=self.OUR_INPUT_DISPLAY , expected_text='hgeuhe343%%%%#%@Grisrfhuisgo3252')
        # we use these asserts to check that the message is displayed and that it is correct
        # we use these asserts, to check that our input is also displayed correctly in the message


    # here we check that the second message is correct when there are no products for the one we searched
    def test_searching_random_characters_no_products(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT,
                                        input_text_1='hgeuhe343%%%%#%@Grisrfhuisgo3252')
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        TestUtils.move_to_element(self.chrome, element=self.FOUND_NO_PRODUCTS)
        # we use this to scroll down the page
        TestUtils.assert_text_message(self.chrome, text_element=self.FOUND_NO_PRODUCTS, expected_text='Nu au fost gasite produse.')


    # in this method we check that the recommended items are displayed
    def test_searching_random_characters_recommended(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        TestUtils.send_inputs_and_click(self.chrome, input_element_1=self.SEARCH_INPUT,
                                        input_text_1='hgeuhe343%%%%#%@Grisrfhuisgo3252')
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        TestUtils.assert_text_message(self.chrome, text_element=self.RECOMMENDED_MESSAGE,
                                      expected_text="Din fericire, poti regasi mai jos o selectie de articole din care sa-ti alegi favoritele!")
        TestUtils.assert_is_element_displayed(self.chrome, element=self.RECOMMENDED_PRODUCT)


