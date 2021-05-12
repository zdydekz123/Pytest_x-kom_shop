import pytest
import allure
from utils.driver_factory import DriverFactory

@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver('chrome')
    driver.implicitly_wait(10)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=allure.attachment_type.PNG)
    driver.quit()