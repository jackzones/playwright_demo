from time import sleep
import allure
from playwright.sync_api import expect
from utils.log import logger
from playwright.sync_api import Page
import re
import difflib

class TujiLieBiaoPage:
    def __init__(self, page: Page):
        self.page = page

        self.fenye = page.locator("div").filter(has_text=re.compile(r"^10条/页$")).nth(1)
        self.fenye_100 = page.get_by_role("option", name="100条/页")
        self.jiazai_shibai = page.get_by_text("加载失败")

        # page.get_by_role("button", name="73").click()



    def select_100_fenye(self):
        with allure.step("选择100条/页"):
            logger.info("选择100条/页")
            self.fenye.click()
            sleep(0.2)
            self.fenye_100.click()

    def view_data_num(self, num):
        self.page.get_by_role("button", name=num, exact=True).click()

    def jiazai_shibai_counts(self):
        sleep(0.5)
        count = self.jiazai_shibai.count()
        return count