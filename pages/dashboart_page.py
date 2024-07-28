from selenium.webdriver.common.by import By

from base.template_funksiya import BasePage

from base.element_xpath import ElementXPath


class DashboardPage(BasePage):
    def element_visible(self, dashboard_header_xpath):
        self.wait_for_element_visible((By.XPATH, dashboard_header_xpath))

    def click_button(self, sales_button_xpath):
        self.wait_and_click((By.XPATH, sales_button_xpath))

