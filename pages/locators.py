from selenium.webdriver.common.by import By


class AuthPageLocators:
    locator_find_login = (By.CSS_SELECTOR, '.AuthForm_form__xobLX > .AuthForm_formItem__kqBY8:nth-child(1)')
    locator_find_password = (By.CSS_SELECTOR, '.AuthForm_form__xobLX > .AuthForm_formItem__kqBY8:nth-child(2)')
    locator_find_btn_enter = (By.CLASS_NAME, 'MyButton_button__q4IIh')
