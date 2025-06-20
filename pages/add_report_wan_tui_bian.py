from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
from time import sleep

class AddReportWanTuiBian(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guanjie_duiwei = self.page.locator('span.el-radio-button__inner:has-text("关节对位")')
        self.tab_guanjie_duiwei_hebing = self.page.locator('span.el-radio-button__inner:has-text("关节对位")').nth(1)
        # self.tree_guanjie_duiwei_xiaci = self.page.get_by_text("下尺桡关节")
        # self.tree_guanjie_duiwei_xiaci = self.page.get_by_text("下尺桡关节", exact=True)
        self.tree_guanjie_duiwei_xiaci = self.page.locator('div.el-tree-node__content:has-text("下尺桡关节")')
        self.tree_guanjie_duiwei_xiaci_hebing = self.page.locator('div.el-tree-node__content:has-text("下尺桡关节")')
        self.data_guanjie_duiwei_yangxing = self.page.get_by_role("row", name="尺骨变异征阳性").locator("span").nth(1)
        self.data_guanjie_duiwei_yinxing = self.page.get_by_role("row", name="尺骨变异征阴性").locator("span").nth(1)

        self.tab_guzhi = self.page.locator('span.el-radio-button__inner:has-text("骨质")')
        self.tab_guzhi_hebing = self.page.locator('span.el-radio-button__inner:has-text("骨质")').nth(1)
        self.tree_guzhi_yuegu = self.page.get_by_text("月骨")
        self.tree_guzhi_sanjiaogu = self.page.get_by_text("三角骨")
        self.tree_guzhi_chigu_yuanduan = self.page.get_by_text("尺骨远端").first
        self.tree_guzhi_gouzhuanggu = self.page.get_by_text("钩状骨")
        self.data_guzhi_gusui_suizhong = self.page.get_by_role("row", name="关节软骨软化，伴软骨下骨髓水肿").locator("span").nth(1)
        self.data_guzhi_nangxingbian = self.page.get_by_role("row", name="关节软骨软化，伴软骨下囊性变").locator("span").nth(1)

        self.tab_ruanzhuzhi = self.page.locator('span.el-radio-button__inner:has-text("软组织")').first
        #标题选择
        self.title_chigu = self.page.get_by_title("尺骨撞击综合征").locator("span").nth(1)
        self.title_chice = self.page.get_by_title("尺侧撞击综合征").locator("span").nth(1)
        self.title_cigu_jingtu = self.page.get_by_title("尺骨茎突撞击综合征").locator("span").nth(1)
        self.title_gouyue = self.page.get_by_title("钩月撞击综合征").locator("span").nth(1)

    def page_side_tuibian_select(self, name):
        with allure.step("点击左侧退变"):
            logger.info(f"点击左侧退变")
            if name == "左腕":
                self.tab_ruanzhuzhi.click()
                self.page.get_by_text("左 腕关节退变").click()
            elif name == "右腕":
                self.tab_ruanzhuzhi.click()
                self.page.get_by_text("右 腕关节退变").click()
            else:
                logger.info(f"无效的部位参数: {name}")
                raise ValueError(f"无效的部位参数: {name}")

    def page_guzhi_ruangu_ruanhua_data_select(self, data):
        sleep(0.1)
        if data == "1":
            with allure.step("勾选关节软骨软化，伴软骨下骨髓水肿"):
                logger.info(f"勾选关节软骨软化，伴软骨下骨髓水肿")
                self.data_guzhi_gusui_suizhong.click()
        elif data == "2":
            with allure.step("勾选关节软骨软化，伴软骨下囊性变"):
                logger.info(f"勾选关节软骨软化，伴软骨下囊性变")
                self.data_guzhi_nangxingbian.click()
        else:
            logger.info(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    def page_guanjie_duiwei_data_select(self, data):
        sleep(3)
        if data == "尺骨变异征阳性":
            with allure.step("勾选尺骨变异征阳性"):
                logger.info(f"勾选尺骨变异征阳性")
                self.data_guanjie_duiwei_yangxing.click()
        elif data == "尺骨变异征阴性":
            with allure.step("勾选尺骨变异征阴性"):
                logger.info(f"勾选尺骨变异征阴性")
                self.data_guanjie_duiwei_yinxing.click()
        else:
            logger.info(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    # 骨质-软骨软化
    def page_guzhi_select_ruangu_ruanhua(self, tree, data):
        if tree == "月骨":
            with allure.step("点击月骨"):
                logger.info(f"点击月骨")
                self.tree_guzhi_yuegu.click()
                self.page_guzhi_ruangu_ruanhua_data_select(data)
        elif tree == "三角骨":
            with allure.step("点击三角骨"):
                logger.info(f"点击三角骨")
                self.tree_guzhi_sanjiaogu.click()
                self.page_guzhi_ruangu_ruanhua_data_select(data)
        elif tree == "尺骨远端":
            with allure.step("点击尺骨远端"):
                logger.info(f"点击尺骨远端")
                self.tree_guzhi_chigu_yuanduan.click()
                self.page_guzhi_ruangu_ruanhua_data_select(data)
        elif tree == "钩状骨":
            with allure.step("点击钩状骨"):
                logger.info(f"点击钩状骨")
                self.tree_guzhi_gouzhuanggu.click()
                self.page_guzhi_ruangu_ruanhua_data_select(data)
        else:
            logger.info(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

        # 关节对位-
    def page_guanjie_duiwei_select(self, tree, data):
        if tree == "下尺桡关节":
            with allure.step("点击下尺桡关节"):
                logger.info(f"点击下尺桡关节")
                # self.tree_guanjie_duiwei_xiaci.click()
                self.tree_guanjie_duiwei_xiaci.click()
                self.page_guanjie_duiwei_data_select(data)
        else:
            logger.info(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    def page_guzhi_data(self, tree, data):
        with allure.step("点击骨质标签"):
            logger.info(f"点击骨质标签")
            self.tab_guzhi.click()
            self.page_guzhi_select_ruangu_ruanhua(tree, data)

    def page_guzhi_data_hebing(self, tree, data):
        with allure.step("点击骨质标签"):
            logger.info(f"点击骨质标签")
            self.tab_guzhi_hebing.click()
            self.page_guzhi_select_ruangu_ruanhua(tree, data)

    def page_guanjie_duiwei_data(self, tree, data):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei.click()
            self.page_guanjie_duiwei_select(tree, data)

    def page_guanjie_duiwei_data_hebing(self, tree, data):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei_hebing.click()
            self.page_guanjie_duiwei_select(tree, data)

    def page_select_title1(self):
        with allure.step("勾选标题：尺骨撞击综合征、尺侧撞击综合征、尺骨茎突撞击综合征、钩月撞击综合征"):
            logger.info(f"勾选标题：尺骨撞击综合征、尺侧撞击综合征、尺骨茎突撞击综合征、钩月撞击综合征")
            self.title_chigu.click()
            self.title_chice.click()
            self.title_cigu_jingtu.click()
            self.title_gouyue.click()
            self.title_ok_btn.click()


    def page_add_report_wan_tuibian_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(tree1, data1)
        self.page_guzhi_data(tree2, data2)
        self.page_tijiao_report()

    def page_add_report_wan_tuibian_title2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(tree1, data1)
        self.page_guzhi_data(tree2, data2)
        self.page_guzhi_data(tree3, data3)
        self.page_tijiao_report()

    def page_add_report_wan_tuibian_title3(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(tree1, data1)
        self.page_guzhi_data(tree2, data2)
        self.page_guzhi_data(tree3, data3)
        self.page_guzhi_data(tree4, data4)
        self.page_guzhi_data(tree5, data5)
        self.page_tijiao_report()

    def page_add_report_wan_tuibian_title4(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guzhi_data(tree1, data1)
        self.page_guzhi_data(tree2, data2)
        self.page_tijiao_report()

    def page_add_report_wan_tuibian_title5(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guzhi_data(tree1, data1)
        self.page_guzhi_data(tree2, data2)
        self.page_guzhi_data(tree3, data3)
        self.page_guzhi_data(tree4, data4)
        self.page_tijiao_report()

    def page_add_report_wan_tuibian_title6(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(tree1, data1)
        self.page_guzhi_data(tree2, data2)
        self.page_guanjie_duiwei_data(tree3, data3)
        self.page_guzhi_data(tree4, data4)
        self.page_guzhi_data(tree5, data5)
        self.page_guzhi_data(tree6, data6)
        self.page_tijiao_report()
        self.page_select_title1()

    def page_add_report_wan_tuibian_title7(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, tree1, data1, tree2, data2, tree3, data3, tree4, data4, tree5, data5, tree6, data6):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_side_tuibian_select(xibuwei)
        sleep(2)
        self.page_guanjie_duiwei_data_hebing(tree1, data1)
        self.page_guzhi_data_hebing(tree2, data2)
        self.page_guanjie_duiwei_data_hebing(tree3, data3)
        self.page_guzhi_data_hebing(tree4, data4)
        self.page_guzhi_data_hebing(tree5, data5)
        self.page_guzhi_data_hebing(tree6, data6)
        self.page_tijiao_report()
        self.page_select_title1()