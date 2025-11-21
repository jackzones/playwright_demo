# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.tuji_liebiao import TujiLieBiaoPage
from common.read_yaml import tuji_liebiao_1

@allure.feature("图集列表")
class TestTujiLieBiao:

    @allure.title("登录并导航到图集列表页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_tuji_liebiao(self, login):
        with allure.step("进入图集列表"):
            page = TujiLieBiaoPage(login.navigt_tuji_liebiao())
            return page

    @allure.story("验证图集中图片无加载失败情况")
    @allure.title("验证图集中图片无加载失败情况")
    @pytest.mark.parametrize("data, data2", tuji_liebiao_1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_tuji_liebiao_yanzheng1(self, data, data2, login_and_navigate_to_tuji_liebiao):
        page = login_and_navigate_to_tuji_liebiao
        page.select_100_fenye()
        page.view_data_num(data)
        with allure.step("开始断言:无加载失败"):
            assert page.jiazai_shibai_counts() == 0



