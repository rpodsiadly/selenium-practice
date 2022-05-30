from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_con
from selenium.webdriver.support.ui import WebDriverWait
from locators.home_page_locators import HomePageLocators


class HomePage:
    head_title = "My Store"
    head_title_for_women_dir = "Women - My Store"
    head_title_for_dresses_dir = "Dresses - My Store"
    head_title_for_tshirts_dir = "T-shirts - My Store"
    price_of_product_we_looking_for = 26.00

    def __init__(self, driver):
        self.driver = driver

    def click_on(self, web_element):
        WebDriverWait(self.driver, 30).until(exp_con.presence_of_element_located(web_element)).click()
        sleep(1)

    def number_of_items_in_cart(self):
        number_of_items = self.driver.find_element(*HomePageLocators.CART_QUANTITY)
        return int(number_of_items.get_attribute("textContent").strip())

    def find_product_by(self, by_attribute, value):
        WebDriverWait(self.driver, 30).until(exp_con.presence_of_element_located(HomePageLocators.PRODUCTS_PRICES))
        if by_attribute == 'value':
            products = self.driver.find_elements(*HomePageLocators.PRODUCTS_PRICES)

            for product_price in products:
                if float(product_price.text[1:]) == value:
                    parent_element = product_price.find_element(By.XPATH,'..')
                    return parent_element
            return False
        else:
            return False

    def wait_for_load(self,locator):
        WebDriverWait(self.driver, 30).until(exp_con.presence_of_element_located(locator))