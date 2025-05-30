
import difflib
from playwright.sync_api import Page
import os
from pathlib import Path
import csv
from pathlib import Path
import allure
import json


def assert_strings_equal(self, actual, expected):
    """比较两个字符串并高亮显示差异"""
    if actual != expected:
        diff = difflib.ndiff(expected.splitlines(keepends=True),
                             actual.splitlines(keepends=True))
        diff_text = ''.join(diff)
        logger.error(f"字符串不匹配，差异如下:\n{diff_text}")
        assert False, f"字符串不匹配，差异如下:\n{diff_text}"
    return True


