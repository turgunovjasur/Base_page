from base.template_funksiya import BasePage


class ElementXPath:

    # Login_page
    login_xpath = "//div/input[@placeholder='Логин@компания']"
    password_xpath = "//div/input[@placeholder='Пароль']"
    signup_xpath = "//div/button[contains(text(), 'Войти')]"

    # Dashboard_page
    dashboard_header_xpath = "//div/h3[contains(text(), 'Trade')]"
    sales_button_xpath = "//li/a/span[contains(text(), 'Продажа')]"

    # Sales modal
    sales_modal_header_xpath = "//h3/span[contains(text(), 'Продажа')]"
    orders_button_xpath = "//a/span[contains(text(), 'Заказы')]"
