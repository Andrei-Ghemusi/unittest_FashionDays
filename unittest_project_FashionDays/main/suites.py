import unittest
import HtmlTestRunner

from main.main_page import MainPageTests
from main.authentication_page import AuthenticationPage
from main.newsletter_tests import NewsletterTests

class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_to_run = unittest.TestSuite()
        tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTests),
                              unittest.defaultTestLoader.loadTestsFromTestCase(AuthenticationPage),
                              unittest.defaultTestLoader.loadTestsFromTestCase(NewsletterTests)])

        runner = HtmlTestRunner.HTMLTestRunner(

            combine_reports= True,  # this will generate only one report with all of the tests
            report_title = "Test Execution Report",
            report_name = "Test Results"
        )

        runner.run(tests_to_run)



