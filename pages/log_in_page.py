from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from locators.log_in_locators import LogInLocators
from pages.base_page import BasePage


class LoginIn(BasePage):

    def open_page(self):
        self.driver.get('https://www.x-kom.pl/')

    def check_page_title(self):
        get_title = self.driver.title
        return get_title

    def hover_on_my_account_icon(self):
        action = ActionChains(self.driver)
        icon = self.driver.find_element(*LogInLocators.YOUR_ACCOUNT_POPUP)
        action.move_to_element(icon).perform()

    def is_log_in_button_displayed(self):
        log_in_button = self.driver.find_element(*LogInLocators.LOG_IN_BUTTON)
        return log_in_button.is_displayed()

    def go_to_log_in(self):
        log_in_button = self.driver.find_element(*LogInLocators.LOG_IN_BUTTON)
        log_in_button.click()

    def sign_in_form(self, email, password):
        input_email = self.driver.find_element(*LogInLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        input_password = self.driver.find_element(*LogInLocators.INPUT_PASSWORD)
        input_password.send_keys(password)

    def is_wrong_msg_displayed(self):
        wrong_message = self.driver.find_element(*LogInLocators.WRONG_MSG)
        return wrong_message.text

    def login_in_submit(self):
        submit_button = self.driver.find_element(*LogInLocators.SUBMIT_LOG_IN)
        submit_button.click()

    def is_logout_button_exist(self):
        try:
            self.driver.find_element(*LogInLocators.LOG_OUT_BUTTON)
        except NoSuchElementException:
            return False
        return True
