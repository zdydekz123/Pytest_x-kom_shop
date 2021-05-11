from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.add_item_locators import SearchEngineLocators, AddToCartLocators, VerificationOrder
from pages.base_page import BasePage
import allure


class AddItemToCart(BasePage):

    def open_page(self):
        self.driver.get('https://www.x-kom.pl/')

    @allure.step('Weryfikacja zgodności tytułu sklepu')
    def check_page_title(self):
        get_title = self.driver.title
        allure.attach(self.driver.get_screenshot_as_png(), name='check_page_title', attachment_type=allure.attachment_type.PNG)
        return get_title

    @allure.step('Czy wyszukiwarka strony jest widoczna')
    def is_search_field_displayed(self):
        search_field = self.driver.find_element(*SearchEngineLocators.SEARCH_FIELD)
        allure.attach(self.driver.get_screenshot_as_png(), name='is_search_field_displayed', attachment_type=allure.attachment_type.PNG)
        return search_field.is_displayed()

    @allure.step('Weryfikacja poprawnej wartości placeholdera')
    def checkout_placeholder_value(self):
        wait = WebDriverWait(self.driver, 40)
        placeholder = wait.until(EC.presence_of_element_located(SearchEngineLocators.SEARCH_FIELD))
        allure.attach(self.driver.get_screenshot_as_png(), name='checkout_placeholder_value', attachment_type=allure.attachment_type.PNG)
        return placeholder.get_attribute('placeholder')

    @allure.step('Kliknięcie w puste pole wyszukiwarki')
    def click_on_search_input(self):
        search_field = self.driver.find_element(*SearchEngineLocators.SEARCH_FIELD)
        search_field.click()
        allure.attach(self.driver.get_screenshot_as_png(), name='click_on_search_input', attachment_type=allure.attachment_type.PNG)

    @allure.step('Wpisana wartość w pole wyszukiwarki to "{1}"')
    def type_proper_value(self, item_name):
        search_value = self.driver.find_element(*SearchEngineLocators.SEARCH_FIELD)
        search_value.send_keys(item_name)
        allure.attach(self.driver.get_screenshot_as_png(), name='type_proper_value', attachment_type=allure.attachment_type.PNG)
        return item_name

    @allure.step('Czy przycisk zatwierdzenia jest dostępny')
    def is_submit_button_enabled(self):
        submit_value = self.driver.find_element(*SearchEngineLocators.SEARCH_SUBMIT)
        allure.attach(self.driver.get_screenshot_as_png(), name='is_submit_button_enabled',attachment_type=allure.attachment_type.PNG)
        return submit_value.is_enabled()

    @allure.step('Wyszukiwanie pożądanej wartości')
    def submit_typed_value(self):
        submit_value = self.driver.find_element(*SearchEngineLocators.SEARCH_SUBMIT)
        submit_value.click()
        allure.attach(self.driver.get_screenshot_as_png(), name='submit_typed_value', attachment_type=allure.attachment_type.PNG)

    @allure.step('Weryfikacji znalezionych produktów o podanej wartości')
    def checkout_searched_value(self):
        try:
            result = self.driver.find_element(*SearchEngineLocators.NO_SEARCH_RESULTS).get_attribute('textContent')
            complement = self.driver.find_element(*SearchEngineLocators.RESULT_COMPLEMENT).get_attribute('textContent')
            allure.attach(self.driver.get_screenshot_as_png(), name='checkout_searched_value', attachment_type=allure.attachment_type.PNG)
            assert 'Brak wyników dla ' + complement + '.' not in result
        except NoSuchElementException:
            amount = self.driver.find_element(*SearchEngineLocators.AMOUNT_SEARCH_RESULTS).get_attribute('textContent')
            str_amount_result = 'Ilość znalezionych produktów: '
            allure.attach(self.driver.get_screenshot_as_png(), name='checkout_searched_value', attachment_type=allure.attachment_type.PNG)
            return str_amount_result + amount

    @allure.step('Wybranie danego produktu z listy')
    def select_available_item(self):
        item_visible = self.driver.find_elements(*AddToCartLocators.FIND_PRODUCT)
        item_visible[0].click()
        allure.attach(self.driver.get_screenshot_as_png(), name='select_available_item', attachment_type=allure.attachment_type.PNG)

    @allure.step('Czy okno kontynuacji zakupu jest dostępne')
    def is_continuation_popup_displayed(self):
        wait = WebDriverWait(self.driver, 40)
        order_popup = wait.until(EC.visibility_of_element_located(AddToCartLocators.ORDER_POPUP))
        allure.attach(self.driver.get_screenshot_as_png(), name='is_continuation_popup_displayed', attachment_type=allure.attachment_type.PNG)
        return order_popup.is_displayed()

    @allure.step('Przejście do koszyka')
    def go_to_cart(self):
        order_popup = self.driver.find_element(*AddToCartLocators.ORDER_POPUP)
        button_gtc = self.driver.find_element(*AddToCartLocators.GO_TO_CART)
        if order_popup.is_displayed():
            button_gtc.click()
            allure.attach(self.driver.get_screenshot_as_png(), name='go_to_cart', attachment_type=allure.attachment_type.PNG)
        else:
            self.driver.close()
            allure.attach(self.driver.get_screenshot_as_png(), name='go_to_cart', attachment_type=allure.attachment_type.PNG)

    @allure.step('Weryfikacja ilości produktów dodanych do koszyka')
    def check_cart_value(self):
        wait = WebDriverWait(self.driver, 40)
        value_cart = wait.until(EC.visibility_of_element_located(VerificationOrder.VERIFY_PRODUCT))
        go_delivery = wait.until(EC.element_to_be_clickable(VerificationOrder.GO_TO_DELIVERY))
        str_message = 'Ilość produktów dodanych do koszyka: '
        if value_cart.text[-1] != '0':
            go_delivery.click()
            allure.attach(self.driver.get_screenshot_as_png(), name='check_cart_value', attachment_type=allure.attachment_type.PNG)
            return str_message + value_cart.text[-1]
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='check_cart_value', attachment_type=allure.attachment_type.PNG)
            return str_message + value_cart.text[-1]