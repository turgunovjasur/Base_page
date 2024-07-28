import time

from selenium.webdriver.common.by import By

from base.template_funksiya import BasePage

from base.element_xpath import ElementXPath


class OrdersPage(BasePage):
    def element_visible(self, order_page_header_xpath):
        self.wait_for_element_visible((By.XPATH, order_page_header_xpath))

    def click_button(self, create_button_xpath):
        time.sleep(5)
        self.wait_and_click((By.XPATH, create_button_xpath))
