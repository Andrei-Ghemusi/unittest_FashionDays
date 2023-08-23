import unittest
import HtmlTestRunner

from main.main_page import MainPageTests
from main.authentication_page import PositiveTestsAuthenticationPage, NegativeTestsAuthenticationPage
from main.newsletter_tests import PositiveNewsletterTests, NegativeNewsletterTests
from main.non_functional_tests import NonFunctionalTestsMainPage
from main.search_functionality import PositiveSearchFunctionalityTests, NegativeSearchFunctionalityTests


class TestSuite(unittest.TestCase):
    def test_suite(self):
        main_suite = unittest.TestSuite()
        main_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(PositiveTestsAuthenticationPage),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NegativeTestsAuthenticationPage),
                             unittest.defaultTestLoader.loadTestsFromTestCase(PositiveNewsletterTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NegativeNewsletterTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(PositiveSearchFunctionalityTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NegativeSearchFunctionalityTests),
                             unittest.defaultTestLoader.loadTestsFromTestCase(NonFunctionalTestsMainPage),])

        # Run the main test suite with HtmlTestRunner
        main_runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # this will generate only one report with all the tests
            report_title="Test Execution Report",
            report_name="Test Results"
        )
        main_runner.run(main_suite)



