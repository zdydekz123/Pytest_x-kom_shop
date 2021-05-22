import pytest
from pages.add_to_cart_page import AddItemToCart
from utils.excel_reader import ExcelReader
import allure

@pytest.mark.usefixtures('setup')
class TestAddToCart:
        
    def prepare_page(self):
        cart_page = AddItemToCart(self.driver)
        # 1. Wejdź na stronę "https://www.x-kom.pl/".
        cart_page.open_page()
        return cart_page

    @allure.title('Test weryfiikacji poprawnego tytułu strony')
    @allure.description('Test sklepu komputerowego Xkom.pl')
    def test_page_title(self):
        # (VERIFICATION) Poprawnego tytulu strony internetowej sklepu.
        cart_page = self.prepare_page()
        assert 'x-kom.pl - Sklep komputerowy' in cart_page.check_page_title()

    @allure.title('Test głównej wyszukiwarki sklepu')
    @allure.description('Test sklepu komputerowego Xkom.pl')
    def test_is_search_field_displayed(self):
        # (VERIFICATION) Czy jest dostepna wyszukiwarka sklepu xkom.pl.
        cart_page = self.prepare_page()
        placeholder = cart_page.checkout_placeholder_value()
        cart_page.click_on_search_input()

        assert cart_page.is_search_field_displayed() is True
        assert placeholder == 'Czego szukasz?'

    @allure.title('Test dodawania produktu do koszyka')
    @allure.description('Test sklepu komputerowego Xkom.pl')
    @pytest.mark.parametrize('data', ExcelReader.search_data())
    def test_add_item_to_cart(self, data):
        cart_page = self.prepare_page()

        # 2. Kliknij w puste pole głównej wyszukiwarki sklepu.
        cart_page.click_on_search_input()

        # 3. W polu wyszukiwarki wpisz wartość "laptop".
        value = cart_page.type_proper_value(data.typed_value)
        assert value == 'laptop'

        # 4. Wyszukaj pozadana wartosc naciskajac w submit button.
        cart_page.submit_typed_value()
        assert cart_page.is_submit_button_enabled() is True

        # (VERIFICATION) Ilość wyników wyszukiwania!!
        cart_page.checkout_searched_value()

        # 5. Kolejno z listy produktów, wybierz element z dostępnym przyciskiem "Dodaj do koszyka”.
        cart_page.select_available_item()
        assert cart_page.is_continuation_popup_displayed() is True

        # 6. Po wyświetleniu okna Popup kliknij w przycisk "Przejdź do koszyka".
        cart_page.go_to_cart()

        # (VERIFICATION) Czy produkt został poprawnie dodany do koszyka.
        cart_page.check_cart_value()