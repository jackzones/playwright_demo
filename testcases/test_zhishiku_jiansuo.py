# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.zhishiku_jiansuo import ZhiShiKuJianSuoPage
from common.read_yaml import zhishiku_jiansuo_type1, zhishiku_jiansuo_search1
import utils.common as cm

@allure.feature("知识库检索")
class TestZhiShiKuJianSuo:

    @allure.title("登录并导航到知识库检索页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_zhishiku_jiansuo(self, login):
        with allure.step("进入知识库检索"):
            page = ZhiShiKuJianSuoPage(login.navigt_zhishiku_jiansuo())
            return page

    @allure.story("知识库检索-设备类型")
    @allure.title("成功测试-{type}-{num}")
    @pytest.mark.parametrize("type, num", zhishiku_jiansuo_type1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_zhishiku_jiansuo_type1(self, type, num, login_and_navigate_to_zhishiku_jiansuo):
        page = login_and_navigate_to_zhishiku_jiansuo
        page.select_device_type(type)
        with allure.step("开始断言"):
            assert num == cm.extract_num_from_str(page.search_counts_text())


    @allure.story("知识库检索-搜索印象和描述")
    @allure.title("搜索成功测试-高亮显示结果-{text}-{num}")
    @pytest.mark.parametrize("text, num", zhishiku_jiansuo_search1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_zhishiku_jiansuo_search1(self, text, num, login_and_navigate_to_zhishiku_jiansuo):
        page = login_and_navigate_to_zhishiku_jiansuo
        page.select_device_type('MRI', text)
        with allure.step("开始断言"):
            assert cm.extract_num_from_str(page.search_counts_text()) >= num
            assert page.highlight_counts(text) >= 6

    @allure.story("知识库检索-删除搜索条件")
    @allure.title("成功测试-保持本页")
    # @pytest.mark.parametrize("text, num")
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_zhishiku_jiansuo_search2(self, login_and_navigate_to_zhishiku_jiansuo):
        page = login_and_navigate_to_zhishiku_jiansuo
        page.select_device_type('MRI', '软骨软化')
        page.input_clear()
        with allure.step("开始断言"):
            assert page.search_page_load.is_visible()