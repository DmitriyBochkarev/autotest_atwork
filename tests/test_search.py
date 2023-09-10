from pages.auth_page import AuthPage
from pages.main_page import MainPage
from conftest import web_browser
import time


class TestSearch:
    def test_search(self, web_browser):
        # 1) Зайти на https://anatoliinovikov.ru/projects/hotels/
        page = AuthPage(web_browser)
        page.get_url()
        time.sleep(3)
        # Убедиться что открылась страница логин
        page.check_auth_url()

        # 2) Проверить наличие поля логин
        page.find_login()

        # 3) Ввести в логин имейл
        page.text_login()

        # 4) Проверить наличие поля пароль
        page.find_password()

        # 5) Ввести пароль
        page.text_password()

        # 6) Проверить наличие кнопки войти
        page.find_btn_enter()

        # 7) Нажать на кнопку войти
        page.click_btn_enter()
        time.sleep(3)
        # Убедиться что открылась главная страница
        page.check_main_url()
        # Инициализировать новый объект Главная страница.
        main_page = MainPage(web_browser, web_browser.current_url)
        time.sleep(3)

        # 9)  Очистить поля поиска
        main_page.clear_search_location()
        time.sleep(3)

        # 10) Ввести в поле поиска Санкт-Петербург
        main_page.text_location()
        time.sleep(3)

        # 11) Нажать на кнопку поиска
        main_page.click_btn_search()

        # 12) Проверить, что появилась страница результатов поиска
        main_page.check_search_results()
