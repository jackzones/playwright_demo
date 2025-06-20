from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
from time import sleep

class AddReportJianTuiBian(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guanjie_duiwei = self.page.locator('span.el-radio-button__inner:has-text("关节对位")')
        self.suntree_zhifangjianxi_jianfengxia = self.page.get_by_text("肩峰下脂肪间隙")
        self.suntree_zhifangjianxi_huitu = self.page.get_by_text("喙突与肱骨小结节脂肪间隙")
        self.check_xiazai = self.page.get_by_role("row", name="狭窄").locator("span").nth(1)

        self.tab_guzhi = self.page.get_by_text("骨质")
        self.tree_guzhi_jianfengxia = self.page.get_by_text("肩胛骨肩峰下缘")
        self.tree_guzhi_xiaojieji = self.page.get_by_text("肱骨小结节")
        self.tree_guzhi_huitu = self.page.get_by_text("肩胛骨喙突")
        self.data_guzhi_zengsheng = self.page.get_by_role("row", name="骨质增生 骨质增生，骨髓未见明显异常信号影").locator("span").nth(1)
        self.data_guzhi_zengsheng_and = self.page.get_by_role("row", name="骨质增生伴骨髓水肿 骨质增生，骨髓内可见小囊片状T1").locator("span").nth(1)

        self.tab_jianxiu = self.page.get_by_text("肩袖").first
        #冈上肌腱
        self.suntree_gangshang_jianxiu = self.page.get_by_text("肩袖部", exact=True).first
        self.suntree_gangshang_jianxiu_guanjienang = self.page.get_by_text("肩袖部关节囊缘")
        self.suntree_gangshang_jianxiu_huanang = self.page.get_by_text("肩袖部滑囊缘")
        self.suntree_gangshang_jianxiu_jijian = self.page.get_by_text("肩袖部肌腱内")

        #肩胛下肌腱
        self.suntree_jianjiaxiajijian_jianxiu = self.page.get_by_text("肩袖部", exact=True).nth(2)

        # 肩袖 数据项 序号定位
        self.jianxiu_checkbox_1 = self.page.get_by_role("row", name="正常").locator("span").nth(1)  # 第一行"正常"选项
        self.jianxiu_checkbox_2 = self.page.get_by_role("row", name="局部全层撕裂IV").locator("span").nth(1)  # 第二行"局部全层撕裂IV°"选项
        self.jianxiu_checkbox_3 = self.page.get_by_role("row", name="全层撕裂IV°，断端回缩").locator("span").nth(1)  # 第三行"全层撕裂IV°，断端回缩"选项
        self.jianxiu_checkbox_4 = self.page.get_by_role("row", name="钙化性肌腱炎").locator("span").nth(1)  # 第四行"钙化性肌腱炎"选项
        self.jianxiu_checkbox_5 = self.page.get_by_role("row", name="退变I°").locator("span").nth(1)  # "退变I"选项
        self.jianxiu_checkbox_6 = self.page.get_by_role("row", name="退变II°").locator("span").nth(1)  # "退变II"选项
        self.jianxiu_checkbox_7 = self.page.get_by_role("row", name="退变III°").locator("span").nth(1)  # "退变III"选项

        #标题选择
        self.title_jianfenxia = self.page.get_by_title("肩峰下撞击综合征").locator("span").nth(1)
        self.title_huituxia = self.page.get_by_title("喙突下撞击综合征").locator("span").nth(1)

    # 脂肪间隙数据选择
    def page_zhifang_jianxi_select_xiazai(self, suntree):
        sleep(1)
        if suntree == "肩峰下脂肪间隙":
            with allure.step("点击脂肪间隙-肩峰下脂肪间隙"):
                logger.info(f"点击脂肪间隙-肩峰下脂肪间隙")
                self.suntree_zhifangjianxi_jianfengxia.click()
        elif suntree == "喙突与肱骨小结节脂肪间隙":
            with allure.step("点击脂肪间隙-喙突与肱骨小结节脂肪间隙"):
                logger.info(f"点击脂肪间隙-喙突与肱骨小结节脂肪间隙")
                self.suntree_zhifangjianxi_huitu.click()

    def page_guzhi_zengsheng_data_select(self, data):
        if data == "骨质增生":
            with allure.step("勾选骨质增生"):
                logger.info(f"勾选骨质增生")
                self.data_guzhi_zengsheng.click()
        elif data == "骨质增生伴骨髓水肿":
            with allure.step("勾选骨质增生伴骨髓水肿"):
                logger.info(f"勾选骨质增生伴骨髓水肿")
                self.data_guzhi_zengsheng_and.click()
        else:
            logger.info(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    def page_jianxiu_broken_data_select(self, data):
        if data == '1':
            self.jianxiu_checkbox_1.click()
        elif data == '2':
            self.jianxiu_checkbox_2.click()
        elif data == '3':
            self.jianxiu_checkbox_3.click()
        elif data == '4':
            self.jianxiu_checkbox_4.click()
        elif data == '5':
            self.jianxiu_checkbox_5.click()
        elif data == '6':
            self.jianxiu_checkbox_6.click()
        elif data == '7':
            self.jianxiu_checkbox_7.click()
        else:
            logger.error(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    # 骨质-骨质增生
    def page_guzhi_select_zengsheng(self, tree, data):
        if tree == "肩胛骨肩峰下缘":
            with allure.step("点击肩胛骨肩峰下缘"):
                logger.info(f"点击脂肩胛骨肩峰下缘")
                self.tree_guzhi_jianfengxia.click()
                self.page_guzhi_zengsheng_data_select(data)
        elif tree == "肱骨小结节":
            with allure.step("点击肱骨小结节"):
                logger.info(f"点击肱骨小结节")
                self.tree_guzhi_xiaojieji.click()
                self.page_guzhi_zengsheng_data_select(data)
        elif tree == "肩胛骨喙突":
            with allure.step("点击肩胛骨喙突"):
                logger.info(f"点击肩胛骨喙突")
                self.tree_guzhi_huitu.click()
                self.page_guzhi_zengsheng_data_select(data)
        else:
            logger.info(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    # 肩袖-退变，全层撕裂，钙化性肌腱炎
    def page_jianxiu_select_broken(self, tree, suntree, data):
        if tree == "冈上肌腱":
            with allure.step("点击冈上肌腱"):
                logger.info(f"点击冈上肌腱")
                if suntree == "肩袖部":
                    with allure.step("点击肩袖部"):
                        logger.info(f"点击肩袖部")
                        self.suntree_gangshang_jianxiu.click()
                        self.page_jianxiu_broken_data_select(data)
                elif suntree == "肩袖部关节囊缘":
                    with allure.step("点击肩袖部关节囊缘"):
                        logger.info(f"点击肩袖部关节囊缘")
                        self.suntree_gangshang_jianxiu_guanjienang.click()
                        self.page_jianxiu_broken_data_select(data)
                elif suntree == "肩袖部滑囊缘":
                    with allure.step("点击肩袖部滑囊缘"):
                        logger.info(f"点击肩袖部滑囊缘")
                        self.suntree_gangshang_jianxiu_huanang.click()
                        self.page_jianxiu_broken_data_select(data)
                elif suntree == "肩袖部肌腱内":
                    with allure.step("点击肩袖部肌腱内"):
                        logger.info(f"点击肩袖部肌腱内")
                        self.suntree_gangshang_jianxiu_jijian.click()
                        self.page_jianxiu_broken_data_select(data)
                else:
                    logger.info(f"无效的部位参数: {suntree}")
                    raise ValueError(f"无效的部位参数: {suntree}")
        elif tree == "肩胛下肌腱":
            with allure.step("点击肩胛下肌腱-肩袖部"):
                logger.info(f"点击肩胛下肌腱-肩袖部")
                self.suntree_jianjiaxiajijian_jianxiu.click()
                self.page_jianxiu_broken_data_select(data)
        else:
            logger.error(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    def page_guanjie_duiwei_data(self, suntree):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei.click()
            self.page_zhifang_jianxi_select_xiazai(suntree)
            # self.check_xiazai.dispatch_event('click')
            self.check_xiazai.click()

    def page_guzhi_data(self, tree, data):
        with allure.step("点击骨质标签"):
            logger.info(f"点击骨质标签")
            self.tab_guzhi.click()
            self.page_guzhi_select_zengsheng(tree, data)

    def page_jianxiu_data(self, tree, suntree, data):
        with allure.step("点击肩袖标签"):
            logger.info(f"点击肩袖标签")
            self.tab_jianxiu.click()
            self.page_jianxiu_select_broken(tree, suntree, data)

    def page_select_title1(self):
        with allure.step("勾选标题：肩峰下撞击综合征&喙突下撞击综合征"):
            logger.info(f"勾选标题：肩峰下撞击综合征&喙突下撞击综合征")
            self.title_jianfenxia.click()
            self.title_huituxia.click()
            self.title_ok_btn.click()


    def page_add_report_jian_tuibian_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, suntree1, tree1, data1, tree2, suntree2, data2):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(suntree1)
        self.page_guzhi_data(tree1, data1)
        self.page_jianxiu_data(tree2, suntree2, data2)
        self.page_tijiao_report()

    def page_add_report_jian_tuibian_title2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, suntree1, tree1, data1, tree2, suntree2, data2, suntree3, tree3, data3, tree4, suntree4, data4):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(suntree1)
        self.page_guzhi_data(tree1, data1)
        self.page_jianxiu_data(tree2, suntree2, data2)
        self.page_guanjie_duiwei_data(suntree3)
        self.page_guzhi_data(tree3, data3)
        self.page_jianxiu_data(tree4, suntree4, data4)
        self.page_tijiao_report()
        self.page_select_title1()
