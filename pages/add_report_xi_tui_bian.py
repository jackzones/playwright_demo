from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure

class AddReportXiTuiBian(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guanjie_ruangu = self.page.locator(".innerTag").get_by_text("关节软骨及软骨下骨")
        self.tab_banyueban = self.page.locator(".innerTag").get_by_text("半月板")
        self.zuoce_tab_xituibian = self.page.get_by_text("左 膝关节退变")
        self.tree_binggu_guanjie_multi = self.page.get_by_role("treeitem", name="髌股关节")
        self.tree_guanjie_ruangu_3ji = self.page.get_by_role("row", name="软骨软化III级 软骨不规则变薄，缺损范围>50").locator("span").nth(1)



    def page_click_ruangu_3ji_multi(self, tree):
        with allure.step("勾选软骨软化III级"):
            self.tab_guanjie_ruangu.click()
            if tree == '髌股关节':
                self.tree_binggu_guanjie_multi.click()
                self.tree_guanjie_ruangu_3ji.click()
            # elif tree == '髌骨关节面':
            #
            #     self.base_click(el_add_report.tree_binggu_guanjie_mian)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)
            # elif tree == '股骨滑车关节面':
            #
            #     self.base_click(el_add_report.tree_gugu_huache_guanjie_mian)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)
            # elif tree == '胫股内侧关节':
            #
            #     self.base_click(el_add_report.tree_jinggu_neice_guanjie)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)
            # elif tree == '胫骨内侧平台关节面':
            #
            #     self.base_click(el_add_report.tree_jinggu_neice_pingtai_guanjie_mian)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)
            # elif tree == '股骨内髁关节面':
            #
            #     self.base_click(el_add_report.tree_gugu_neihuai_guanjie_mian)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_2ji)
            # elif tree == '胫股外侧关节':
            #
            #     self.base_click(el_add_report.tree_jinggu_waice_guanjie)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)
            # elif tree == '胫骨外侧平台关节面':
            #
            #     self.base_click(el_add_report.tree_jinggu_waice_pingtai_guanjie_mian)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)
            # elif tree == '股骨外髁关节面':
            #
            #     self.base_click(el_add_report.tree_jinggu_waihuai_guanjie_mian)
            #     self.base_click(el_add_report.tree_guanjie_ruangu_3ji)


    def page_add_report_ruangu_3ji_multi(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, treename):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        with allure.step(f"点击膝关节退变标签"):
            self.zuoce_tab_xituibian.click()
        with allure.step("点击关节软骨及软骨下骨"):
            self.page_click_ruangu_3ji_multi(treename)
        with allure.step("点击提交报告"):
            self.tijiao_report().click()
            self.page_bi_tian_assure.click()