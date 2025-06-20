
import json
import os
import platform
import pytest
from config.config import cm


def set_report_env_on_results():
    """
    在json报告的目录下生成一个写入环境信息的文件：environment.properties(注意：不能放置中文，否则会出现乱码)
    """
    # 需要写入的环境信息，根据实际工程填写
    allure_env = {
        'OperatingEnvironment': 'mcx DC',
        'PythonVersion': platform.python_version(),
        'PytestVersion': pytest.__version__,
        'Platform': platform.platform(),
        'Playwright': '0.7.0',
        'Browser': 'Google Chrome',
        'BrowserVersion': "133.0.6943.16"
    }

    allure_env_file = os.path.join(cm.dir_report_json, 'environment.properties')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        for _k, _v in allure_env.items():
            f.write(f'{_k}={_v}\n')


def set_report_executer_on_results():
    """
    在json报告的目录下生成一个写入执行人的文件：executor.json
    """
    # 需要写入的运行信息
    allure_executor = {
        "name": "徐仁杰",
        "type": "Pycharm",
        "url": "http://xx.com",  # allure报告的地址
        "buildOrder": 1,
        "buildName": "allure-report_deploy#1",
        "buildUrl": "http://xx.com#1",
        "reportUrl": "http://xx.com#1/AllureReport",
        "reportName": "徐仁杰 Allure Report"
    }
    allure_env_file = os.path.join(cm.dir_report_json, 'executor.json')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        f.write(str(json.dumps(allure_executor, ensure_ascii=False, indent=4)))


def set_report_categories_on_results():
    """
    在json报告的目录下生成一个写入统计类型的文件：categories.json
    """
    # 需要写入的运行信息
    allure_categories = [
          {
            "name": "Ignored tests",
            "matchedStatuses": ["skipped"]
          },
          {
            "name": "Infrastructure problems",
            "matchedStatuses": ["broken", "failed"],
            "messageRegex": ".*bye-bye.*"
          },
          {
            "name": "Outdated tests",
            "matchedStatuses": ["broken"],
            "traceRegex": ".*FileNotFoundException.*"
          },
          {
            "name": "Product defects",
            "matchedStatuses": ["failed"]
          },
          {
            "name": "Test defects",
            "matchedStatuses": ["broken"]
          }
        ]

    allure_cat_file = os.path.join(cm.dir_report_json, 'categories.json')
    with open(allure_cat_file, 'w', encoding='utf-8') as f:
        f.write(str(json.dumps(allure_categories, ensure_ascii=False, indent=4)))
