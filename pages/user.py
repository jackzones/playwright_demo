from time import sleep
import allure
from playwright.sync_api import expect
from utils.log import logger
from playwright.sync_api import Page
import re
import difflib

class UserPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_user_btn = self.page.get_by_role("button", name="新增用户")
        self.username_input = self.page.get_by_role("textbox", name="*账号")
        self.name_input = self.page.get_by_role("textbox", name="*用户姓名")
        self.phone_input = self.page.get_by_role("textbox", name="*手机号")
        self.email_input = self.page.get_by_role("textbox", name="*邮箱地址")
        self.save_btn = self.page.get_by_role("button", name="保存").nth(1)

        self.sure_btn = self.page.get_by_role("button", name="确定")


    def add_user_without_pwd(self, username, name, phone, email):
        with allure.step(f"添加用户-{username}"):
            logger.info(f"添加用户-{username}")
            self.add_user_btn.click()
            self.username_input.fill(username)
            self.name_input.fill(name)
            self.phone_input.fill(phone)
            self.email_input.fill(email)
            self.save_btn.click()

    def delete_user(self, username):
        with allure.step(f"删除用户-{username}"):
            logger.info(f"删除用户-{username}")
            self.page.get_by_role("row", name=username).get_by_role("button").nth(3).click()
            self.sure_btn.click()
            sleep(0.5)

