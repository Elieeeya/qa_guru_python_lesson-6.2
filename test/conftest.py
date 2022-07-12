from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com/'


