from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    EMAIL_FIELD = (By.ID, "email_create")
    CREATE_BUTTON = (By.ID, "SubmitCreate")
    ALERT_FIELD = (By.XPATH, "//div[contains(@class,'alert alert-danger')]/ol/li")
    GENDER_MR_CHECKBOX = (By.ID,"uniform-id_gender1")
    GENDER_MRS_CHECKBOX = (By.ID,"uniform-id_gender2")
    FIRSTNAME_FIELD = (By.ID, "customer_firstname")
    LASTNAME_FIELD = (By.ID, "customer_lastname")
    EMAIL_CHECK_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "passwd")
    DATE_DAY_SELECTOR = (By.ID, "days")
    DATE_MONTH_SELECTOR = (By.ID, "months")
    DATE_YEAR_SELECTOR = (By.ID, "years")
    FIRSTNAME_CHECK_FIELD = (By.ID, "firstname")
    LASTNAME_CHECK_FIELD = (By.ID, "lastname")
    ADDRESS_FIELD = (By.ID, "address1")
    CITY_FIELD = (By.ID, "city")
    STATE_SELECTOR = (By.ID, "id_state")
    POSTCODE_FIELD = (By.ID, "postcode")
    COUNTRY_SELECTOR = (By.ID, "id_country")
    PHONE_FIELD = (By.ID, "phone_mobile")
    REGISTER_BUTTON = (By.ID, "submitAccount")

class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "passwd")
    SIGNIN_BUTTON = (By.ID, "SubmitLogin")
