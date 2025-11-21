#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest
from urllib.parse import urlparse
import allure
import pytest
from utils.log import logger
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
import os
from utils.log import get_project_root
import time
import threading
from config.config import cm
import datetime  # 添加datetime模块用于时间戳


def extract_domain(url_string):
    parsed_url = urlparse(url_string)
    return parsed_url.netloc


@pytest.fixture(scope="session")
def page(pytestconfig):
    with sync_playwright() as p:
        logger.info("page session fixture starting....")
        browser = p.chromium.launch(headless=True, timeout=5000)
        context = browser.new_context(viewport={"width": 1920, "height": 1080}, record_video_dir="videos/",ignore_https_errors=True)
        page = context.new_page()
        # 设置默认超时时间为4秒（3000毫秒）
        page.set_default_timeout(3000)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield page
        logger.info("page session fixture closing.......")
        base_url = pytestconfig.getoption("base_url") or "http://192.168.1.104:9104"
        domain = extract_domain(base_url).replace(".", "_")
        logger.info("stop tracing...")
        context.tracing.stop(path=f"{domain}_trace.zip")
        browser.close()


@pytest.fixture(scope="session")
def auth_page():
    with sync_playwright() as p:
        logger.info("page session fixture starting....")
        browser = p.chromium.launch(headless=True, timeout=10_000)
        logger.info("使用auth.json文件恢复登录状态")
        base_path = os.path.dirname(os.path.realpath(__file__))
        context = browser.new_context(
            storage_state=os.path.join(base_path, "auth.json"),
            viewport={"width": 1920, "height": 1080},
            record_video_dir = "videos/",
            ignore_https_errors=True
        )
        page = context.new_page()
        # 设置默认超时时间为4秒（3000毫秒）
        page.set_default_timeout(3000)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield page
        logger.info("page session fixture closing.......")
        context.tracing.stop(path="trace.zip")
        browser.close()


def _login(page, pytestconfig, is_goto_project_detail=False):
    if base_url := pytestconfig.getoption("base_url"):
        logger.info(f"命令行传入参数，base_url={base_url}")
    else:
        default_url = "http://192.168.1.104:9104"
        logger.warning(f"没有传入base-url，会使用默认base_url = {default_url}，如果需要使用--base-url=xxx修改")
        base_url = default_url

    login_page = LoginPage(page, base_url=base_url)

    login_page.login("xurj", "User123456")
    if is_goto_project_detail:
        logger.info("登录并进入项目详情")
        login_page.navigt_jiegouhua()
    return login_page


# 创建一个 pytest fixture 实现登录操作，并设置为session级别，实现共享登录状态
@pytest.fixture(scope="function")
def login(page, pytestconfig):
    logger.info("登录操作#############")
    yield _login(page, pytestconfig)

#截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # 设置报告属性（重要，其他fixture会用到）
    setattr(item, "rep_" + rep.when, rep)

    # 只在测试执行阶段处理
    if rep.when == 'call':
        # 使用时间戳作为截图文件名
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        screenshot_name = f"screenshot_{timestamp}"
        screenshot_path = f"screenshots/{screenshot_name}.png"

        # 确保截图目录存在
        os.makedirs("screenshots", exist_ok=True)

        # 尝试获取page对象
        page = None
        try:
            # 从测试上下文中获取page对象
            if "page" in item.funcargs:
                page = item.funcargs["page"]
            elif "auth_page" in item.funcargs:
                page = item.funcargs["auth_page"]
        except Exception as e:
            logger.error(f"获取page对象失败: {str(e)}")

        # 如果有page对象则截图
        if page:
            try:
                # 添加短暂等待确保页面稳定
                time.sleep(0.05)
                # 截取截图
                screenshot = page.screenshot(full_page=True, path=screenshot_path)

                # 附加到Allure报告
                allure.attach(
                    screenshot,
                    name=screenshot_name,
                    attachment_type=allure.attachment_type.PNG
                )
                logger.info(f"已附加截图: {screenshot_name}")

            except Exception as e:
                logger.error(f"截图失败: {str(e)}")
            # logger.warning("未找到page对象，无法截图")

#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--host",
#         action="store",
#         default="http://192.168.1.104:9104",
#         help="base URL for login page",
#     )
#     logger.info("添加命令行参数 host")
#     # parser.addoption("--base-url", action="store", default="http://119.91.147.215", help="base URL for login page")