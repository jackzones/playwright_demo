# !/usr/bin/python3
# -*- coding: utf-8 -*-

# @Author: 花菜
# @File: login_page.py.py
# @Time : 2024/1/13 00:16
# @Email: lihuacai168@gmail.com

import allure
from utils.log import logger
from playwright.sync_api import Page
from time import sleep


class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        self.username_input = self.page.get_by_role("textbox", name="* 账号")
        self.password_input = self.page.get_by_role("textbox", name="* 密码")
        self.submit_button = self.page.get_by_role("button", name="登录")

        #后台管理，标签页
        self.zhishiku_gailan_menu = self.page.get_by_role("menubar").get_by_role("link", name="知识库概览")
        self.zhishiku_jiansuo_menu = self.page.get_by_role("link", name="知识库检索")

        self.shuju_guanli_menu = self.page.get_by_role("menuitem", name="数据管理").locator("div")
        self.report_history_menu = self.page.get_by_role("link", name="报告历史数据")

        self.xitong_guanli_menu = self.page.get_by_role("menuitem", name="系统管理").locator("div")
        self.user_menu = self.page.get_by_role("link", name="用户管理")
        self.role_menu = self.page.get_by_role("link", name="角色管理")


    # 定义操作
    @allure.step("打开登录页面，填写账号密码")
    def login(self, username: str, password: str):
        logger.info(f"打开登录页面: {self.base_url + '/login'}，填写账号密码")
        # self.page.goto(self.base_url + "/login")
        self.page.goto(self.base_url + "/login", timeout=10_000, wait_until="networkidle")
        self.username_input.fill(username)
        self.password_input.fill(password)
        logger.info("点击登录按钮")
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle", timeout=5_000)
        logger.info("登录成功")

    @allure.step("切换结构化报告页")
    def navigt_jiegouhua(self):
        logger.info("切换结构化报告页")
        self.page.get_by_role("button", name="结构化报告").click()
        return self.page


    @allure.step("切换后台管理页")
    def navigt_houtai(self):
        logger.info("切换后台管理页")
        self.page.get_by_text("后台管理").click()
        return self.page

    @allure.step("切换知识库概览页")
    def navigt_zhishiku_gailan(self):
        logger.info("切换知识库概览页")
        self.page.get_by_text("后台管理").click()
        sleep(0.5)
        self.zhishiku_gailan_menu.click()
        return self.page

    @allure.step("切换知识库检索页")
    def navigt_zhishiku_jiansuo(self):
        logger.info("切换知识库检索页")
        self.page.get_by_text("后台管理").click()
        sleep(0.5)
        self.zhishiku_jiansuo_menu.click()
        return self.page

    @allure.step("切换用户管理页")
    def navigt_user(self):
        logger.info("切换用户管理页")
        self.page.get_by_text("后台管理").click()
        sleep(0.5)
        self.xitong_guanli_menu.click()
        self.user_menu.click()
        return self.page

