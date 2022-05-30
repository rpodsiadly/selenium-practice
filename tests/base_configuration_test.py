import unittest
from selenium import webdriver


class BaseHomePageTest(unittest.TestCase):
    def setUp(self):
        # default settings for githubactions:
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        # end of default settings
        
        # visual env settings - you should comment #8 #9 #10 line and uncomment #14 #15 line
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # end of visual env
        
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class BaseAuthenticationPageTest(unittest.TestCase):
    def setUp(self):
        # default settings for githubactions:
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        # end of default settings
        
        # visual env settings - you should comment #29 #30 #31 line and uncomment #35 #36 line
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # end of visual env

        self.driver.get("http://automationpractice.com/index.php?controller=authentication")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
