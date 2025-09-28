from playwright.sync_api import Page, expect
from utils.helpers import parse_price

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = "span#productTitle"
        self.price = "#corePriceDisplay_desktop_feature_div .a-price-whole"
        self.confirm_price = ".a-price.sw-subtotal-amount .a-price-whole"
        self.add_to_cart_button = "button[name='Add to Cart'], [role='button'][name='Add to Cart']"
        self.confirmation_msg = "#NATC_SMART_WAGON_CONF_MSG_SUCCESS"
        self.checkout_button = "input[name*='proceedToRetailCheckout']"
        self.login_continue = "#continue-announce"

    def validate_title(self, expected_title: str):
        expect(self.page.locator(self.title)).to_have_text(expected_title)

    def get_price(self) -> int:
        price_text = self.page.locator(self.price).text_content()
        return parse_price(price_text)

    def add_to_cart_if_affordable(self, max_price: int):
        price = self.get_price()
        if price <= max_price:
            self.page.get_by_role("button", name="Add to Cart").click()
            expect(self.page.locator(self.confirmation_msg)).to_contain_text("Added to cart")

            confirm_price = parse_price(self.page.locator(self.confirm_price).text_content())
            assert confirm_price == price

            self.page.locator(self.checkout_button).click()
            expect(self.page.locator(self.login_continue)).to_be_visible()
