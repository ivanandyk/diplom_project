import psycopg2
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.group_page import GroupPage
from steps.db_group_creation import new_group


group = "Main Group"
connection = psycopg2.connect(
    host="localhost", user="postgres",
    password="postgres", dbname="postgres")


def test_1(driver):

    new_group(connection, group)
    base_page = BasePage(driver)
    base_page.open_base_page()
    main_page = MainPage(driver)
    main_page.check_main_page()
    main_page.open_admin_page()
    login_page = LoginPage(driver)
    login_page.check_login()
    login_page.login_steps()
    admin_page = AdminPage(driver)
    admin_page.check_admin_page()
    admin_page.open_group_page()
    group_page = GroupPage(driver)
    group_page.check_result(group)
    connection.close()
