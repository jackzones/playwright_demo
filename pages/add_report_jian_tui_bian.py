from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
import time

class AddReportJianTuiBian(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guanjie_duiwei = self.page.locator(".el-radio-button__original-radio").get_by_text("关节对位")
        self.suntree_zhifangjianxi_jianfengxia = self.page.get_by_text("肩峰下脂肪间隙")
        self.suntree_zhifangjianxi_huitu = self.page.get_by_text("喙突与肱骨小结节脂肪间隙")
        self.check_xiazai = self.page.locator('//div[contains(text(),"股骨-坐骨间距减小")]/ancestor::tr//input[@type="checkbox"]')

        self.tab_guzhi = self.page.get_by_text("骨质")
        self.tree_guzhi_jianfengxia = self.page.get_by_text("肩胛骨肩峰下缘")
        self.tree_guzhi_xiaojieji = self.page.get_by_text("肱骨小结节")
        self.tree_guzhi_huitu = self.page.get_by_text("肩胛骨喙突")
        self.data_guzhi_zengsheng = self.page.locator('//div[text()="骨质增生"]/ancestor::tr//input[@type="checkbox"]')
        self.data_guzhi_zengsheng_and = self.page.locator('//div[text()="骨质增生伴骨髓水肿"]/ancestor::tr//input[@type="checkbox"]')

        self.tab_jianxiu = self.page.get_by_text("肩袖")
        #冈上肌腱
        self.suntree_gangshang_jianxiu = self.page.get_by_text("肩袖部", exact=True).first
        self.suntree_gangshang_jianxiu_guanjienang = self.page.get_by_text("肩袖部关节囊缘")
        self.suntree_gangshang_jianxiu_huanang = self.page.get_by_text("肩袖部滑囊缘")
        self.suntree_gangshang_jianxiu_jijian = self.page.get_by_text("肩袖部肌腱内")

        #肩胛下肌腱
        self.suntree_jianjiaxiajijian_jianxiu = self.page.get_by_text("肩袖部", exact=True).nth(2)

        # 肩袖 数据项 序号定位
        self.jianxiu_checkbox_1 = self.page.locator('//tr[1]//input[@type="checkbox"]')  # 第一行"正常"选项
        self.jianxiu_checkbox_2 = self.page.locator('//tr[2]//input[@type="checkbox"]')  # 第二行"局部全层撕裂IV°"选项
        self.jianxiu_checkbox_3 = self.page.locator('//tr[3]//input[@type="checkbox"]')  # 第三行"全层撕裂IV°，断端回缩"选项
        self.jianxiu_checkbox_4 = self.page.locator('//tr[4]//input[@type="checkbox"]')  # 第四行"钙化性肌腱炎"选项
        self.jianxiu_checkbox_5 = self.page.locator('//tr[5]//input[@type="checkbox"]')  # 第四行"钙化性肌腱炎"选项
        self.jianxiu_checkbox_6 = self.page.locator('//tr[6]//input[@type="checkbox"]')  # 第四行"钙化性肌腱炎"选项
        self.jianxiu_checkbox_7 = self.page.locator('//tr[7]//input[@type="checkbox"]')  # 第四行"钙化性肌腱炎"选项

    # 脂肪间隙数据选择
    def page_zhifang_jianxi_select_xiazai(self, suntree):
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
            with allure.step("点击骨质增生"):
                logger.info(f"点击骨质增生")
                self.data_guzhi_zengsheng.dispatch_event('click')
        elif data == "骨质增生伴骨髓水肿":
            with allure.step("点击骨质增生伴骨髓水肿"):
                logger.info(f"点击骨质增生伴骨髓水肿")
                self.data_guzhi_zengsheng_and.dispatch_event('click')

    def page_jianxiu_broken_data_select(self, data):
        if data == '1':
            self.jianxiu_checkbox_1.dispatch_event('click')
        elif data == '2':
            self.jianxiu_checkbox_2.dispatch_event('click')
        elif data == '3':
            self.jianxiu_checkbox_3.dispatch_event('click')
        elif data == '4':
            self.jianxiu_checkbox_4.dispatch_event('click')
        elif data == '5':
            self.jianxiu_checkbox_5.dispatch_event('click')
        elif data == '6':
            self.jianxiu_checkbox_6.dispatch_event('click')
        elif data == '7':
            self.jianxiu_checkbox_7.dispatch_event('click')



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

    # 肩袖-退变，全层撕裂，钙化性肌腱炎
    def page_jianxiu_select_broken(self, tree, suntree, data):
        if tree == "冈上肌腱":
            with allure.step("点击肩胛下肌腱"):
                logger.info(f"点击肩胛下肌腱")
                if suntree == "肩袖部":
                    self.suntree_gangshang_jianxiu.click()
                    self.page_jianxiu_broken_data_select(data)
                elif suntree == "肩袖部关节囊缘":
                    self.suntree_gangshang_jianxiu_guanjienang.click()
                    self.page_jianxiu_broken_data_select(data)
                elif suntree == "肩袖部滑囊缘":
                    self.suntree_gangshang_jianxiu_huanang.click()
                    self.page_jianxiu_broken_data_select(data)
                elif suntree == "肩袖部肌腱内":
                    self.suntree_gangshang_jianxiu_jijian.click()
                    self.page_jianxiu_broken_data_select(data)
        elif tree == "肩胛下肌腱":
            with allure.step("点击肩胛下肌腱"):
                logger.info(f"点击肩胛下肌腱")
                self.suntree_jianjiaxiajijian_jianxiu.click()
                self.page_jianxiu_broken_data_select(data)


    def page_guanjie_duiwei_data(self, suntree):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei.click()
            self.page_zhifang_jianxi_select_xiazai(suntree)
            self.check_xiazai.dispatch_event('click')

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

    def page_add_report_jian_tuibian_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, suntree,
                                                   tree, data):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(suntree)
        self.page_guzhi_data(tree, data)
        self.page_jianxiu_data(tree, data)
        self.page_tijiao_report()