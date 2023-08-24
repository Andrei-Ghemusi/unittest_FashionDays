import unittest
import HtmlTestRunner

from authentication_page.authentication_page_non_functional_tests import NonFunctionalTestsAuthenticationPage
from authentication_page.negative_authentication_tests import NegativeTestsAuthenticationPage
from main_page.main_page_tests import MainPageTests
from authentication_page.positive_authentication_tests import PositiveTestsAuthenticationPage
from newsletter_functionality.negative_newsletter_tests import NegativeNewsletterTests
from newsletter_functionality.positive_newsletter_tests import PositiveNewsletterTests
from main_page.main_page_non_functional_tests import NonFunctionalTestsMainPage
from search_functionality.negative_search_functionality_tests import NegativeSearchFunctionalityTests
from search_functionality.positive_search_functionality_tests import PositiveSearchFunctionalityTests

class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(PositiveTestsAuthenticationPage),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NegativeTestsAuthenticationPage),
                             unittest.defaultTestLoader.loadTestsFromTestCase(PositiveNewsletterTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NegativeNewsletterTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(PositiveSearchFunctionalityTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NegativeSearchFunctionalityTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NonFunctionalTestsMainPage),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NonFunctionalTestsAuthenticationPage)])

        runner = HtmlTestRunner.HTMLTestRunner(

            combine_reports= True,  # this will generate only one report with all the tests
            report_title = "Test Execution Report",
            report_name = "Test Results"
        )

        runner.run(tests_to_run)