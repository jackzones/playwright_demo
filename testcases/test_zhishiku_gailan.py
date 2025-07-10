# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.zhishiku_gailan import ZhiShiKuGaiLanPage
from common.read_yaml import zhishiku_gailan_paixu1

@allure.feature("知识库概览")
class TestZhiShiKuGaiLan:

    @allure.title("登录并导航到知识库概览页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_zhishiku_gailan(self, login):
        with allure.step("进入知识库概览"):
            page = ZhiShiKuGaiLanPage(login.navigt_zhishiku_gailan())
            return page

    @allure.story("排序")
    @allure.title("排序成功测试-排序：全部，颈椎，胸椎，腰椎，肩，腕，髋，膝，踝")
    @pytest.mark.parametrize("card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16", zhishiku_gailan_paixu1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_zhishiku_gailan_paixu1(self, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, login_and_navigate_to_zhishiku_gailan):
        page = login_and_navigate_to_zhishiku_gailan
        with allure.step("开始断言"):
            assert card1 == page.all_card.inner_text()
            assert card2 == page.jingzui_tuibian_card.inner_text()
            assert card3 == page.jingzui_waishang_card.inner_text()
            assert card4 == page.xiongzui_waishang_card.inner_text()
            assert card5 == page.yaozui_tuibian_card.inner_text()
            assert card6 == page.yaozui_waishang_card.inner_text()
            assert card7 == page.jian_tuibian_card.inner_text()
            assert card8 == page.jian_waishang_card.inner_text()
            assert card9 == page.wan_tuibian_card.inner_text()
            assert card10 == page.wan_waishang_card.inner_text()
            assert card11 == page.kan_tuibian_card.inner_text()
            assert card12 == page.kan_gugutou_card.inner_text()
            assert card13 == page.xi_tuibian_card.inner_text()
            assert card14 == page.xi_waishang_card.inner_text()
            assert card15 == page.huai_tuibian_card.inner_text()
            assert card16 == page.huai_waishang_card.inner_text()

    @allure.story("进入知识库搜索-软骨")
    @allure.title("搜索成功测试-结果显示正确")
    # @pytest.mark.parametrize("card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16", zhishiku_gailan_paixu1)
    # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    def test_zhishiku_gailan_search1(self, login_and_navigate_to_zhishiku_gailan):
        page = login_and_navigate_to_zhishiku_gailan
        page.search_name("软骨")
        with allure.step("开始断言"):
            page.check_search_result()


