from webbrowser import Chrome

import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser to use")

@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch()
    elif browser_name == "firefox":
        browser = playwright.firefox.launch()

    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()



