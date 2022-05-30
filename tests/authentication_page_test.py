import unittest
import HtmlTestRunner
from base_configuration_test import BaseAuthenticationPageTest
from locators.authentication_page_locators import RegistrationPageLocators, LoginPageLocators
from pages.authentication_page import AuthenticationPage


class RegistrationPageTest(BaseAuthenticationPageTest):
    def test_registration_email_already_exist_negative(self):
        authPage = AuthenticationPage(self.driver)
        authPage.fill_in(RegistrationPageLocators.EMAIL_FIELD, authPage.register_mail_already_taken)
        authPage.click_on(RegistrationPageLocators.CREATE_BUTTON)
        authPage.check_error()
        self.assertTrue(authPage.result["result_boolean"], authPage.result["message"])

    def test_registration_invalid_date_of_birth_negative(self):
        authPage = AuthenticationPage(self.driver)
        authPage.fill_in(RegistrationPageLocators.EMAIL_FIELD, authPage.fake_email())
        authPage.click_on(RegistrationPageLocators.CREATE_BUTTON)
        if authPage.is_email_ok():
            authPage.fullfill_the_registration_form("incorrectDate", "2")
            authPage.check_error()
            self.assertTrue(authPage.result["result_boolean"], authPage.result["message"])
        else:
            self.assertTrue(False,"email given before clicking create an account != email in the form")

    def test_registration_incorrect_password_negative(self):
        authPage = AuthenticationPage(self.driver)
        authPage.fill_in(RegistrationPageLocators.EMAIL_FIELD, authPage.fake_email())
        authPage.click_on(RegistrationPageLocators.CREATE_BUTTON)
        if authPage.is_email_ok():
            authPage.fullfill_the_registration_form("incorrectPassword", "1234")  # password must be atleast 5 chars
            authPage.check_error()
            self.assertTrue(authPage.result["result_boolean"], authPage.result["message"])
        else:
            self.assertTrue(False,"email given before clicking create an account != email in the form")

    def test_registration_blank_password_negative(self):
        authPage = AuthenticationPage(self.driver)
        authPage.fill_in(RegistrationPageLocators.EMAIL_FIELD, authPage.fake_email())
        authPage.click_on(RegistrationPageLocators.CREATE_BUTTON)
        if authPage.is_email_ok():
            authPage.fullfill_the_registration_form("blankPassword", "noValue")
            authPage.check_error()
            self.assertTrue(authPage.result["result_boolean"], authPage.result["message"])
        else:
            self.assertTrue(False,"email given before clicking create an account != email in the form")

    def test_registration_email_too_long_negative(self):
        authPage = AuthenticationPage(self.driver)
        authPage.fake_email_address = authPage.register_mail_too_long
        authPage.fill_in(RegistrationPageLocators.EMAIL_FIELD, authPage.register_mail_too_long)
        authPage.click_on(RegistrationPageLocators.CREATE_BUTTON)
        if authPage.is_email_ok():
            authPage.fullfill_the_registration_form("", "")
            authPage.check_error()
            self.assertTrue(authPage.result["result_boolean"], authPage.result["message"])
        else:
            self.assertTrue(False,"email given before clicking create an account != email in the form")

    def test_registration_positive(self):
        authPage = AuthenticationPage(self.driver)
        authPage.fill_in(RegistrationPageLocators.EMAIL_FIELD, authPage.fake_email())
        authPage.click_on(RegistrationPageLocators.CREATE_BUTTON)
        if authPage.is_email_ok():
            authPage.fullfill_the_registration_form("", "")
            self.assertEqual(authPage.head_title_registration_positive, self.driver.title)
        else:
            self.assertTrue(False,"email given before clicking create an account != email in the form")


class LoginPageTest(BaseAuthenticationPageTest):
    def test_login_blank_fields_negative(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, "")
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, "")
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        loginPage.check_error()
        self.assertTrue(loginPage.result["result_boolean"], loginPage.result["message"])

    def test_login_blank_email_negative(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, "")
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, loginPage.login_password_positive)
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        loginPage.check_error()
        self.assertTrue(loginPage.result["result_boolean"], loginPage.result["message"])

    def test_login_blank_password_negative(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, loginPage.login_email_positive)
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, "")
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        loginPage.check_error()
        self.assertTrue(loginPage.result["result_boolean"], loginPage.result["message"])

    def test_login_incorrect_email_syntax_negative(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, loginPage.login_incorrect_syntax_email)
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, loginPage.login_password_positive)
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        loginPage.check_error()
        self.assertTrue(loginPage.result["result_boolean"], loginPage.result["message"])

    def test_login_mail_not_in_database_negative(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, loginPage.login_email_not_in_database)
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, loginPage.login_password_positive)
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        loginPage.check_error()
        self.assertTrue(loginPage.result["result_boolean"], loginPage.result["message"])

    def test_login_invalid_password_negative(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, loginPage.login_email_positive)
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, loginPage.login_password_positive + "333")
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        loginPage.check_error()
        self.assertTrue(loginPage.result["result_boolean"], loginPage.result["message"])

    def test_login_positive(self):
        loginPage = AuthenticationPage(self.driver)
        loginPage.fill_in(LoginPageLocators.EMAIL_FIELD, loginPage.login_email_positive)
        loginPage.fill_in(LoginPageLocators.PASSWORD_FIELD, loginPage.login_password_positive)
        loginPage.click_on(LoginPageLocators.SIGNIN_BUTTON)
        self.driver.refresh()
        self.assertEqual(loginPage.head_title_registration_positive, self.driver.title)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
