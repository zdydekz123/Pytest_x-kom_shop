import pytest
from pages.log_in_page import LoginIn
import allure

@pytest.mark.usefixtures('setup')
class TestLogIn:

    def prepare_page(self):
        cart_page = LoginIn(self.driver)
        # 1. Wejdź na stronę "https://www.x-kom.pl/".
        cart_page.open_page()
        return cart_page

    @allure.title('Test weryfiikacji poprawnego tytułu strony')
    @allure.description('Test sklepu komputerowego Xkom.pl')
    def test_page_title(self):
        # (VERIFICATION) Poprawnego tytulu strony internetowej sklepu.
        cart_page = self.prepare_page()

        assert 'x-kom.pl - Sklep komputerowy' in cart_page.check_page_title()

    @allure.title('Test logowania z pozytywnym rezultatem')
    @allure.description('Test sklepu komputerowego Xkom.pl')
    def test_log_in_passed(self):
        cart_page = self.prepare_page()

        # 2. Najedź kursorem myszy na przycisk "Twoje konto"
        cart_page.hover_on_my_account_icon()

        assert cart_page.is_log_in_button_displayed() is True

        # 3. Z Okna popup naciśnij w przycisk "Zaloguj się".
        cart_page.go_to_log_in()

        # 4. Wypełnij logowania o adres e-mail oraz hasło.
        cart_page.sign_in_form('zdybek1997@gmail.com', 'zdybek123')

        # 5. Naciśnij w przycisk "Zaloguj się"
        cart_page.login_in_submit()

        # (VERIFICATION) Czy przycisk wyloguj sie jest dostępny
        assert cart_page.is_logout_button_exist()


    @allure.title('Test logowania z negatywnym rezultatem')
    @allure.description('Test sklepu komputerowego Xkom.pl')
    def test_log_in_not_passed(self):
        cart_page = self.prepare_page()

        # 2. Najedź kursorem myszy na przycisk "Twoje konto"
        cart_page.hover_on_my_account_icon()

        assert cart_page.is_log_in_button_displayed() is True

        # 3. Z Okna popup naciśnij w przycisk "Zaloguj się".
        cart_page.go_to_log_in()

        # 4. Wypełnij logowania o adres e-mail oraz hasło.
        cart_page.sign_in_form('zdybek1997@gmail.com', 'zdybek')

        # 5. Naciśnij w przycisk "Zaloguj się"
        cart_page.login_in_submit()

        # (VERIFICATION) Czy informacja o niepoprawnym logowaniu jest dostępna
        assert 'Sprawdź, czy adres e-mail i hasło są poprawne' in cart_page.is_wrong_msg_displayed()