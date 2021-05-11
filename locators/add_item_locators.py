from selenium.webdriver.common.by import By

class SearchEngineLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Czego szukasz?"]')
    SEARCH_SUBMIT = (By.CSS_SELECTOR, 'button.apKoa')
    NO_SEARCH_RESULTS = (By.CLASS_NAME, 'jWLcUU')
    RESULT_COMPLEMENT = (By.CLASS_NAME, 'ceCpjl')
    AMOUNT_SEARCH_RESULTS = (By.CLASS_NAME, 'gfzxIs')

class AddToCartLocators:
    FIND_PRODUCT = (By.XPATH, '//button[@title="Dodaj do koszyka" and not(@disabled)]')
    ORDER_POPUP = (By.CLASS_NAME, 'modal')
    GO_TO_CART = (By.PARTIAL_LINK_TEXT, 'Przejdź do koszyka')

class VerificationOrder:
    VERIFY_PRODUCT = (By.CLASS_NAME, 'esEJdj')
    GO_TO_DELIVERY = (By.CLASS_NAME, 'jSCQpQ')