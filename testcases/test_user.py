# !/usr/bin/python3
# -*- coding: utf-8 -*-

import allure
import pytest
from playwright.sync_api import expect
from pages.user import UserPage
from common.read_yaml import user_add1
import utils.common as cm
import random
import string
from utils.log import logger

@allure.feature("用户管理")
class TestUser:

    @allure.title("登录并导航到用户管理页面")
    @pytest.fixture(scope="function", autouse=True)
    def login_and_navigate_to_user(self, login):
        with allure.step("进入用户管理"):
            page = UserPage(login.navigt_user())
            return page

    # @allure.story("用户管理-添加用户")
    # @allure.title("成功测试")
    # @pytest.mark.parametrize("username, name, phone, email", user_add1)
    # # 多参数的参数化，这样写的话参数可以直接使用，但在parametrize与测试函数的形参中需要列出所有的参数，并且参数的顺序必须一致
    # def test_user_type1(self, username, name, phone, email, login_and_navigate_to_user):
    #     page = login_and_navigate_to_user
    #     page.add_user_without_pwd(username, name, phone, email)

    @pytest.fixture
    @allure.title("删除测试用户")
    def cleanup_users(self, login_and_navigate_to_user):
        """用于测试后清理用户的fixture"""
        page = login_and_navigate_to_user
        test_users = []  # 存储测试创建的用户名
        yield test_users  # 将控制权交给测试函数
        # 测试完成后自动清理
        with allure.step("清理测试用户"):
            for username in test_users:
                try:
                    page.delete_user(username)
                    logger.info(f"已清理用户: {username}")
                except Exception as e:
                    logger.error(f"清理用户 {username} 失败: {str(e)}")

    @allure.story("用户管理-添加随机用户")
    @allure.title("成功添加3个随机用户并记录ID")
    def test_add_random_users(self, login_and_navigate_to_user, cleanup_users):
        page = login_and_navigate_to_user

        for i in range(3):
            # 生成随机数据
            username = f"user_{''.join(random.choices(string.ascii_lowercase, k=6))}"
            name = f"测试用户_{random.randint(1000, 9999)}"
            phone = f"1{random.randint(30, 39)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
            email = f"{username}@test.com"

            # 添加用户
            page.add_user_without_pwd(username, name, phone, email)

            cleanup_users.append(username)
