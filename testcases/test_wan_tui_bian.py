# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_wan_tui_bian import AddReportWanTuiBian
from common.read_yaml import new_report_title_wan_tuibian_1, new_report_title_wan_tuibian_2, new_report_title_wan_tuibian_3, new_report_title_wan_tuibian_4, new_report_title_wan_tuibian_5, new_report_title_wan_tuibian_6, new_report_title_wan_tuibian_7, new_report_title_wan_tuibian_8, new_report_title_wan_tuibian_9, new_report_title_wan_tuibian_10

@allure.feature("腕关节退变")
class TestAddReportWanTuiBian:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportWanTuiBian(login.navigt_jiegouhua())
            return page

    @allure.story("报告添加-印象标题-左/右腕尺骨撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, expect", new_report_title_wan_tuibian_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-左/右腕尺骨撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, expect", new_report_title_wan_tuibian_2)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-在下方-腕尺侧撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, expect", new_report_title_wan_tuibian_3)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian3(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title1(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect == info

    @allure.story("报告添加-印象标题-在下方-腕尺侧撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, expect", new_report_title_wan_tuibian_4)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian4(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect == info

    @allure.story("报告添加-印象标题-在下方-尺骨茎突撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, expect", new_report_title_wan_tuibian_5)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian5(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title2(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect == info

    @allure.story("报告添加-印象标题-在下方-尺骨茎突撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{tree4}-{data4}-{tree5}-{data5}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, expect", new_report_title_wan_tuibian_6)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian6(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title3(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect == info

    @allure.story("报告添加-印象标题-在下方-钩月撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, expect", new_report_title_wan_tuibian_7)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian7(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title4(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect == info

    @allure.story("报告添加-印象标题-在下方-钩月撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{tree4}-{data4}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, expect", new_report_title_wan_tuibian_8)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian8(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title5(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect == info

    @pytest.mark.titles
    @allure.story("报告添加-多印象标题-尺骨撞击综合征（上标题）-尺骨茎突、钩月、尺侧撞击综合征（下标题）")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{tree4}-{data4}-{tree5}-{data5}-{tree6}-{data6}-{expect_top}-{expect_btm1}-{expect_btm2}-{expect_btm3}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6, expect_top, expect_btm1, expect_btm2, expect_btm3", new_report_title_wan_tuibian_9)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian9(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6, expect_top, expect_btm1, expect_btm2, expect_btm3, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title6(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
            info_btm = page.page_get_form_info_rule_title_bottom()
        with allure.step("开始断言"):
            assert expect_top in info
            assert expect_btm1 in info_btm
            assert expect_btm2 in info_btm
            assert expect_btm3 in info_btm

    @pytest.mark.titles
    @allure.story("报告添加-外伤合并退变-多印象标题-尺骨撞击综合征（上标题）-尺骨茎突、钩月、尺侧撞击综合征（下标题）")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{xibuwei}-{tree1}-{data1}-{tree2}-{data2}-{tree3}-{data3}-{tree4}-{data4}-{tree5}-{data5}-{tree6}-{data6}-{expect_top}-{expect_btm1}-{expect_btm2}-{expect_btm3}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6, expect_top, expect_btm1, expect_btm2, expect_btm3", new_report_title_wan_tuibian_10)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_jian10(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6, expect_top, expect_btm1, expect_btm2, expect_btm3, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_wan_tuibian_title7(fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6)
        # with allure.step("查看报告结果"):
        #     first_title = page.page_get_form_info_rule_title_top()
        #     second_title = page.page_get_form_info_rule_title_bottom()
        #     # info_btm = page.page_get_form_info_rule_title_third()
        #     info = page.page_get_form_info_content()
        # with allure.step("开始断言"):
        #     # assert xibuwei == first_title
        #     assert expect_top == first_title
        #     assert expect_btm1 in second_title
        #     assert expect_btm2 in second_title
        #     assert expect_btm3 in second_title
        #     assert '未见明显骨折征象，必要时CT检查明确细微骨质情况' not in info

        with allure.step("查看报告结果"):
            first_title = page.page_get_form_info_rule_title_top()
            second_title = page.page_get_form_info_rule_title_bottom()
            info_btm = page.page_get_form_info_rule_title_third()
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert xibuwei == first_title
            assert expect_top == second_title
            assert expect_btm1 in info_btm
            assert expect_btm2 in info_btm
            assert expect_btm3 in info_btm
            assert '未见明显骨折征象，必要时CT检查明确细微骨质情况'  in info