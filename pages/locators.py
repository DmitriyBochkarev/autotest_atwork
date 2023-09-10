from selenium.webdriver.common.by import By


class AuthPageLocators:
    locator_find_login = (By.CSS_SELECTOR, '.AuthForm_form__xobLX > .AuthForm_formItem__kqBY8:nth-child(1)')
    locator_find_password = (By.CSS_SELECTOR, '.AuthForm_form__xobLX > .AuthForm_formItem__kqBY8:nth-child(2)')
    locator_find_btn_enter = (By.CLASS_NAME, 'MyButton_button__q4IIh')


class MainPageLocators:
    locator_find_search_location = (
        By.CSS_SELECTOR, '.FilterBlock_body__hJKNC > form > .FilterBlock_formItem__MHmdR:nth-child(1) > input')
    locator_find_btn_search = (By.CLASS_NAME, 'MyButton_button__q4IIh')
    locator_find_search_results = (By.CLASS_NAME, 'HotelBlock_city__J4HJG')
