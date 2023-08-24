import time
from setups import MainPageSetupAndTearDown
from selenium.webdriver import ActionChains
from utility_methods import TestUtils

class NegativeSearchFunctionalityTests(MainPageSetupAndTearDown):

    # here we search with an empty searchbar
    def test_empty_search_enter(self):
        TestUtils.click_element(self.chrome, element=self.SEARCH)
        # we click on the search so that it opens up and lets us type
        TestUtils.press_enter(self.chrome, element=self.SEARCH_INPUT)
        # we press 'ENTER'
        TestUtils.assert_current_url(self.chrome, expected_url='https://www.fashiondays.ro/') # after pressing enter we are still on the main_page page, hence why I check if this still happens
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