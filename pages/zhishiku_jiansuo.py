from time import sleep
import allure
from playwright.sync_api import expect
from utils.log import logger
from playwright.sync_api import Page
import re
import difflib

class ZhiShiKuJianSuoPage:
    def __init__(self, page: Page):
        self.page = page

        self.device_type_list = self.page.get_by_role("main").get_by_role("img").nth(1)
        self.search_btn = self.page.get_by_role("button", name="搜索")
        self.search_input = self.page.locator("input.el-input__inner").first
        self.search_page_load = self.page.get_by_role("link", name="检索详情")
        self.search_counts = self.page.locator("span.el-pagination__total")
        self.ruangu_ruanhua_highlight = self.page.locator('span[style="color:var(--el-color-primary)"]', has_text='软骨软化')
        self.duanduan_fenli_highlight = self.page.locator('span[style="color:var(--el-color-primary)"]', has_text='断端分离')

    def select_device_type(self, device_type, text=None):
        with allure.step(f"选择设备类型: {device_type}, 输入搜索内容: {text}，点击搜索按钮"):
            logger.info(f"选择设备类型: {device_type}, 输入搜索内容: {text}，点击搜索按钮")
            self.device_type_list.click()
            if device_type == "CT":
                self.page.get_by_role("option", name="CT").click()
            elif device_type == "MRI":
                self.page.get_by_role("option", name="MRI").click()
            elif device_type == "DR":
                self.page.get_by_role("option", name="DR").click()
            else:
                logger.error(f"不支持的设备类型: {device_type}")
            if text:
                self.search_input.fill(text)
            self.search_btn.click()

    def search_counts_text(self):
        self.search_page_load.wait_for(state="visible")
        sleep(0.3)
        return self.search_counts.inner_text()

    def highlight_counts(self, text):
        with allure.step(f"检查高亮显示的数量: {text}"):
            logger.info(f"检查高亮显示的数量: {text}")
            if text == '软骨软化':
                return self.ruangu_ruanhua_highlight.count()
            elif text == '断端分离':
                return self.duanduan_fenli_highlight.count()
            else:
                logger.error(f"不支持的字段: {text}")

    def input_clear(self):
        with allure.step("清空搜索框"):
            logger.info(f"清空搜索框")
            self.search_input.clear()

    # def check_search_result(self):
    #     expect(self.search_result_yinxiang).to_be_visible()
    #     expect(self.search_result_yinxiang_text).to_be_visible()
    #     expect(self.search_result_miaoshu).to_be_visible()
    #     expect(self.search_result_miaoshu_text).to_be_visible()
    #     expect(self.search_result_title).to_be_visible()
