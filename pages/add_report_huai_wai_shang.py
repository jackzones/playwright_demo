from time import sleep

from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
import time

class AddReportHuaiWaiShang(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guzhi_gusui_suizhong = self.page.locator('span.el-radio-button__inner:has-text("骨质（骨髓水肿）")')
        # self.tab_guanjie_ruangu = self.page.locator(".innerTag").get_by_text("关节软骨及软骨下骨")
        #骨质（骨髓水肿）
        self.tree_gusui_suizhong_zhougu = self.page.get_by_text("舟骨", exact=True)
        self.tree_gusui_suizhong_juhou_sanjiaogu = self.page.get_by_text("距后三角骨")
        self.tree_gusui_suizhong_fuzhougu = self.page.get_by_text("副舟骨")
        self.tree_gusui_suizhong_jugu = self.page.get_by_text("距骨", exact=True)

        self.gusui_suizhong_checkbox = self.page.get_by_role("row", name="骨髓水肿").locator("span").nth(1)  # 第一行"骨髓水肿"选项

        #标题选择
        self.title_fuzhougu = self.page.get_by_title("副舟骨综合征").locator("span").nth(1)
        self.title_juhou_sanjiaogu = self.page.get_by_title("距后三角骨综合征").locator("span").nth(1)


    # 骨质（骨髓水肿），距后三角骨，骨髓水肿
    def page_gusui_suizhong_select_broken(self, tree):
        if tree == "舟骨":
            with allure.step("点击舟骨-勾选骨髓水肿"):
                logger.info(f"点击舟骨-勾选骨髓水肿")
                self.tree_gusui_suizhong_zhougu.click()
                sleep(0.1)
                self.gusui_suizhong_checkbox.click()
        elif tree == "副舟骨":
            with allure.step("点击副舟骨-勾选骨髓水肿"):
                logger.info(f"点击副舟骨-勾选骨髓水肿")
                self.tree_gusui_suizhong_fuzhougu.click()
                sleep(0.1)
                self.gusui_suizhong_checkbox.click()
        elif tree == "距骨":
            with allure.step("点击距骨-勾选骨髓水肿"):
                logger.info(f"点击距骨-勾选骨髓水肿")
                self.tree_gusui_suizhong_jugu.click()
                sleep(0.1)
                self.gusui_suizhong_checkbox.click()
        elif tree == "距后三角骨":
            with allure.step("点击距后三角骨-勾选骨髓水肿"):
                logger.info(f"点击距后三角骨-勾选骨髓水肿")
                self.tree_gusui_suizhong_juhou_sanjiaogu.click()
                sleep(0.1)
                self.gusui_suizhong_checkbox.click()
        else:
            logger.error(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    def page_guzhi_gusui_suizhong_data(self, tree):
        with allure.step("点击骨质（骨髓水肿）"):
            logger.info(f"点击骨质（骨髓水肿）")
            self.tab_guzhi_gusui_suizhong.click()
            self.page_gusui_suizhong_select_broken(tree)


    def page_select_title1(self):
        with allure.step("勾选标题：副舟骨综合征、距后三角骨综合征"):
            logger.info(f"勾选标题：副舟骨综合征、距后三角骨综合征")
            self.title_fuzhougu.click()
            self.title_juhou_sanjiaogu.click()
            self.title_ok_btn.click()

    def page_add_report_huai_waishang_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guzhi_gusui_suizhong_data(tree1)
        self.page_guzhi_gusui_suizhong_data(tree2)
        self.page_tijiao_report()

    def page_add_report_huai_waishang_title2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, tree2, tree3, tree4):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guzhi_gusui_suizhong_data(tree1)
        self.page_guzhi_gusui_suizhong_data(tree2)
        self.page_guzhi_gusui_suizhong_data(tree3)
        self.page_guzhi_gusui_suizhong_data(tree4)
        self.page_tijiao_report()
        self.page_select_title1()
