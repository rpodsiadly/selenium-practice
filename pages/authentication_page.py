from locators.authentication_page_locators import RegistrationPageLocators
from selenium.webdriver.support import expected_conditions as exp_con
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from faker import Faker


class AuthenticationPage:
    head_title = "Login - My Store"
    head_title_registration_positive = "My account - My Store"
    result = {}
    register_mail_too_long = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb@aaaaaaaaaaaaaa.com"
    register_mail_already_taken = "aa@aa.com"
    register_firstname = "Bob"
    register_lastname = "Sparkley"
    register_password = "12345"
    register_date_day = "30"
    register_date_month = "1"
    register_date_year = "1950"
    register_address = "Avenue Street 30C"
    register_city = "Montgomery"
    register_state = "1"
    register_postcode = "36043"
    register_phonenumber = "733210209"
    login_email_positive = "bob@sparkley.com"
    login_password_positive = "12345"
    login_incorrect_syntax_email = "bobsparkley.com"
    login_email_not_in_database = "bb000b@sparkley.com"

    def __init__(self, driver):
        self.fake_email_address = None
        self.driver = driver

    def fill_in(self, locator, input_text):
        WebDriverWait(self.driver, 50).until(exp_con.presence_of_element_located(locator)).send_keys(input_text)

    def click_on(self, web_element_to_click):
        WebDriverWait(self.driver, 50).until(exp_con.presence_of_element_located(web_element_to_click)).click()

    def choose_selector(self, locator_of_element, value):
        select_locator = Select(self.driver.find_element(*locator_of_element))
        select_locator.select_by_value(value)

    def check_error(self):
        WebDriverWait(self.driver, 50).until(exp_con.presence_of_element_located(RegistrationPageLocators.ALERT_FIELD))
        registration_message = self.driver.find_element(*RegistrationPageLocators.ALERT_FIELD)
        self.result = {'result_boolean': True, 'message': (registration_message.get_attribute("textContent")).strip()}
        print(self.result["message"])

    def fake_email(self):
        fake = Faker()
        self.fake_email_address = (
                    (fake.name()).replace(" ", "") + str(fake.random.randint(0, 1000)) + "@" + (fake.name()).replace(
                " ", "") + str(fake.random.randint(0, 1000)) + ".com").lower()
        return self.fake_email_address

    def fullfill_the_registration_form(self, incorrect_data_field, incorrect_value):
        self.click_on(RegistrationPageLocators.GENDER_MR_CHECKBOX)
        self.fill_in(RegistrationPageLocators.FIRSTNAME_FIELD, self.register_firstname)
        self.fill_in(RegistrationPageLocators.LASTNAME_FIELD, self.register_lastname)
        if incorrect_data_field == "incorrectPassword":
            self.fill_in(RegistrationPageLocators.PASSWORD_FIELD, incorrect_value)
        elif incorrect_data_field == "blankPassword":
            pass
        else:
            self.fill_in(RegistrationPageLocators.PASSWORD_FIELD, self.register_password)
        self.choose_selector(RegistrationPageLocators.DATE_DAY_SELECTOR, self.register_date_day)
        if incorrect_data_field == "incorrectDate":
            self.choose_selector(RegistrationPageLocators.DATE_MONTH_SELECTOR, incorrect_value)
        else:
            self.choose_selector(RegistrationPageLocators.DATE_MONTH_SELECTOR, self.register_date_month)
        self.choose_selector(RegistrationPageLocators.DATE_YEAR_SELECTOR, self.register_date_year)
        self.fill_in(RegistrationPageLocators.ADDRESS_FIELD, self.register_address)
        self.fill_in(RegistrationPageLocators.CITY_FIELD, self.register_city)
        self.choose_selector(RegistrationPageLocators.STATE_SELECTOR, self.register_state)
        self.fill_in(RegistrationPageLocators.POSTCODE_FIELD, self.register_postcode)
        self.fill_in(RegistrationPageLocators.PHONE_FIELD, self.register_phonenumber)
        self.click_on(RegistrationPageLocators.REGISTER_BUTTON)

    def is_email_ok(self):
        WebDriverWait(self.driver, 50).until(exp_con.presence_of_element_located(RegistrationPageLocators.GENDER_MR_CHECKBOX))
        check_field = self.driver.find_element(*RegistrationPageLocators.EMAIL_CHECK_FIELD)
        mail=check_field.get_attribute("value")
        if mail == self.fake_email_address:
            return True
        else:
            return False
