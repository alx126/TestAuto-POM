import unittest

import HtmlTestRunner

from tests.test_login_page import TestLoginPage
from tests.test_secure_page import TestSecurePage


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()

        test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSecurePage),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test report pom_bdd",
            report_name="Test results pom_bdd"
        )
        runner.run(test_suite)