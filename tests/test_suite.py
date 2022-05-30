import unittest
import HtmlTestRunner
from tests.home_page_test import HomePageTest
from tests.authentication_page_test import RegistrationPageTest
from tests.authentication_page_test import LoginPageTest


class TestSuite(unittest.TestSuite):
    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(HomePageTest('test_is_home_page_loaded_successfully'))#id:M01
        suite.addTest(HomePageTest('test_navigate_to_women_dir'))#id:M02
        suite.addTest(HomePageTest('test_navigate_to_dresses_dir'))#id:M03
        suite.addTest(HomePageTest('test_navigate_to_tshirts_dir'))#id:M04
        suite.addTest(HomePageTest('test_navigate_to_signin'))#id:M05
        suite.addTest(HomePageTest('test_add_to_cart'))  # id:M06

        suite.addTest(RegistrationPageTest('test_registration_email_already_exist_negative'))#id:A01
        suite.addTest(RegistrationPageTest('test_registration_invalid_date_of_birth_negative'))#id:A02
        suite.addTest(RegistrationPageTest('test_registration_incorrect_password_negative'))#id:A03
        suite.addTest(RegistrationPageTest('test_registration_blank_password_negative'))#id:A04
        suite.addTest(RegistrationPageTest('test_registration_email_too_long_negative'))#id:A05
        suite.addTest(RegistrationPageTest('test_registration_positive'))#id:A06

        suite.addTest(LoginPageTest('test_login_blank_fields_negative'))
        suite.addTest(LoginPageTest('test_login_blank_email_negative'))
        suite.addTest(LoginPageTest('test_login_blank_password_negative'))
        suite.addTest(LoginPageTest('test_login_incorrect_email_syntax_negative'))
        suite.addTest(LoginPageTest('test_login_mail_not_in_database_negative'))
        suite.addTest(LoginPageTest('test_login_invalid_password_negative'))
        suite.addTest(LoginPageTest('test_login_positive'))
        return suite


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_name="unittestresult", output="reports/", combine_reports=True))
