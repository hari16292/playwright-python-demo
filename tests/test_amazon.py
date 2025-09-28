import json

import pytest
from playwright.sync_api import Page, Playwright
from pytest_playwright.pytest_playwright import page

from pages.home_page import HomePage
from pages.product_page import ProductPage

# json file
with open('data/search_key.json') as json_file:
    test_data = json.load(json_file)
    search_key_list = test_data['search']


@pytest.mark.smoketest
@pytest.mark.parametrize('search_key', search_key_list)
def test_amazon_home(search_key, page):
    home = HomePage(page)
    home.go_to_home()
    search_results = home.search_product("search-alias=electronics", search_key["key"])
    allResults = page.locator(search_results.results)

    for i in range(3):
        title = allResults.nth(i).text_content()
        print("Home Page title:", title)
        assert "iphone" in title.lower()

        child_page = search_results.click_result_with_popup(i)
        product = ProductPage(child_page)
        print("Child Page title:", child_page.locator(product.title).text_content().strip())
        product.validate_title(title)
        product.add_to_cart_if_affordable(50000)
        break
