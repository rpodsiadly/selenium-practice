from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN = (By.PARTIAL_LINK_TEXT, "Sign in")
    MENU_WOMEN = (By.XPATH, "//div[contains(@id,'block_top_menu')]/ul/li/a[contains(@title,'Women')]")
    MENU_DRESSES = (By.XPATH, "//div[contains(@id,'block_top_menu')]/ul/li/a[contains(@title,'Dresses')]")
    MENU_TSHIRTS = (By.XPATH, "//div[contains(@id,'block_top_menu')]/ul/li/a[contains(@title,'T-shirts')]")
    CART_QUANTITY = (By.XPATH, "//div[contains(@class,'shopping_cart')]/a/span[contains(@class,'ajax_cart_quantity')]")
    PRODUCTS_PRICES = (By.XPATH, "//div[contains(@class,'right-block')]/div/span[contains(@itemprop,'price')]")
    SUMMARYCARD_CLOSE = (By.XPATH, "//span[contains(@class,'cross')]")
    CATALOGUE_NAME = (By.XPATH,"//span[contains(@class,'cat-name')]")
