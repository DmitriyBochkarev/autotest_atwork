from pages.base_page import BasePage
from pages.locators import AuthPageLocators


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://anatoliinovikov.ru/projects/hotels/"

    def check_auth_url(self):
        """ Проверка, что открылась форма авторизации https://anatoliinovikov.ru/projects/hotels/auth """
        expected_url = 'https://anatoliinovikov.ru/projects/hotels/auth'
        current_url = self.get_current_url()
        assert current_url == expected_url, "Не открылась форма авторизации"

    def find_login(self):
        """ Найти поле логин """
        element = self.find_webelement(AuthPageLocators.locator_find_login)
        return element

    def text_login(self):
        """ Ввести в поле логин имейл """
        element = self.find_login().send_keys('admin@mail.ru')
        return element

    def find_password(self):
        """ Найти поле пароль """
        element = self.find_webelement(AuthPageLocators.locator_find_password)
        return element

    def text_password(self):
        """ Ввести пароль """
        element = self.find_password().send_keys('1234567890qwerty')
        return element

    def find_btn_enter(self):
        """ Найти кнопку Войти """
        element = self.find_webelement(AuthPageLocators.locator_find_btn_enter)
        return element

    def click_btn_enter(self):
        """ Нажать кнопку Войти """
        element = self.find_webelement(AuthPageLocators.locator_find_btn_enter).click()
        return element

    def check_main_url(self):
        """ Проверка, что перешли на страницу https://anatoliinovikov.ru/projects/hotels/ """
        expected_url = 'https://anatoliinovikov.ru/projects/hotels/'
        current_url = self.get_current_url()
        assert current_url == expected_url, "Мы не перешли на url https://anatoliinovikov.ru/projects/hotels/"
