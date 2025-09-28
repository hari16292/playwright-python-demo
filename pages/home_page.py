from playwright.sync_api import Page, expect

from pages.search_results_page import SearchResultsPage


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = "#nav-logo-sprites"
        self.category_dropdown = "#searchDropdownBox"
        self.search_input = "input[name='field-keywords']"
        self.search_button = "#nav-search-submit-button"

    def go_to_home(self):
        self.page.goto("https://amazon.in")
        expect(self.page.locator(self.logo)).to_be_visible()

    def search_product(self, category: str, product: str):
        self.page.select_option(self.category_dropdown, category)
        self.page.get_by_label("Search Amazon.in").fill(product)
        self.page.locator(self.search_button).click()
        return SearchResultsPage(self.page)
