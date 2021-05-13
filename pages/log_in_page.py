from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from locators.log_in_locators import LogInLocators
from pages.base_page import BasePage
import allure


class LoginIn(BasePage):

    def open_page(self):
        self.driver.get('https://www.x-kom.pl/')

    @allure.step('Weryfikacja zgodności tytułu sklepu')
    def check_page_title(self):
        self.logger.info('[LOGS] Weryfikacja zgodności tytułu sklepu')
        get_title = self.driver.title
        allure.attach(self.driver.get_screenshot_as_png(), name='check_page_title', attachment_type=allure.attachment_type.PNG)
        return get_title

    @allure.step('Czy logowanie do sklepu jest dostępne')
    def hover_on_my_account_icon(self):
        self.logger.info('[LOGS] Czy logowanie do sklepu jest dostępne')
        action = ActionChains(self.driver)
        icon = self.driver.find_element(*LogInLocators.YOUR_ACCOUNT_POPUP)
        action.move_to_element(icon).perform()
        allure.attach(self.driver.get_screenshot_as_png(), name='hover_on_my_account_icon', attachment_type=allure.attachment_type.PNG)

    @allure.step('Czy przycisk do logowania jest widoczny')
    def is_log_in_button_displayed(self):
        self.logger.info('[LOGS] Czy przycisk do logowania jest widoczny')
        log_in_button = self.driver.find_element(*LogInLocators.LOG_IN_BUTTON)
        allure.attach(self.driver.get_screenshot_as_png(), name='is_log_in_button_displayed', attachment_type=allure.attachment_type.PNG)
        return log_in_button.is_displayed()

    @allure.step('Przechodzenie do sesji logowania')
    def go_to_log_in(self):
        self.logger.info('[LOGS] Przechodzenie do sesji logowania')
        log_in_button = self.driver.find_element(*LogInLocators.LOG_IN_BUTTON)
        log_in_button.click()
        allure.attach(self.driver.get_screenshot_as_png(), name='go_to_log_in', attachment_type=allure.attachment_type.PNG)

    @allure.step('Formularz logowania: email: {1} oraz hasło: {2}')
    def sign_in_form(self, email, password):
        self.logger.info('[LOGS] Formularz logowania: email: {email} oraz hasło: {password}'.format(email=email, password=password))
        input_email = self.driver.find_element(*LogInLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_password = self.driver.find_element(*LogInLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name='sign_in_form', attachment_type=allure.attachment_type.PNG)

    @allure.step('Czy komunikat o niepoprawnym logowaniu jest dostępny')
    def is_wrong_msg_displayed(self):
        self.logger.info('[LOGS] Czy komunikat o niepoprawnym logowaniu jest dostępny')
        wrong_message = self.driver.find_element(*LogInLocators.WRONG_MSG)
        allure.attach(self.driver.get_screenshot_as_png(), name='is_wrong_msg_displayed', attachment_type=allure.attachment_type.PNG)
        return wrong_message.text

    @allure.step('Zatwierdzenie próby logowania')
    def login_in_submit(self):
        self.logger.info('[LOGS] Zatwierdzenie próby logowania')
        submit_button = self.driver.find_element(*LogInLocators.SUBMIT_LOG_IN)
        submit_button.click()
        allure.attach(self.driver.get_screenshot_as_png(), name='login_in_submit', attachment_type=allure.attachment_type.PNG)

    @allure.step('Weryfikacja czy przycisk wylogowania jest dostępny')
    def is_logout_button_exist(self):
        self.logger.info('[LOGS] Weryfikacja czy przycisk wylogowania jest dostępny')
        try:
            self.driver.find_element(*LogInLocators.LOG_OUT_BUTTON)
            allure.attach(self.driver.get_screenshot_as_png(), name='is_logout_button_exist', attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name='is_logout_button_exist', attachment_type=allure.attachment_type.PNG)
            return False
        return True
