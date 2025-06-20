# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_jian_wai_shang import AddReportJianWaiShang
from common.read_yaml import new_report_title_jian_wai_shang_1, new_report_title_jian_wai_shang_2, new_report_title_jian_wai_shang_3, new_report_title_jian_wai_shang_4, new_report_title_jian_waishang_hebing_tuibian_1

@allure.feature("肩关节外伤")
class TestAddReportJianWaiShang:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportJianWaiShang(login.navigt_jiegouhua())
            return page

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

    @allure.story("报告添加-印象标题-左/右肩关节反Bankart-反Hill-Sachs损伤")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{data1}-{tree2}-{suntree2}-{data2}-{tree3}-{suntree3}-{data3}-{tree4}-{data4}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, expect", new_report_title_jian_wai_shang_2)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian_wai_shang2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_jian_waishang_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-不触发-左/右肩关节反Bankart-反Hill-Sachs损伤")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{data1}-{tree2}-{suntree2}-{data2}-{tree3}-{suntree3}-{data3}-{tree4}-{data4}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, expect", new_report_title_jian_wai_shang_4)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian_wai_shang4(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_jian_waishang_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect not in info

    @pytest.mark.titles
    @allure.story("报告添加-多印象标题-左/右肩关节Bankart-Hill-Sachs损伤、左/右肩关节反Bankart-反Hill-Sachs损伤")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{data1}-{tree2}-{suntree2}-{data2}-{tree3}-{suntree3}-{data3}-{tree4}-{data4}-{tree5}-{data5}-{data6}-{tree7}-{suntree7}-{data7}-{tree8}-{suntree8}-{data8}-{tree9}-{data9}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, data6, tree7, suntree7, data7, tree8, suntree8, data8, tree9, data9, expect", new_report_title_jian_wai_shang_3)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian_wai_shang3(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, data6, tree7, suntree7, data7, tree8, suntree8, data8, tree9, data9, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_jian_waishang_title3(fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, data6, tree7, suntree7, data7, tree8, suntree8, data8, tree9, data9)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @pytest.mark.titles
    @allure.story("报告添加-外伤合并退变-多印象标题-肩关节反Bankart-反Hill-Sachs损伤、肩峰下撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{expect1}-{expect2}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, suntree5, tree6, data6, tree7, suntree7, data7, expect1, expect2", new_report_title_jian_waishang_hebing_tuibian_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian_wai_shang5(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, suntree5, tree6, data6, tree7, suntree7, data7, expect1, expect2, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_jian_waishanghebing_tuibian_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, suntree5, tree6, data6, tree7, suntree7, data7)
        with allure.step("查看报告结果"):
            first_title = page.page_get_form_info_rule_title_top()
            second_title = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect1 == first_title
            assert expect2 == second_title
            # assert expect_btm1 in info_btm