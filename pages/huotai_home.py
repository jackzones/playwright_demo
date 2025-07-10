from time import sleep
import allure
from playwright.sync_api import expect
from utils.log import logger
from playwright.sync_api import Page
import re
import difflib

class HouTaiHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.zhishiku_gailan_menu = self.page.get_by_role("link", name="知识库概览")
        self.zhishiku_jiansuo_menu = self.page.get_by_role("link", name="知识库检索")

        self.shuju_guanli_menu = self.page.get_by_role("menuitem", name="数据管理").locator("div")
        self.report_history_menu = self.page.get_by_role("link", name="报告历史数据")

        self.xitong_guanli_menu = self.page.get_by_role("menuitem", name="系统管理").locator("div")
        self.user_menu = self.page.get_by_role("link", name="用户管理")
        self.role_menu = self.page.get_by_role("link", name="角色管理")

    @allure.step("切换知识库概览页")
    def navigt_zhishiku_gailan(self):
        logger.info("切换知识库概览页")
        self.zhishiku_gailan_menu.click()
        return self.page