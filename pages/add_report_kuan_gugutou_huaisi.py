from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
import time

class AddReportKuanGuGuTouHuaiSi(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
