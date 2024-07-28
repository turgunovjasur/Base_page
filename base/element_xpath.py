from base.template_funksiya import BasePage


class ElementXPath:

    # Login_page
    login_xpath = "//div/input[@placeholder='Логин@компания']"
    password_xpath = "//div/input[@placeholder='Пароль']"
    signup_xpath = "//div/button[contains(text(), 'Войти')]"

    # Dashboard_page
    dashboard_header_xpath = "//div/h3[contains(text(), 'Trade')]"
    sales_button_xpath = "//li/a/span[contains(text(), 'Продажа')]"

    # Sales_modal
    sales_modal_header_xpath = "//h3/span[contains(text(), 'Продажа')]"
    orders_button_xpath = "//a/span[contains(text(), 'Заказы')]"

    # Order_page
    order_page_header_xpath = "//ul/li/a[contains(text(), 'Опросники')]"
    create_button_xpath = "//div/button[contains(text(), 'Создать')]"

    # Create_order_page
    create_order_header_xpath = "//div/h3/t[contains(text(), 'Основное')]"

    order_request_xpath = "(//div/input[@placeholder = 'Поиск...'])[1]"
    room_xpath = "(//div/input[@placeholder='Поиск...'])[1]"
    robot_xpath = "(//div/input[@placeholder='Поиск...'])[2]"
    client_xpath = "(//div/input[@placeholder='Поиск...'])[3]"

    next_button_xpath = "//span/t[contains(text(), 'Далее')]"





