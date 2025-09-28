from playwright.sync_api import Page, expect

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.results = ".a-section.a-spacing-small.a-spacing-top-small h2 span"

    def get_top_results(self, count=3):
        return [self.results, count]

    def click_result_with_popup(self, index: int):
        allResults = self.page.locator(self.results)
        with self.page.expect_popup() as newPage_info:
            allResults.nth(index).click()
        return newPage_info.value
