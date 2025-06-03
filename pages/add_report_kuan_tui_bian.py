from playwright.sync_api import Page
from pages.add_report_base_page import AddReportBasePage
import allure
from utils.log import logger
import time

class AddReportKuanTuiBian(AddReportBasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # 可以添加膝退变特有的元素定位
        #股骨-坐骨标签
        self.tab_gugu_zuogu = self.page.get_by_text("股骨-坐骨")
        self.tree_suangkuan_jiangu = self.page.get_by_text("间距").first
        self.tree_youkuan_jiangu = self.page.get_by_text("间距").nth(1)
        self.tree_zuokuan_jiangu = self.page.get_by_text("间距").nth(2)
        self.tree_suangkuan_gufangji = self.page.get_by_text("股方肌").first
        self.tree_youkuan_gufangji = self.page.get_by_text("股方肌").nth(1)
        self.tree_zuokuan_gufangji = self.page.get_by_text("股方肌").nth(2)
        self.check_jianju_jiansao = self.page.locator('//div[contains(text(),"股骨-坐骨间距减小")]/ancestor::tr//input[@type="checkbox"]')
        self.check_gufangji_suizhong = self.page.locator('//div[contains(text(),"股方肌水肿")]/ancestor::tr//input[@type="checkbox"]')
        #关节软骨及软骨下骨
        self.tab_guanjie_ruangu = self.page.get_by_text("关节软骨及软骨下骨")
        ##双髋
        self.tree_suangkuan_guanjie = self.page.get_by_text("双髋关节")
        self.tree_suangkuan_kuanjiu = self.page.get_by_text("髋臼关节面").first
        self.tree_suangkuan_gugutou = self.page.get_by_text("股骨头关节面").first
        ##右髋
        self.tree_youkuan_guanjie = self.page.get_by_text("右髋关节")
        self.tree_youkuan_kuanjiu = self.page.get_by_text("髋臼关节面").nth(1)
        self.tree_youkuan_gugutou = self.page.get_by_text("股骨头关节面").nth(1)
        ##左髋
        self.tree_zuokuan_guanjie = self.page.get_by_text("左髋关节")
        self.tree_zuokuan_kuanjiu = self.page.get_by_text("髋臼关节面").nth(2)
        self.tree_zuokuan_gugutou = self.page.get_by_text("股骨头关节面").nth(2)

        self.check_1ji = self.page.locator('//div[(text()="软骨软化I级")]/ancestor::tr//input[@type="checkbox"]')
        self.check_1ji_and = self.page.locator('//div[(text()="软骨软化I级，伴软骨下骨髓水肿")]/ancestor::tr//input[@type="checkbox"]')
        self.check_2ji = self.page.locator('//div[(text()="软骨软化II级")]/ancestor::tr//input[@type="checkbox"]')
        self.check_2ji_and = self.page.locator('//div[(text()="软骨软化II级，伴软骨下骨髓水肿")]/ancestor::tr//input[@type="checkbox"]')
        self.check_3ji = self.page.locator('//div[(text()="软骨软化III级")]/ancestor::tr//input[@type="checkbox"]')
        self.check_3ji_and = self.page.locator('//div[(text()="软骨软化III级，伴软骨下骨髓水肿")]/ancestor::tr//input[@type="checkbox"]')
        self.check_4ji = self.page.locator('//div[(text()="软骨软化IV级")]/ancestor::tr//input[@type="checkbox"]')
        self.check_4ji_and = self.page.locator('//div[(text()="软骨软化IV级，伴软骨下骨髓水肿")]/ancestor::tr//input[@type="checkbox"]')

        #关节形态
        self.tab_guanjie_xingtai = self.page.get_by_text("关节形态")
        ##双髋
        self.tree_suangkuan_kuanjiu_2 = self.page.get_by_text("髋臼").first
        self.tree_suangkuan_gugutou_2 = self.page.get_by_text("股骨头").first
        ##右髋
        self.tree_youkuan_kuanjiu_2 = self.page.get_by_text("髋臼").nth(1)
        self.tree_youkuan_gugutou_2 = self.page.get_by_text("股骨头").nth(1)
        ##左髋
        self.tree_zuokuan_kuanjiu_2 = self.page.get_by_text("髋臼").nth(2)
        self.tree_zuokuan_gugutou_2 = self.page.get_by_text("股骨头").nth(2)

        self.check_baorong_guodu = self.page.locator('//div[(text()="包容过度")]/ancestor::tr//input[@type="checkbox"]')
        self.check_waiyuan_penglong = self.page.locator('//div[(text()="头颈交界外缘膨隆")]/ancestor::tr//input[@type="checkbox"]')

    def page_check_gugu(self, tree):
        with allure.step("点击股骨-坐骨标签"):
            logger.info(f"点击股骨-坐骨标签")
            self.tab_gugu_zuogu.click()
        if tree == '双髋':
            with allure.step("勾选坐骨间距减小"):
                logger.info(f"勾选坐骨间距减小")
                self.tree_suangkuan_jiangu.click()
                self.check_jianju_jiansao.dispatch_event('click')
            with allure.step("勾选股方肌水肿"):
                logger.info(f"勾选股方肌水肿")
                self.tree_suangkuan_gufangji.click()
                self.check_gufangji_suizhong.dispatch_event('click')
        elif tree == '左髋':
            with allure.step("勾选坐骨间距减小"):
                logger.info(f"勾选坐骨间距减小")
                self.tree_zuokuan_jiangu.click()
                self.check_jianju_jiansao.dispatch_event('click')
            with allure.step("勾选股方肌水肿"):
                logger.info(f"勾选股方肌水肿")
                self.tree_zuokuan_gufangji.click()
                self.check_gufangji_suizhong.dispatch_event('click')
        elif tree == '右髋':
            with allure.step("勾选坐骨间距减小"):
                logger.info(f"勾选坐骨间距减小")
                self.tree_youkuan_jiangu.click()
                self.check_jianju_jiansao.dispatch_event('click')
            with allure.step("勾选股方肌水肿"):
                logger.info(f"勾选股方肌水肿")
                self.tree_youkuan_gufangji.click()
                self.check_gufangji_suizhong.dispatch_event('click')

    def if_bansuizhong(self, ban_suizhong, jishu):
        if jishu == '1':
            if ban_suizhong == "No":
                with allure.step("勾选软骨软化I级"):
                    self.check_1ji.dispatch_event('click')
            else:
                with allure.step("勾选软骨软化I级，伴软骨下骨髓水肿"):
                    self.check_1ji_and.dispatch_event('click')
        elif jishu == '2':
            if ban_suizhong == "No":
                with allure.step("勾选软骨软化II级"):
                    self.check_2ji.dispatch_event('click')
            else:
                with allure.step("勾选软骨软化II级，伴软骨下骨髓水肿"):
                    self.check_2ji_and.dispatch_event('click')
        elif jishu == '3':
            if ban_suizhong == "No":
                with allure.step("勾选软骨软化III级"):
                    self.check_3ji.dispatch_event('click')
            else:
                with allure.step("勾选软骨软化III级，伴软骨下骨髓水肿"):
                    self.check_3ji_and.dispatch_event('click')
        elif jishu == '4':
            if ban_suizhong == "No":
                with allure.step("勾选软骨软化IV级"):
                    self.check_4ji.dispatch_event('click')
            else:
                with allure.step("勾选软骨软化IV级，伴软骨下骨髓水肿"):
                    self.check_4ji_and.dispatch_event('click')

    def if_kuang_select(self, tree, suntree, ban_suizhong, jishu):
        if tree == '双髋':
            if suntree == '双髋关节':
                with allure.step("点击双髋关节"):
                    logger.info(f"点击双髋关节")
                    self.tree_suangkuan_guanjie.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
            elif suntree == '髋臼关节面':
                with allure.step("点击髋臼关节面"):
                    logger.info(f"点击髋臼关节面")
                    self.tree_suangkuan_kuanjiu.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
            elif suntree == '股骨头关节面':
                with allure.step("点击股骨头关节面"):
                    logger.info(f"点击股骨头关节面")
                    self.tree_suangkuan_gugutou.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
        elif tree == '右髋':
            if suntree == '右髋关节':
                with allure.step("点击右髋关节"):
                    logger.info(f"点击右髋关节")
                    self.tree_youkuan_guanjie.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
            elif suntree == '髋臼关节面':
                with allure.step("点击髋臼关节面"):
                    logger.info(f"点击髋臼关节面")
                    self.tree_youkuan_kuanjiu.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
            elif suntree == '股骨头关节面':
                with allure.step("点击股骨头关节面"):
                    logger.info(f"点击股骨头关节面")
                    self.tree_youkuan_gugutou.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
        elif tree == '左髋':
            if suntree == '左髋关节':
                with allure.step("点击左髋关节"):
                    logger.info(f"点击左髋关节")
                    self.tree_zuokuan_guanjie.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
            elif suntree == '髋臼关节面':
                with allure.step("点击股骨关节面"):
                    logger.info(f"点击股骨关节面")
                    self.tree_zuokuan_kuanjiu.click()
                    self.if_bansuizhong(ban_suizhong, jishu)
            elif suntree == '股骨头关节面':
                with allure.step("点击股骨关节面"):
                    logger.info(f"点击股骨关节面")
                    self.tree_zuokuan_gugutou.click()
                    self.if_bansuizhong(ban_suizhong, jishu)

    def if_kuang_select_xingtai(self, tree, suntree):
        if tree == '双髋':
            if suntree == '髋臼':
                with allure.step("点击髋臼"):
                    logger.info(f"点击髋臼")
                    self.tree_suangkuan_kuanjiu_2.click()
                    self.check_baorong_guodu.dispatch_event('click')
            elif suntree == '股骨头':
                with allure.step("点击股骨头"):
                    logger.info(f"点击股骨头")
                    self.tree_suangkuan_gugutou_2.click()
                    self.check_waiyuan_penglong.dispatch_event('click')
        elif tree == '右髋':
            if suntree == '髋臼':
                with allure.step("点击髋臼"):
                    logger.info(f"点击髋臼")
                    self.tree_youkuan_kuanjiu_2.click()
                    self.check_baorong_guodu.dispatch_event('click')
            elif suntree == '股骨头':
                with allure.step("点击股骨头"):
                    logger.info(f"点击股骨头")
                    self.tree_youkuan_gugutou_2.click()
                    self.check_waiyuan_penglong.dispatch_event('click')
        elif tree == '左髋':
            if suntree == '髋臼':
                with allure.step("点击髋臼"):
                    logger.info(f"点击髋臼")
                    self.tree_zuokuan_kuanjiu_2.click()
                    self.check_baorong_guodu.dispatch_event('click')
            elif suntree == '股骨头':
                with allure.step("点击股骨头"):
                    logger.info(f"点击股骨头")
                    self.tree_zuokuan_gugutou_2.click()
                    self.check_waiyuan_penglong.dispatch_event('click')

    def page_click_ruangu_num_ji(self, tree, suntree, ban_suizhong, jishu):
        with allure.step("点击关节软骨及软骨下骨标签"):
            logger.info(f"点击关节软骨及软骨下骨")
            self.tab_guanjie_ruangu.click()
            self.if_kuang_select(tree, suntree, ban_suizhong, jishu)

    def page_click_gugu_kuanjiu_zhuangji_zonghezheng1(self, tree, suntree):
        with allure.step("点击关节形态标签"):
            logger.info(f"点击关节形态标签")
            self.tab_guanjie_xingtai.click()
            self.if_kuang_select_xingtai(tree, suntree)

    def page_add_report_kuan_zuangji(self, fangshe_bianhao, buweimingcheng, leibie, treename):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        self.page_check_gugu(treename)
        with allure.step("点击提交报告"):
            logger.info(f"点击提交报告")
            self.tijiao_report.click()
            self.page_bi_tian_assure.click()

    def page_add_report_kuan_tuixingxing_gaibian_1(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        self.page_click_ruangu_num_ji(treename, suntree, ban_suizhong, '1')
        self.page_tijiao_report()

    def page_add_report_kuan_tuixingxing_gaibian_2(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        self.page_click_ruangu_num_ji(treename, suntree, ban_suizhong, '2')
        self.page_tijiao_report()

    def page_add_report_kuan_tuixingxing_gaibian_3(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        self.page_click_ruangu_num_ji(treename, suntree, ban_suizhong, '3')
        self.page_tijiao_report()

    def page_add_report_kuan_tuixingxing_gaibian_4(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree, ban_suizhong):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        self.page_click_ruangu_num_ji(treename, suntree, ban_suizhong, '4')
        self.page_tijiao_report()

    def page_add_report_kuan_tuixingxing_gaibian_5(self, fangshe_bianhao, buweimingcheng, leibie, treename, suntree):
        self.add_simple_base_info(fangshe_bianhao, buweimingcheng, leibie)
        self.page_click_gugu_kuanjiu_zhuangji_zonghezheng1(treename, suntree)
        self.page_tijiao_report()