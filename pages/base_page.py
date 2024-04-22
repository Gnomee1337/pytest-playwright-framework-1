from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    @allure.step('open page')
    def open(self, url: str):
        self.page.goto(url)