import time
from selenium.webdriver.common.by import By

from base.template_funksiya import BasePage

from base.element_xpath import ElementXPath


class SalesModal(BasePage):
    def element_visible(self, sales_modal_header_xpath):
        self.wait_for_element_visible((By.XPATH, sales_modal_header_xpath))

    def click_button(self, orders_button_xpath):
        self.wait_and_click((By.XPATH, orders_button_xpath))
