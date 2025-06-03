# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.add_report_kuan_gugutou_huaisi import AddReportKuanGuGuTouHuaiSi
from common.read_yaml import new_report_bi_tian_title2

@allure.feature("髋股骨头坏死")
class TestAddReportKuanGuGuTouHuaiSi:

    @allure.title("登录并导航到结构化报告页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_jiegouhua(self, login):
        with allure.step("进入结构化报告"):
            page = AddReportKuanGuGuTouHuaiSi(login.navigt_jiegouhua())
            return page

    @allure.story("报告添加-必填规则变化")
    @allure.title("添加成功测试-{fangshe_bianhao}-{buweimingcheng}-{leibie}-{louzhen_text}-{yingxiangxue_biaoxian_text}-{yinxiang_text}")
    @pytest.mark.parametrize("fangshe_bianhao, buweimingcheng, leibie, louzhen_text, yingxiangxue_biaoxian_text, yinxiang_text", new_report_bi_tian_title2)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_add_report_bi_tian_title2(self, fangshe_bianhao, buweimingcheng, leibie, louzhen_text, yingxiangxue_biaoxian_text, yinxiang_text, login_and_navigate_to_jiegouhua):
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
            page.assert_str_equal(info_yingxiangxue_biaoxian, yingxiangxue_biaoxian_text)
            assert yinxiang_text == info_yinxiang