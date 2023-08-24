import time
from setups import MainPageSetupAndTearDown
from selenium.webdriver import ActionChains
from utility_methods import TestUtils


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