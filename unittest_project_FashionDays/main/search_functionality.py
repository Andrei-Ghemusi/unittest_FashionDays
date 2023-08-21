import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from main.setups import MainPageSetupAndTearDown
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchFunctionalityTests(MainPageSetupAndTearDown):
    SEARCH: tuple[str, str] = (By.XPATH, '//*[@id="mobile-search"]/span')
    SEARCH_INPUT: tuple[str, str] = (By.XPATH, '//*[@id="search-input"]')
    SEARCH_BUTTON: tuple[str, str] = (By.XPATH, '//*[@id="search-submit"]/span')
    random_search: str = 'hgeuhe343%%%%#%@Grisrfhuisgo3252'
    first_search: str = 'nike'
    SECOND_HANDLE: tuple[str, str] = (By.XPATH, '//*[@id="slider-range"]/span[2]')
    FIRST_HANDLE: tuple[str, str] = (By.XPATH, '//*[@id="slider-range"]/span[1]')
    NO_PRODUCTS: tuple[str, str] = (By.XPATH, '//*[@id="products-listing-list"]/div/h2')
    MARIMILE_TALE: tuple[str, str] = (By.XPATH, '//*[@id="f_1_9717FilterOptions"]/h2')
    MENS: tuple[str, str] = (By.XPATH, '//*[@id="tagOpt_2"]/a/span[1]')
    HOODIES: tuple[str, str] = (By.XPATH, '//*[@id="categoryOpt_122__HOODIES__4__CLOTHING"]/a/span[1]')

    # here we have a bug
    """BUG """ # if we search for something (i.e. nike) and then after 1 second press back, the site does not load any promotions or campaigns, it completely fails and shows the code of the application

    # here we search with an empty searchbar
    def test_empty_search_enter(self):
        self.chrome.find_element(*self.SEARCH).click()
        # we click on the search so that it opens up and lets us type
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        # we press 'ENTER'
        """ POSSIBLE ISSUE """
        # this apparently refreshes the page,
        # I would ask if this is intended as I would consider that a message box should appear explaining that there needs to be a text input in order for the search to work

    def test_empty_search_click(self):
        self.chrome.find_element(*self.SEARCH).click()
        # we click on the search so that it opens up and lets us type
        self.chrome.find_element(By.XPATH, '//*[@id="search-submit"]/span').click()
        # we could also press the magnifying glass icon to search, and we test it too.
        # this does not refresh the page
        # Again I would consider this an issue that needs to be addressed

    # this method checks that the suggestion in the search bar is correct with what we wrote
    def test_suggestions_in_search_bar(self):
        self.chrome.find_element(*self.SEARCH).click()
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(self.first_search)
        first_suggestion = self.chrome.find_element(By.XPATH, '//*[@id="search-container__results"]/li[1]').text
        self.assertIn(self.first_search, first_suggestion, f'ERROR: was expecting {self.first_search} to be in {first_suggestion}')


    # this method checks that when we set the price filter to 0, there are no products shown
    def test_price_filter_set_to_zero(self):
        self.chrome.find_element(*self.SEARCH).click()
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(self.first_search)
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        actions = ActionChains(self.chrome)
        first_handle = self.chrome.find_element(*self.FIRST_HANDLE)
        second_handle = self.chrome.find_element(*self.SECOND_HANDLE)
        actions.drag_and_drop(second_handle, first_handle).perform()
        # we use action chains here to drag and drop the the second handle
        no_products_message = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.NO_PRODUCTS))
        # i gave an explicit wait here because I would receive issues given the slow load time of the element
        self.assertTrue(no_products_message.is_displayed(), f'ERROR: message is not displayed')
        actual_amount = int(self.chrome.find_element(By.XPATH, '//*[@id="amountMax"]').text)
        self.assertEqual(0,actual_amount, f'ERROR: expected the amount to be set on 0, but it is actually set on {actual_amount}')
        # here we verify that the amount actually changes to 0
        """ BUG HERE 
        If the value is set to 0 real fast, the application itself changes the number to 0, but on the GUI it does not, so we will have no products found for 0, 
        but the display will show any other number between 1 - 1500 (in this case, because selenium is so fast, it will show 1500, but when doing manual testing the number shown varies)
        """

    # this method is not used as a test because we just call it when needed
    def searching_random_characters(self):
        self.chrome.find_element(*self.SEARCH).click()
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(self.random_search)
        # we write in the search input random letters, numbers and special characters
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)

    # this method checks that the first message, when there are no products, is correct
    def test_searching_random_characters_no_results(self):
        self.searching_random_characters()
        # here we called the method 'searching_random_characters' to save some code
        sorry_message = self.chrome.find_element(By.XPATH, '//*[@id="fallback-top-container"]/div[1]')
        assert sorry_message.is_displayed()
        expected_message = 'Ne pare rau, niciun rezultat gasit pentru:'
        self.assertEqual(expected_message, sorry_message.text, f'ERROR, expected {expected_message} message, but got {sorry_message.text} message instead')
        # we use these asserts to check that the message is displayed and that it is correct
        my_random_search = self.chrome.find_element(By.XPATH, '//*[@id="fallback-top-container"]/div[2]')
        assert my_random_search.is_displayed()
        self.assertEqual(self.random_search, my_random_search.text, f'ERROR, expected {self.random_search} message, but got {my_random_search.text} message instead')
        # we use these asserts, to check that our input is also displayed correctly in the message


    # here we check that the second message is correct when there are no products for the one we searched
    def test_searching_random_characters_no_products(self):
        self.searching_random_characters()
        self.chrome.execute_script("window.scrollTo(0, 500);")
        # we use this to scroll down the page
        actual_message = self.chrome.find_element(By.XPATH, '//*[text()="Nu au fost gasite produse."]').text
        expected_message = 'Nu au fost gasite produse.'
        self.assertEqual(expected_message, actual_message, f'ERROR, expected {expected_message} message, but got {actual_message} message instead')


    # in this method we check that the recommended items are displayed
    def test_searching_random_characters_recommended(self):
        # we also check that the message recommending them is correct
        self.searching_random_characters()
        recommendation_message = self.chrome.find_element(By.XPATH, '//*[@id="fallback-top-container"]/div[3]').text
        expected_message = "Din fericire, poti regasi mai jos o selectie de articole din care sa-ti alegi favoritele!"
        self.assertEqual(expected_message, recommendation_message, f'ERROR, expected {expected_message} message, but got {recommendation_message} message instead')
        recommended_product = self.chrome.find_element(By.XPATH, '//*[@class="carousel-builder-product-image"]')
        assert recommended_product.is_displayed(), f'ERROR, recommended product not displayed '


    # this method checks that after searching a valid product, the first 5 products with that name will be displayed
    def test_search_valid_product(self):
        self.chrome.find_element(*self.SEARCH).click()
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys('nike')
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        results_list = self.chrome.find_elements(By.XPATH, '//h2[@class="product-card-brand"]')
        # here we made a list of the products shown after the search using the class they all use so that we can iterate through them and see if the text is as expected
        for i in range(5):
            # we use the range of 5 as I feel it is enough for the test
            results = results_list[i].text.lower()
            # we use lowercase as to avoid random uppercases or lowercases
            expected_text = 'nike'
            assert expected_text in results, f'Error, {expected_text} does not appear in {results} at product number {i}'
            # in case the name of the product is not the expected one this assertion points where the issue is

    # this method checks that all filters are deleted when clicking on 'delete all filters'
    def test_delete_all_filters(self):
        self.chrome.find_element(*self.SEARCH).click()
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys('nike')
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        self.chrome.find_element(*self.MENS).click()
        # here we choose one filter "Men's"
        self.chrome.find_element(*self.HOODIES).click()
        # here we choose another filter called 'Hoodies'
        self.chrome.execute_script("window.scrollTo(0, 0);")
        # we scroll al the way up
        mens_filter = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tagOpt_2"]/a')))
        hoodies_filter = WebDriverWait(self.chrome, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="categoryOpt_122__HOODIES__4__CLOTHING"]/a')))
        # we selected the elements which contain the active filters and we use explicit waits as it might take a while for the elements to load
        self.chrome.find_element(By.XPATH, '//*[@id="filters"]/div[1]/div/a').click()
        # we click on 'delete all filters'
        time.sleep(1)
        # we use a sleep here to let the elements update
        self.assertNotIn("filter-link  active filter", mens_filter.get_attribute('class'))
        self.assertNotIn("filter-link  active filter", hoodies_filter.get_attribute('class'))
        # we verify that the filters have been removed
