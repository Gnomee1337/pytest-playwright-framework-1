import base64
from datetime import datetime

import allure
import pytest
from playwright.sync_api import sync_playwright
from logger import mylogger

# @pytest.fixture(scope='session')
# def set_env(pytestconfig):
#     with sync_playwright() as playwright:
#         mylogger.info("page session started")
#         browser = playwright.chromium.launch(headless=False, timeout=5)
#         context = browser.new_context()
#         page = context.new_page()
#         # context.tracing.start(screenshots=True, snapshots=True, sources=True)
#         yield page
#         screenshot_bytes = page.screenshot()
#         print(base64.b64encode(screenshot_bytes).decode())
#         allure.attach(base64.b64encode(screenshot_bytes).decode(), name=f"Screenshot {datetime.today()}",
#                       attachment_type=allure.attachment_type.JPG)
#         mylogger.info("page session finished")
#         # context.tracing.stop(path=f"{domain}_trace.zip")
#         browser.close()
