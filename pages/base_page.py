import logging

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)