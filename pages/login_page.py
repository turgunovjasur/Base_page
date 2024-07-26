from selenium.webdriver.common.by import By

from base.template_funksiya import BasePage

from base.element_xpath import ElementXPath


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_form(self, email, password, login_xpath, password_xpath):
        self.input_text((By.XPATH, login_xpath), email)
        self.input_text((By.XPATH, password_xpath), password)

    def click_button(self, signup_xpath):
        self.click((By.XPATH, signup_xpath))
