from time import sleep

from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
import time

class AddReportJianWaiShang(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        self.tab_guanjie_duiwei = self.page.locator('span.el-radio-button__inner:has-text("关节对位")').first
        self.tab_guanjie_duiwei_hebing = self.page.locator('span.el-radio-button__inner:has-text("关节对位")').nth(1)
        #关节对位
        self.tree_yugong_guanjie = self.page.get_by_text("盂肱关节").first
        self.data_qiantuowei = self.page.get_by_role("row", name="前脱位").locator("span").nth(1)
        self.data_houtuowei = self.page.get_by_role("row", name="后脱位").locator("span").nth(1)
        #骨质
        self.tab_guzhi = self.page.locator('span.el-radio-button__inner:has-text("骨质")').first
        self.tab_guzhi_hebing = self.page.locator('span.el-radio-button__inner:has-text("骨质")').nth(1)
        ##肱骨
        self.suntree_gonggu_touhouyuan = self.page.get_by_text("头后缘")
        self.suntree_gonggu_touqianyuan = self.page.get_by_text("头前缘")
        self.touhouyuan_checkbox_1 = self.page.get_by_role("row", name="Hill-Sachs损伤：肱骨头后外侧面骨挫伤").locator("span").nth(1)  # 第一行"Hill-Sachs损伤：肱骨头后外侧面骨挫伤"选项
        self.touhouyuan_checkbox_2 = self.page.get_by_role("row", name="Hill-Sachs损伤：肱骨头后外侧面凹陷骨折").locator("span").nth(1)  # 第二行"Hill-Sachs损伤：肱骨头后外侧面凹陷骨折"选项
        self.touqianyuan_checkbox_1 = self.page.get_by_role("row", name="反Hill-Sachs损伤：肱骨头前内侧面骨挫伤").locator("span").nth(1)  # 第一行"反Hill-Sachs损伤：肱骨头前内侧面骨挫伤"选项
        self.touqianyuan_checkbox_2 = self.page.get_by_role("row", name="反Hill-Sachs损伤：肱骨头前内侧面凹陷骨折").locator("span").nth(1)  # 第二行"反Hill-Sachs损伤：肱骨头前内侧面凹陷骨折"选项
        ##肩胛盂
        self.suntree_jianxiayu_houyuan = self.page.get_by_text("后缘", exact=True)
        self.suntree_jianxiayu_qianyuan = self.page.get_by_text("前缘", exact=True)
        self.jianxiayu_checkbox_1 = self.page.get_by_role("row", name="骨挫伤").locator("span").nth(1)  # 第一行"骨挫伤"选项
        self.jianxiayu_checkbox_2 = self.page.get_by_role("row", name="骨折、断端无移位").locator("span").nth(1)  # 第二行"骨折、断端无移位"选项
        self.jianxiayu_checkbox_3 = self.page.get_by_role("row", name="骨折、断端移位").locator("span").nth(1)  # 第三行"骨折、断端移位"选项

        # self.tab_jianxiu = self.page.get_by_text("肩袖").first
        # self.tab_jianxiu = self.page.locator('span.el-radio-button__inner:has-text("肩袖")').first
        self.tab_jianxiu = self.page.locator('span.el-radio-button__inner >> text="肩袖"').first
        self.tab_jianxiu_hebing = self.page.locator('span.el-radio-button__inner >> text="肩袖"').nth(1)
        self.suntree_jianjiaxiajijian_jianxiu = self.page.get_by_text("肩袖部", exact=True).nth(2)
        self.suntree_gangxiajijian_jianxiu = self.page.get_by_text("肩袖部", exact=True).nth(1)
        # 肩袖 数据项 序号定位
        self.jianxiu_checkbox_1 = self.page.get_by_role("row", name="正常").locator("span").nth(1)  # 第一行"正常"选项
        self.jianxiu_checkbox_2 = self.page.get_by_role("row", name="部分撕裂I°").locator("span").nth(1)
        self.jianxiu_checkbox_3 = self.page.get_by_role("row", name="部分撕裂II°").locator("span").nth(1)
        self.jianxiu_checkbox_4 = self.page.get_by_role("row", name="部分撕裂III°").locator("span").nth(1)
        self.jianxiu_checkbox_5 = self.page.get_by_role("row", name="局部全层撕裂IV").locator("span").nth(1)
        self.jianxiu_checkbox_6 = self.page.get_by_role("row", name="全层撕裂IV°，断端回缩").locator("span").nth(1)

        self.tab_guanjieyucun = self.page.get_by_text("关节盂唇")
        self.suntree_guanjieyucun_qianxia = self.page.get_by_text("前下盂唇")
        # 关节盂唇 数据项 序号定位
        self.yucun_checkbox_1 = self.page.get_by_role("row", name="正常").locator("span").nth(1)  # 第一行"正常"选项
        self.yucun_checkbox_2 = self.page.get_by_role("row", name="损伤I-II").locator("span").nth(1)
        self.yucun_checkbox_3 = self.page.get_by_role("row", name="Bankart损伤：前下盂唇撕裂III").locator("span").nth(1)
        self.yucun_checkbox_4 = self.page.get_by_role("row", name="ALPSA损伤：前下盂唇撕裂III").locator("span").nth(1)
        self.yucun_checkbox_5 = self.page.get_by_role("row", name="Perthes损伤：前下盂唇撕裂III").locator("span").nth(1)
        self.yucun_checkbox_6 = self.page.get_by_role("row", name="GLAD损伤：肩胛盂前下盂唇撕裂III").locator("span").nth(1)

#外伤合并退变
        self.tab_ruanzhuzhi = self.page.locator('span.el-radio-button__inner:has-text("软组织")').first
        self.suntree_gangshang_jianxiu = self.page.get_by_text("肩袖部", exact=True).first
        self.tree_guzhi_jianfengxia = self.page.get_by_text("肩胛骨肩峰下缘")
        self.data_guzhi_zengsheng = self.page.get_by_role("row", name="骨质增生 骨质增生，骨髓未见明显异常信号影").locator("span").nth(1)
        self.jianxiu_checkbox_2_hebing = self.page.get_by_role("row", name="局部全层撕裂IV").locator("span").nth(1)  # 第二行"局部全层撕裂IV°"选项
        self.suntree_zhifangjianxi_jianfengxia = self.page.get_by_text("肩峰下脂肪间隙")
        self.check_xiazai = self.page.get_by_role("row", name="狭窄").locator("span").nth(1)


        #标题选择
        self.title_bhs_sunshang = self.page.get_by_title("关节Bankart-Hill-Sachs损伤").locator("span").nth(1)
        self.title_bhs_sunshang_fan = self.page.get_by_title("关节反Bankart-反Hill-Sachs损伤").locator("span").nth(1)


    def page_jianxiayu_broken_data_select(self, data):
        sleep(0.1)
        if data == '骨挫伤':
            self.jianxiayu_checkbox_1.click()
        elif data == '骨折、断端无移位':
            self.jianxiayu_checkbox_2.click()
        elif data == '骨折、断端移位':
            self.jianxiayu_checkbox_3.click()
        else:
            logger.error(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    def page_gonggu_touqianhouyuan_broken_data_select(self, data):
        sleep(0.1)
        if data == 'Hill-Sachs损伤：肱骨头后外侧面骨挫伤':
            self.touhouyuan_checkbox_1.click()
        elif data == 'Hill-Sachs损伤：肱骨头后外侧面凹陷骨折':
            self.touhouyuan_checkbox_2.click()
        elif data == '反Hill-Sachs损伤：肱骨头前内侧面骨挫伤':
            self.touqianyuan_checkbox_1.click()
        elif data == '反Hill-Sachs损伤：肱骨头前内侧面凹陷骨折':
            self.touqianyuan_checkbox_2.click()
        else:
            logger.error(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    # 骨质-肱骨（tree）-头后缘-data
    def page_guzhi_select_broken(self, tree, suntree, data):
        self.tab_guzhi.click()
        if tree == "肱骨":
            with allure.step("点击骨质-肱骨"):
                logger.info(f"点击骨质-肱骨")
                if suntree == "头后缘":
                    with allure.step("点击头后缘"):
                        logger.info(f"点击头后缘")
                        self.suntree_gonggu_touhouyuan.click()
                        self.page_gonggu_touqianhouyuan_broken_data_select(data)
                elif suntree == "头前缘":
                    with allure.step("点击头前缘"):
                        logger.info(f"点击头前缘")
                        self.suntree_gonggu_touqianyuan.click()
                        self.page_gonggu_touqianhouyuan_broken_data_select(data)
                else:
                    logger.info(f"无效的部位参数: {suntree}")
                    raise ValueError(f"无效的部位参数: {suntree}")
        elif tree == "肩胛盂":
            with allure.step("点击骨质-肩胛盂"):
                logger.info(f"点击骨质-肩胛盂")
                if suntree == "后缘":
                    with allure.step("点击后缘"):
                        logger.info(f"点击后缘")
                        self.suntree_jianxiayu_houyuan.click()
                        self.page_jianxiayu_broken_data_select(data)
                elif suntree == "前缘":
                    with allure.step("点击前缘"):
                        logger.info(f"点击前缘")
                        self.suntree_jianxiayu_qianyuan.click()
                        self.page_jianxiayu_broken_data_select(data)
        else:
            logger.error(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")


    def page_yugong_guanjie_select_data(self, data):
        with allure.step("点击盂肱关节"):
            logger.info(f"点击盂肱关节")
            self.tree_yugong_guanjie.click()
            sleep(0.5)
            if data == "前脱位":
                self.data_qiantuowei.click()
            elif data == "后脱位":
                self.data_houtuowei.click()

    def page_guanjie_duiwei_data(self, data):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei.click()
            self.page_yugong_guanjie_select_data(data)

    # def page_guanjie_duiwei_data_hebing(self, data):
    #     with allure.step("点击关节对位标签"):
    #         logger.info(f"点击关节对位标签")
    #         self.tab_guanjie_duiwei_hebing.click()
    #         self.page_yugong_guanjie_select_data(data)

    def page_jianxiu_broken_data_select(self, data):
        sleep(0.6)
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
        else:
            logger.error(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    def page_jianxiu_broken_data_select_hebing(self, data):
        sleep(0.6)
        if data == '1':
            self.jianxiu_checkbox_1.click()
        elif data == '2':
            self.jianxiu_checkbox_2_hebing.click()
        else:
            logger.error(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    def page_yucun_broken_data_select(self, data):
        if data == '1':
            self.yucun_checkbox_1.click()
        elif data == '2':
            self.yucun_checkbox_2.click()
        elif data == '3':
            self.yucun_checkbox_3.click()
        elif data == '4':
            self.yucun_checkbox_4.click()
        elif data == '5':
            self.yucun_checkbox_5.click()
        elif data == '6':
            self.yucun_checkbox_6.click()
        else:
            logger.error(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")

    # 肩袖-退变，全层撕裂，钙化性肌腱炎
    def page_jianxiu_select_broken(self, tree, data):
        if tree == "冈下肌腱":
            with allure.step("点击冈下肌腱-肩袖部"):
                logger.info(f"点击冈下肌腱-肩袖部")
                self.suntree_gangxiajijian_jianxiu.click()
                self.page_jianxiu_broken_data_select(data)
        elif tree == "肩胛下肌腱":
            with allure.step("点击肩胛下肌腱-肩袖部"):
                logger.info(f"点击肩胛下肌腱-肩袖部")
                self.suntree_jianjiaxiajijian_jianxiu.click()
                self.page_jianxiu_broken_data_select(data)
        else:
            logger.error(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    # 关节盂唇-前下盂唇
    def page_guanjieyucun_select_broken(self, tree, data):
        if tree == "前下盂唇":
            with allure.step("点击前下盂唇"):
                logger.info(f"点击前下盂唇")
                self.suntree_guanjieyucun_qianxia.click()
                self.page_yucun_broken_data_select(data)
        else:
            logger.error(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    def page_jianxiu_data(self, tree, data):
        with allure.step("点击肩袖标签"):
            logger.info(f"点击肩袖标签")
            self.tab_jianxiu.click()
            self.page_jianxiu_select_broken(tree, data)

    def page_guanjieyucun_data(self, tree, data):
        with allure.step("点击关节盂唇标签"):
            logger.info(f"点击关节盂唇标签")
            self.tab_guanjieyucun.click()
            self.page_guanjieyucun_select_broken(tree, data)

    def page_select_title1(self):
        with allure.step("勾选标题：肩关节Bankart-Hill-Sachs损伤&肩关节反Bankart-反Hill-Sachs损伤"):
            logger.info(f"勾选标题：肩关节Bankart-Hill-Sachs损伤&肩关节反Bankart-反Hill-Sachs损伤")
            self.title_bhs_sunshang.click()
            self.title_bhs_sunshang_fan.click()
            self.title_ok_btn.click()

    def page_add_report_jian_waishang_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(data1)
        self.page_guzhi_select_broken(tree2, suntree2, data2)
        self.page_guzhi_select_broken(tree3, suntree3, data3)
        self.page_jianxiu_data(tree4, data4)
        self.page_guanjieyucun_data(tree5, data5)
        self.page_tijiao_report()

    def page_add_report_jian_waishang_title2(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(data1)
        self.page_guzhi_select_broken(tree2, suntree2, data2)
        self.page_guzhi_select_broken(tree3, suntree3, data3)
        self.page_jianxiu_data(tree4, data4)
        self.page_tijiao_report()

    # def page_add_report_jian_waishang_title3(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, data6, tree7, suntree7, data7, tree8, suntree8, data8, tree9, data9):
    #     self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
    #     self.page_guanjie_duiwei_data(data1)
    #     self.page_guzhi_select_broken(tree2, suntree2, data2)
    #     self.page_guzhi_select_broken(tree3, suntree3, data3)
    #     self.page_jianxiu_data(tree4, data4)
    #     self.page_guanjieyucun_data(tree5, data5)
    #     self.page_guanjie_duiwei_data(data6)
    #     self.page_guzhi_select_broken(tree7, suntree7, data7)
    #     self.page_guzhi_select_broken(tree8, suntree8, data8)
    #     self.page_jianxiu_data(tree9, data9)
    #     self.page_tijiao_report()
    #     self.page_select_title1()

    def page_add_report_jian_waishang_title3(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, tree5, data5, data6, tree7, suntree7, data7, tree8, suntree8, data8, tree9, data9):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(data1)
        self.page_guanjie_duiwei_data(data6)
        self.page_guzhi_select_broken(tree2, suntree2, data2)
        self.page_guzhi_select_broken(tree3, suntree3, data3)
        self.page_guzhi_select_broken(tree7, suntree7, data7)
        self.page_guzhi_select_broken(tree8, suntree8, data8)
        self.page_jianxiu_data(tree9, data9)
        self.page_jianxiu_data(tree4, data4)
        self.page_guanjieyucun_data(tree5, data5)
        self.page_tijiao_report()
        self.page_select_title1()

    def page_side_tuibian_select(self, name):
        with allure.step("点击左侧退变"):
            logger.info(f"点击左侧退变")
            if name == "左肩":
                self.tab_ruanzhuzhi.click()
                self.page.get_by_text("左 肩关节退变").click()
            elif name == "右肩":
                self.tab_ruanzhuzhi.click()
                self.page.get_by_text("右 肩关节退变").click()
            else:
                logger.info(f"无效的部位参数: {name}")
                raise ValueError(f"无效的部位参数: {name}")


    # 肩袖-退变，全层撕裂，钙化性肌腱炎
    def page_jianxiu_select_broken_hebing(self, tree, suntree, data):
        if tree == "冈上肌腱":
            with allure.step("点击冈上肌腱"):
                logger.info(f"点击冈上肌腱")
                if suntree == "肩袖部":
                    with allure.step("点击肩袖部"):
                        logger.info(f"点击肩袖部")
                        self.suntree_gangshang_jianxiu.click()
                        self.page_jianxiu_broken_data_select_hebing(data)
                else:
                    logger.info(f"无效的部位参数: {suntree}")
                    raise ValueError(f"无效的部位参数: {suntree}")
        else:
            logger.error(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")

    def page_jianxiu_data_hebing(self, tree, suntree, data):
        with allure.step("点击肩袖标签"):
            logger.info(f"点击肩袖标签")
            self.tab_jianxiu_hebing.click()
            self.page_jianxiu_select_broken_hebing(tree, suntree, data)

    def page_guzhi_data(self, tree, data):
        with allure.step("点击骨质标签"):
            logger.info(f"点击骨质标签")
            self.tab_guzhi_hebing.click()
            self.page_guzhi_select_zengsheng(tree, data)

    def page_guzhi_zengsheng_data_select(self, data):
        if data == "骨质增生":
            with allure.step("勾选骨质增生"):
                logger.info(f"勾选骨质增生")
                self.data_guzhi_zengsheng.click()
        else:
            logger.info(f"无效的数据参数: {data}")
            raise ValueError(f"无效的数据参数: {data}")


    # 骨质-骨质增生
    def page_guzhi_select_zengsheng(self, tree, data):
        if tree == "肩胛骨肩峰下缘":
            with allure.step("点击肩胛骨肩峰下缘"):
                logger.info(f"点击脂肩胛骨肩峰下缘")
                self.tree_guzhi_jianfengxia.click()
                self.page_guzhi_zengsheng_data_select(data)
        else:
            logger.info(f"无效的部位参数: {tree}")
            raise ValueError(f"无效的部位参数: {tree}")
        # 脂肪间隙数据选择

    def page_zhifang_jianxi_select_xiazai(self, suntree):
        sleep(1)
        if suntree == "肩峰下脂肪间隙":
            with allure.step("点击脂肪间隙-肩峰下脂肪间隙"):
                logger.info(f"点击脂肪间隙-肩峰下脂肪间隙")
                self.suntree_zhifangjianxi_jianfengxia.click()

    def page_guanjie_duiwei_data_hebing(self, suntree):
        with allure.step("点击关节对位标签"):
            logger.info(f"点击关节对位标签")
            self.tab_guanjie_duiwei_hebing.click()
            self.page_zhifang_jianxi_select_xiazai(suntree)
            self.check_xiazai.click()

    def page_add_report_jian_waishanghebing_tuibian_title1(self, fangshe_bianhao, buweimingcheng, leibie, xibuwei, data1, tree2, suntree2, data2, tree3, suntree3, data3, tree4, data4, suntree5, tree6, data6, tree7, suntree7, data7):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie, xibuwei)
        self.page_guanjie_duiwei_data(data1)
        self.page_guzhi_select_broken(tree2, suntree2, data2)
        self.page_guzhi_select_broken(tree3, suntree3, data3)
        self.page_jianxiu_data(tree4, data4)
        self.page_side_tuibian_select(xibuwei)
        sleep(2)
        self.page_guanjie_duiwei_data_hebing(suntree5)
        self.page_guzhi_data(tree6, data6)
        self.page_jianxiu_data_hebing(tree7, suntree7, data7)
        self.page_tijiao_report()