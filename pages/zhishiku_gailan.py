from time import sleep
import allure
from playwright.sync_api import expect
from utils.log import logger
from playwright.sync_api import Page
import re
import difflib

class ZhiShiKuGaiLanPage:
    def __init__(self, page: Page):
        self.page = page
        self.all_card = self.page.locator('div.el-col.el-col-8.is-guttered').first
        self.jingzui_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(1)
        self.jingzui_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(2)
        self.xiongzui_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(3)
        self.yaozui_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(4)
        self.yaozui_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(5)
        self.jian_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(6)
        self.jian_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(7)
        self.wan_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(8)
        self.wan_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(9)
        self.kan_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(10)
        self.kan_gugutou_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(11)
        self.xi_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(12)
        self.xi_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(13)
        self.huai_tuibian_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(14)
        self.huai_waishang_card = self.page.locator('div.el-col.el-col-8.is-guttered').nth(15)

        self.xiguanjie_btn = self.page.locator("div:nth-child(6) > div > .el-card > .el-card__body > div:nth-child(3) > .el-image__inner").first
        self.search_input = self.page.get_by_role("textbox", name="请输入位置信息")
        self.search_btn = self.page.locator("button")
        self.search_result = self.page.get_by_text("关节软骨及软骨下骨").first
        self.search_result_yinxiang = self.page.get_by_text("印象")
        self.search_result_yinxiang_text = self.page.get_by_text("正常")
        self.search_result_miaoshu = self.page.get_by_text("描述")
        self.search_result_miaoshu_text = self.page.get_by_text("软骨规则，软骨及软骨下骨髓未见异常信号")
        self.search_result_title = self.page.get_by_text("/ 膝关节退变 / 左膝 / 关节软骨及软骨下骨")

    def search_name(self, name):
        with allure.step("进入膝关节退变知识库，搜索名称为："+name+"的内容, 查看搜索结果"):
            logger.info("进入膝关节退变知识库，搜索名称为："+name+"的内容, 查看搜索结果")
            self.xiguanjie_btn.click()
            self.search_input.fill(name)
            self.search_btn.click()
            self.search_result.click()

    def check_search_result(self):
        expect(self.search_result_yinxiang).to_be_visible()
        expect(self.search_result_yinxiang_text).to_be_visible()
        expect(self.search_result_miaoshu).to_be_visible()
        expect(self.search_result_miaoshu_text).to_be_visible()
        expect(self.search_result_title).to_be_visible()
