from pages.base_page import BasePage
from pages.locators import MainPageLocators
import time


class MainPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

    def find_search_location(self):
        """ Найти поле поиска """
        element = self.find_webelement(MainPageLocators.locator_find_search_location)
        return element

    def clear_search_location(self):
        """ Очистить поле поиска """
        element = self.find_webelement(MainPageLocators.locator_find_search_location).clear()
        return element

    def text_location(self):
        """ Ввести в поле поиска Санкт-Петербург """
        element = self.find_webelement(MainPageLocators.locator_find_search_location).send_keys('Санкт-Петербург')
        return element

    def find_btn_search(self):
        """ Найти кнопку поиска """
        element = self.find_webelement(MainPageLocators.locator_find_btn_search)
        return element

    def click_btn_search(self):
        """ Нажать кнопку поиска """
        element = self.find_webelement(MainPageLocators.locator_find_btn_search).click()
        return element

    def check_search_results(self):
        """ Проверить результаты поиска """
        element_text = self.find_webelement(MainPageLocators.locator_find_search_results).text
        expected_text = 'Санкт-Петербург'
        assert element_text == expected_text, "Результаты поиска по Санкт-Петербургу отсутствуют"
