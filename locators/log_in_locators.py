from selenium.webdriver.common.by import By

class LogInLocators:
    YOUR_ACCOUNT_POPUP = (By.CLASS_NAME, 'bolRtX')
    LOG_IN_BUTTON = (By.CSS_SELECTOR, 'a.kwClzl[href="/logowanie"]')
    INPUT_EMAIL = (By.XPATH, '//input[@name="login"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    SUBMIT_LOG_IN = (By.XPATH, '//button[@type="submit"]')
    WRONG_MSG = (By.XPATH, '//span[@class="dttHhd"]')
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, 'a.kwClzl[href="/wyloguj"]')