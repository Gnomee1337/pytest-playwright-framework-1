import time

import allure
from pages.elements_page import TextBoxPage, CheckBoxPage
from playwright.sync_api import Page, expect


@allure.suite("Elements")
class TestElements:
    @allure.feature("Text Box Page")
    class TestTextBox:
        @allure.title("Test text box")
        def test_text_box(self, page: Page):
            text_box_page = TextBoxPage(page, base_url="https://demoqa.com/text-box")
            text_box_page.open(text_box_page.base_url)
            filled_data = text_box_page.fill_all_fields()
            result_data = text_box_page.check_filled_form()
            assert filled_data == result_data,  "input_data doesnt match output_data in Text Box"

    @allure.feature("Check Box Page")
    class TestCheckBox:
        @allure.title("Check check box")
        def test_check_box(self, page: Page):
            check_box_page = CheckBoxPage(page, base_url="https://demoqa.com/checkbox")
            check_box_page.open(check_box_page.base_url)
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_data = check_box_page.get_checked_checkboxes()
            output_data = check_box_page.get_selected_result()
            assert input_data == output_data, "selected checkboxes doesnt match in Check Box"
