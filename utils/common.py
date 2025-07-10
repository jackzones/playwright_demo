
import difflib
from playwright.sync_api import Page
import os
from pathlib import Path
import csv
from pathlib import Path
import allure
import json
import re


def assert_strings_equal(self, actual, expected):
    """比较两个字符串并高亮显示差异"""
    if actual != expected:
        diff = difflib.ndiff(expected.splitlines(keepends=True),
                             actual.splitlines(keepends=True))
        diff_text = ''.join(diff)
        logger.error(f"字符串不匹配，差异如下:\n{diff_text}")
        assert False, f"字符串不匹配，差异如下:\n{diff_text}"
    return True


def extract_num_from_str(text: str) -> int:
    """从类似'共 5191 条'的字符串中提取数字部分
    Args:
        text: 包含数字的字符串，如'共 5191 条'

    Returns:
        提取出的数字，如5191
    """
    print(text)
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    return 0