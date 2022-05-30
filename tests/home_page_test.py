import time
import unittest
import HtmlTestRunner
from base_configuration_test import BaseHomePageTest
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from pages.authentication_page import AuthenticationPage
from locators.authentication_page_locators import RegistrationPageLocators


class HomePageTest(BaseHomePageTest):

    def test_is_home_page_loaded_successfully(self):
        self.assertEqual(HomePage.head_title, self.driver.title)

    def test_navigate_to_signin(self):
        homePage = HomePage(self.driver)
        homePage.click_on(HomePageLocators.SIGN_IN)
        homePage.wait_for_load(RegistrationPageLocators.CREATE_BUTTON)
        self.assertEqual(AuthenticationPage.head_title, self.driver.title)

    def test_navigate_to_women_dir(self):
        homePage = HomePage(self.driver)
        homePage.click_on(HomePageLocators.MENU_WOMEN)
        homePage.wait_for_load(HomePageLocators.CATALOGUE_NAME)
        self.assertEqual(HomePage.head_title_for_women_dir, self.driver.title)

    def test_navigate_to_dresses_dir(self):
        homePage = HomePage(self.driver)
        homePage.click_on(HomePageLocators.MENU_DRESSES)
        homePage.wait_for_load(HomePageLocators.CATALOGUE_NAME)
        self.assertEqual(HomePage.head_title_for_dresses_dir, self.driver.title)

    def test_navigate_to_tshirts_dir(self):
        homePage = HomePage(self.driver)
        homePage.click_on(HomePageLocators.MENU_TSHIRTS)
        homePage.wait_for_load(HomePageLocators.CATALOGUE_NAME)
        self.assertEqual(HomePage.head_title_for_tshirts_dir, self.driver.title)

    def test_add_to_cart(self):
        homePage = HomePage(self.driver)
        homePage.click_on(HomePageLocators.MENU_DRESSES)
        homePage.wait_for_load(HomePageLocators.CATALOGUE_NAME)
        number_of_items_on_start = homePage.number_of_items_in_cart()
        product_found = homePage.find_product_by('value', homePage.price_of_product_we_looking_for)
        if product_found:
            product_found.click()
            time.sleep(5)
        else:
            self.assertTrue(False,
                            "Cannot find product by given value: " + str(homePage.price_of_product_we_looking_for))
        homePage.wait_for_load(HomePageLocators.SUMMARYCARD_CLOSE)
        homePage.click_on(HomePageLocators.SUMMARYCARD_CLOSE)
        self.assertGreater(homePage.number_of_items_in_cart(), number_of_items_on_start,
                           "Number of products in cart is not greater than at starting point")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
