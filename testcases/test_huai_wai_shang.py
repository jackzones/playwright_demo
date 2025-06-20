# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_huai_wai_shang import AddReportHuaiWaiShang
from common.read_yaml import new_report_title_huai_wai_shang_1, new_report_title_huai_wai_shang_2, new_report_title_huai_wai_shang_3, new_report_title_huai_wai_shang_4

@allure.feature("踝外伤")
class TestAddReportHuaiWaiShang:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportHuaiWaiShang(login.navigt_jiegouhua())
            return page

    @allure.story("报告添加-印象标题-副舟骨综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{tree2}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, expect", new_report_title_huai_wai_shang_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_huai_wai_shang1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_huai_waishang_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info


    @allure.story("报告添加-印象标题-距后三角骨综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{tree2}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, expect", new_report_title_huai_wai_shang_2)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_huai_wai_shang2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_huai_waishang_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @pytest.mark.titles
    @allure.story("报告添加-外伤合并退变-多印象标题-副舟骨综合征、距后三角骨综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{tree2}-{tree3}-{tree4}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4, expect", new_report_title_huai_wai_shang_3)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_huai_wai_shang3(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_huai_waishang_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-不触发-距后三角骨综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{tree2}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, expect", new_report_title_huai_wai_shang_4)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_huai_wai_shang4(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_huai_waishang_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect not in info

    # @allure.story("报告添加-印象标题-副舟骨综合征、距后三角骨综合征")
    # @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{tree2}-{tree3}-{tree4}-{expect}")
    # @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4, expect", new_report_title_huai_wai_shang_5)
    # # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    # def test_add_report_huai_wai_shang5(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4, expect, login_and_navigate_to_jiegouhua):
    #     page = login_and_navigate_to_jiegouhua
    #     page.page_add_report_huai_waishang_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4)
    #     with allure.step("查看报告结果"):
    #         info = page.page_get_form_info_content()
    #     with allure.step("开始断言"):
    #         assert expect in info