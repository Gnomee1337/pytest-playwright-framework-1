import random

from pages.base_page import BasePage
from utils.data_generator import generated_person
from logger import mylogger
from playwright.sync_api import expect
import allure


class TextBoxPage(BasePage):
    # Form fields
    FULL_NAME = "input#userName"
    EMAIL = "input[id='userEmail']"
    CURRENT_ADDRESS = "textarea[id='currentAddress']"
    PERMANENT_ADDRESS = "textarea[id='permanentAddress']"
    SUBMIT = "button[id='submit']"

    # Created form
    CREATED_FULL_NAME = "#output #name"
    CREATED_EMAIL = "#output #email"
    CREATED_CURRENT_ADDRESS = "#output #currentAddress"
    CREATED_PERMANENT_ADDRESS = "#output #permanentAddress"

    @allure.step("Fill all fields in Text Box")
    def fill_all_fields(self):
        mylogger.info(f"Open page: {self.base_url} and input data")
        person_info = next(generated_person())
        # self.page.goto(url=self.base_url)
        self.page.locator(selector=self.FULL_NAME).fill(value=person_info.full_name)
        self.page.locator(selector=self.EMAIL).fill(value=person_info.email)
        self.page.locator(selector=self.CURRENT_ADDRESS).fill(value=person_info.current_address)
        self.page.locator(selector=self.PERMANENT_ADDRESS).fill(value=person_info.permanent_address)
        mylogger.info("Click 'Submit' button")
        self.page.locator(selector=self.SUBMIT).click()
        mylogger.info("Data submitted")
        return [person_info.full_name, person_info.email, person_info.current_address, person_info.permanent_address]

    @allure.step("Get all filled data from Text Box")
    def check_filled_form(self):
        mylogger.info("Get form data")
        full_name = self.page.locator(self.CREATED_FULL_NAME).text_content().split(':')[1]
        email = self.page.locator(self.CREATED_EMAIL).text_content().split(':')[1]
        current_address = self.page.locator(self.CREATED_CURRENT_ADDRESS).text_content().split(':')[1].rstrip()
        permanent_address = self.page.locator(self.CREATED_PERMANENT_ADDRESS).text_content().split(':')[1]
        return [full_name, email, current_address, permanent_address]


class CheckBoxPage(BasePage):
    EXPAND_ALL_BUTTON = 'button.rct-option-expand-all'
    ITEM_LIST = 'span.rct-title'
    CHECKED_ITEMS = 'svg.rct-icon-check.rct-icon'
    TITLE_ITEM = "xpath=.//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = 'span.text-success'

    @allure.step('open full list')
    def open_full_list(self):
        self.page.locator(self.EXPAND_ALL_BUTTON).click()

    @allure.step('click random checkbox')
    def click_random_checkbox(self):
        item_list = self.page.locator(self.ITEM_LIST).all()
        item_list[random.randint(1, len(item_list))].click()

    @allure.step('get titles of checked checkboxes')
    def get_checked_checkboxes(self):
        checked_list = self.page.locator(self.CHECKED_ITEMS).all()
        checked_item_names = []
        for checked_element in checked_list:
            checked_item_title = checked_element.locator(self.TITLE_ITEM).text_content()
            checked_item_names.append(checked_item_title)
        return str(checked_item_names).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('get names of checked checkboxes from "You have selected"')
    def get_selected_result(self):
        checked_checkboxes = self.page.locator(self.OUTPUT_RESULT).all()
        result_titles_of_checked_checkboxes = []
        for checkbox in checked_checkboxes:
            result_titles_of_checked_checkboxes.append(checkbox.text_content())
        return str(result_titles_of_checked_checkboxes).lower().replace(' ', '')
