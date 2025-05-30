# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_xi_tui_bian import AddReportXiTuiBian
from common.read_yaml import new_report_title_4_1

@allure.feature("膝关节退变")
class TestAddReportXiTuiBian:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportXiTuiBian(login.navigt_jiegouhua())
            return page

    @allure.story("报告添加-印象标题-左/右膝退行性骨关节病-软骨软化III级-多项类别")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{treename}-{expect}-{expect_content}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, treename, expect, expect_content", new_report_title_4_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_ruangu_2ji(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, treename, expect, expect_content, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_ruangu_3ji_multi(fangshe_bianhao, buweimingcheng, leibie, xibuwei, treename)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info
            assert expect_content in info

    @allure.story("确认进入页面")
    @allure.title("添加成功测试2-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei", [("11111111", "膝", "退变", "左膝")])
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_ruangu_3ji(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        with allure.step("开始断言"):
            expect(page.tab_banyueban).to_be_visible()