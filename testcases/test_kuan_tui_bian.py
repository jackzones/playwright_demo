# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_kuan_tui_bian import AddReportKuanTuiBian
from common.read_yaml import new_report_title_kuan_1, new_report_title_kuan_2, new_report_title_kuan_3, new_report_title_kuan_4, new_report_title_kuan_5, new_report_title_kuan_6, new_report_bi_tian_title1, new_report_title_kuan_7, new_report_title_kuan_8, new_report_title_kuan_9

@allure.feature("髋关节退变")
class TestAddReportKuanTuiBian:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportKuanTuiBian(login.navigt_jiegouhua())
            return page

    @allure.story("报告添加-印象标题-股骨-坐骨撞击综合征")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{expect}-{expect_content}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, expect, expect_content", new_report_title_kuan_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan1(self, fangshe_bianhao, buweimingcheng, leibie, treename, expect, expect_content, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_zuangji(fangshe_bianhao, buweimingcheng, leibie, treename)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info
            assert expect_content in info

    @allure.story("报告添加-印象标题-股骨-坐骨撞击综合征（左髋、右髋、双髋）")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename1}-{expect1}-{expect_content1}-{treename2}-{expect2}-{expect_content2}-{treename3}-{expect3}-{expect_content3}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename1, expect1, expect_content1, treename2, expect2, expect_content2, treename3, expect3, expect_content3", new_report_title_kuan_7)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan6(self, fangshe_bianhao, buweimingcheng, leibie, treename1, treename2, treename3, expect1, expect_content1, expect2, expect_content2, expect3, expect_content3, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_zuangji_multi1(fangshe_bianhao, buweimingcheng, leibie, treename1, treename2, treename3)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
            info_title1, info_title2, info_title3, info_title4, info_title5, info_title6 = page.impression_title1()
        with allure.step("开始断言"):
            assert expect_content1 in info
            assert expect_content2 in info
            assert expect_content3 in info
            assert '右髋' == info_title1
            assert expect1 == info_title2
            assert '左髋' == info_title3
            assert expect2 == info_title4
            assert '双髋' == info_title5
            assert expect3 == info_title6

    @pytest.mark.titles
    @allure.story("报告添加-多印象标题-上标题和小标题都有-股骨-坐骨撞击综合征（右髋、左髋、双髋）&&（右髋、左髋、双髋）髋退行性改变")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename1}-{expect1}-{expect_content1}-{treename2}-{expect2}-{expect_content2}-{treename3}-{expect3}-{expect_content3}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename1, expect1, expect_content1, treename2, expect2, expect_content2, treename3, expect3, expect_content3, treename4, suntree4, ban_suizhong4, treename5, suntree5, ban_suizhong5, treename6, suntree6, ban_suizhong6", new_report_title_kuan_8)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan6(self, fangshe_bianhao, buweimingcheng, leibie, treename1, treename2, treename3, expect1, expect_content1, expect2, expect_content2, expect3, expect_content3, treename4, suntree4, ban_suizhong4, treename5, suntree5, ban_suizhong5, treename6, suntree6, ban_suizhong6, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_zuangji_multi2(fangshe_bianhao, buweimingcheng, leibie, treename1, treename2, treename3, treename4, suntree4, ban_suizhong4, treename5, suntree5, ban_suizhong5, treename6, suntree6, ban_suizhong6)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
            info_title1, info_title2, info_title3, info_title4, info_title5, info_title6 = page.impression_title1()
        with allure.step("开始断言"):
            assert expect_content1 in info
            assert expect_content2 in info
            assert expect_content3 in info
            assert '右髋退行性改变' == info_title1
            assert expect1 == info_title2
            assert '左髋退行性改变' == info_title3
            assert expect2 == info_title4
            assert '双髋退行性改变' == info_title5
            assert expect3 == info_title6

    @allure.story("报告添加-印象标题-退行性改变-软骨软化I级和软骨下骨髓水肿")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{suntree}-{ban_suizhong}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect", new_report_title_kuan_2)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan2(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_tuixingxing_gaibian_1(fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-退行性改变-软骨软化II级和软骨下骨髓水肿")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{suntree}-{ban_suizhong}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect", new_report_title_kuan_3)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan3(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_tuixingxing_gaibian_2(fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-退行性骨关节病-软骨软化III级和软骨下骨髓水肿")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{suntree}-{ban_suizhong}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect", new_report_title_kuan_4)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan4(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_tuixingxing_gaibian_3(fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-退行性骨关节病-软骨软化IV级和软骨下骨髓水肿")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{suntree}-{ban_suizhong}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect", new_report_title_kuan_5)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan5(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_tuixingxing_gaibian_4(fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-印象标题-髋臼撞击综合征（FAI）")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{suntree}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, suntree, expect", new_report_title_kuan_6)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan5(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_tuixingxing_gaibian_5(fangshe_bianhao, buweimingcheng, leibie, treename, suntree)
        with allure.step("查看报告结果"):
            info = page.page_get_form_info_content()
        with allure.step("开始断言"):
            assert expect in info

    @allure.story("报告添加-必填规则变化")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{louzhen_text}-{yingxiangxue_biaoxian_text}-{yinxiang_text}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, louzhen_text, yingxiangxue_biaoxian_text, yinxiang_text", new_report_bi_tian_title1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_bi_tian_title1(self, fangshe_bianhao, buweimingcheng, leibie, louzhen_text, yingxiangxue_biaoxian_text, yinxiang_text, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        page.page_tijiao_report_without_bitian()
        with allure.step("查看漏诊提示"):
            info_louzhen = page.page_get_form_info_louzhen()
        with allure.step("必填确认"):
            assert louzhen_text in info_louzhen
            page.page_bi_tian_assure.click()
        with allure.step("开始断言"):
            info_yinxiang = page.page_get_form_info_content()
            info_yingxiangxue_biaoxian = page.page_get_form_info_impression_text()
            assert yinxiang_text == info_yinxiang
            page.assert_str_equal(info_yingxiangxue_biaoxian, yingxiangxue_biaoxian_text)  # 修改为使用新方法

    @allure.story("报告添加-复制功能-转义字符<和>")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{treename}-{suntree}-{ban_suizhong}-{jishu}-{expect}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, jishu, expect", new_report_title_kuan_9)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_kuan6(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, jishu, expect, login_and_navigate_to_jiegouhua):
        page = login_and_navigate_to_jiegouhua
        page.page_add_report_kuan_tuixingxing_gaibian_6(fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong, jishu)
        info = page.get_yingxiangxue_biaoxian_clipboard_text()
        with allure.step("开始断言"):
            assert expect in info
            assert "&" not in info