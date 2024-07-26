from pages.login_page import LoginPage
from pages.dashboart_page import DashboardPage
from base.element_xpath import ElementXPath
from utils.driver_setup import driver


def test_all(driver):
    email = "admin@test"
    password = 'greenwhite'

    login_page = LoginPage(driver)
    login_page.fill_form(email, password, ElementXPath.login_xpath, ElementXPath.password_xpath)
    login_page.click_button(ElementXPath.signup_xpath)

    dashboard_page = DashboardPage(driver)
    dashboard_page.element_visible(ElementXPath.dashboard_header_xpath)
    dashboard_page.click_button(ElementXPath.sales_button_xpath)

    sales_modal =
