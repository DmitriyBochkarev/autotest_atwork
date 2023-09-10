from pages.base_page import BasePage
from pages.locators import AuthPageLocators
import time

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://anatoliinovikov.ru/projects/hotels/"

    def find_login(self):
        """ Найти поле логин"""
        element = self.find_webelement(AuthPageLocators.locator_find_login)
        return element

    def text_login(self):
        """ввести в поле логин имейл"""
        element = self.find_login().send_keys('admin@mail.ru')
        return element

    def find_password(self):
        """ Найти поле пароль"""
        element = self.find_webelement(AuthPageLocators.locator_find_password)
        return element


    def text_password(self):
        """ввести в поле логин имейл"""
        element = self.find_password().send_keys('1234567890qwerty')
        return element

    def find_btn_enter(self):
        """ввести в поле логин имейл"""
        element = self.find_webelement(AuthPageLocators.locator_find_btn_enter)
        return element
