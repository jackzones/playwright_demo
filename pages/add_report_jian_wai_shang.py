from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
import time

class AddReportJianWaiShang(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guanjie_duiwei = self.page.locator('span.el-radio-button__inner:has-text("关节对位")')
        self.tree_yugong_guanjie = self.page.get_by_text("盂肱关节")
        self.data_qiantuowei = self.page.get_by_role("row", name="前脱位").locator("span").nth(1)
        self.data_houtuowei = self.page.get_by_role("row", name="后脱位").locator("span").nth(1)






    def page_menggong_guanjie_select_data(self, data):
        with allure.step("点击盂肱关节"):
            logger.info(f"点击盂肱关节")
            self.tree_yugong_guanjie.click()
            if data == "前脱位":
                self.data_qiantuowei.click()
            elif data == "后脱位":
                self.data_houtuowei.click()

    def page_guanjie_duiwei_data(self, suntree):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei.click()
            self.page_menggong_guanjie_select_data(data)
            self.check_xiazai.click()



    def page_add_report_jian_waishang_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, suntree1, tree1, data1, tree2, suntree2, data2):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(suntree1)
        self.page_guzhi_data(tree1, data1)
        self.page_jianxiu_data(tree2, suntree2, data2)
        self.page_tijiao_report()