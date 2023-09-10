from pages.auth_page import AuthPage
from conftest import web_browser
import time


class TestSearch:
    def test_search(self, web_browser):
        # 1) Зайти на https://anatoliinovikov.ru/projects/hotels/
        page = AuthPage(web_browser)
        page.get_url()

        # 2) Проверить наличие поля логин
        page.find_login()

        # 4) Ввести в логин имейл
        page.text_login()

        # 5) Проверить наличие поля пароль
        page.find_password()

        # 6) Ввести пароль
        page.text_password()

        # 7) Проверить наличие кнопки войти и нажать
        page.find_btn_enter().click()

