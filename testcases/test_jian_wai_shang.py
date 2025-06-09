# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_jian_wai_shang import AddReportJianWaiShang
from common.read_yaml import new_report_title_jian_wai_shang_1

@allure.feature("肩关节外伤")
class TestAddReportJianWaiShang:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportJianWaiShang(login.navigt_jiegouhua())
            return page

    @pytest.mark.debug
    @allure.story("报告添加-印象标题-左/右肩关节Bankart-Hill-Sachs损伤")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{data1}-{tree2}-{suntree2}-{data2}-{tree3}-{suntree3}-{data3}-{tree4}-{data4}-{tree5}-{data5}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, expect", new_report_title_jian_wai_shang_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian_wai_shang1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_jian_waishang_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info