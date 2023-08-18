import unittest
import HtmlTestRunner

from main.main_page import MainPageTests
from main.authentication_page import PositiveTestsAuthenticationPage, NegativeTestsAuthenticationPage
from main.newsletter_tests import PositiveNewsletterTests

class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTests),
                              unittest.defaultTestLoader.loadTestsFromTestCase(PositiveTestsAuthenticationPage),
                              unittest.defaultTestLoader.loadTestsFromTestCase(PositiveNewsletterTests),
                               unittest.defaultTestLoader.loadTestsFromTestCase(NegativeTestsAuthenticationPage)])

        runner = HtmlTestRunner.HTMLTestRunner(

            combine_reports= True,  # this will generate only one report with all the tests
            report_title = "Test Execution Report",
            report_name = "Test Results"
        )

        runner.run(tests_to_run)



