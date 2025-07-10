from time import sleep
import allure
from playwright.sync_api import expect
from utils.log import logger
from playwright.sync_api import Page
import re
import difflib

class AddReportBasePage:
    def __init__(self, page: Page):
        self.page = page
        self.fsbh_input = self.page.get_by_role("textbox", name="* 放射编号")
        self.buweimingcheng = self.page.locator("div").filter(has_text=re.compile(r"^部位名称请选择$")).locator("span")
        self.xi = self.page.get_by_role("option", name="膝")
        self.kuan = self.page.get_by_role("option", name="髋")
        self.jian = self.page.get_by_role("option", name="肩")
        self.huai = self.page.get_by_role("option", name="踝")
        self.wan = self.page.get_by_role("option", name="腕")
        self.buwei_lable = self.page.locator("ul.el-scrollbar__view.el-select-dropdown__list").nth(1)
        self.leibie_lable = self.page.locator("ul.el-scrollbar__view.el-select-dropdown__list").nth(2)
        # self.leibie = self.page.locator("div").filter(has_text=re.compile(r"^类别请选择$")).locator("span")
        self.leibie = self.page.locator("div:nth-child(8) > .el-form-item__content > .el-select > .el-select__wrapper > .el-select__selection > div:nth-child(2)")
        self.tuibian = self.page.get_by_role("option", name="退变", exact=True)
        self.gugutou_huaisi = self.page.get_by_role("option", name="股骨头坏死")
        self.waishang = self.page.get_by_role("option", name="外伤", exact=True)
        self.tuibian_waishang = self.page.get_by_text("外伤合并退变")
        self.zuoxi = self.page.get_by_text("左膝")
        self.youxi = self.page.get_by_text("右膝")
        self.zuojian = self.page.locator("label").filter(has_text="左肩").locator("span").nth(1)
        self.youjian = self.page.locator("label").filter(has_text="右肩").locator("span").nth(1)
        self.zuohuai = self.page.locator("label").filter(has_text="左踝").locator("span").nth(1)
        self.youhuai = self.page.locator("label").filter(has_text="右踝").locator("span").nth(1)
        self.zuowan = self.page.locator("label").filter(has_text="左腕").locator("span").nth(1)
        self.youwan = self.page.locator("label").filter(has_text="右腕").locator("span").nth(1)
        self.jingzui = self.page.get_by_text("颈椎")
        self.xiongzui = self.page.get_by_text("胸椎")

        self.xi_select_assure = self.page.get_by_role("button", name="确认")

        #提交报告，确认按钮
        self.tijiao_report = self.page.get_by_role("button", name="提交报告")
        self.page_bi_tian_assure = self.page.get_by_role("button", name="确认")

        #漏诊
        self.louzhen_assure_text = self.page.locator("//div[@class='el-dialog__body']//div").first

        #弹出的标题选择
        self.select_title = self.page.locator("//header[@class='el-dialog__header']/span[@class='el-dialog__title']")
        self.title_ok_btn = self.page.get_by_role("button", name="确认")

        #报告内容
        self.yingxiangxue_bianxian = self.page.locator("//div[@class='impression-text']")
        self.impression = self.page.locator("//div[@class='impression-text impressS']")
        self.yingxiangxue_bianxian_copy_button = self.page.locator('button.copy_btn').first
        self.yinxiang_copy_button = self.page.locator('button.copy_btn').nth(1)


        ##上、下标题
        self.top_title = self.page.locator('div.impression-text.impressS span.rule_title').first
        self.second_title = self.page.locator('div.impression-text.impressS span.rule_title').nth(1)
        self.third_title = self.page.locator('div.impression-text.impressS span.rule_title').nth(2)

        self.pop_tips = self.page.locator('p.el-message__content').first


    def buweimingcheng_select(self, buweimingcheng: str):
        self.buweimingcheng.click()
        if buweimingcheng == "膝":
            self.xi.click()
        elif buweimingcheng == "髋":
            self.kuan.click()
        elif buweimingcheng == "肩":
            self.jian.click()
        elif buweimingcheng == "踝":
            self.huai.click()
        elif buweimingcheng == "腕":
            self.wan.click()
        elif buweimingcheng == "颈椎":
            self.jingzui.click()
        elif buweimingcheng == "胸椎":
            self.xiongzui.click()
        else:
            logger.error(f"无效的数据参数: {buweimingcheng}")
            raise ValueError(f"无效的部位参数: {buweimingcheng}")  # 抛出异常


    def leibie_select(self, leibie: str):
        self.leibie.click()
        if leibie == "退变":
            self.tuibian.click()
        elif leibie == "股骨头坏死":
            self.gugutou_huaisi.click()
        elif leibie == "外伤":
            self.waishang.click()
        elif leibie == "外伤合并退变":
            self.tuibian_waishang.click()
        else:
            logger.error(f"无效的数据参数: {leibie}")
            raise ValueError(f"无效的部位参数: {leibie}")

    def xi_select(self, xibuwei=None):
        if xibuwei == "左膝":
            self.zuoxi.click()
        elif xibuwei == "右膝":
            self.youxi.click()
        elif xibuwei == "左肩":
            self.zuojian.click()
        elif xibuwei == "右肩":
            self.youjian.click()
        elif xibuwei == "左踝":
            self.zuohuai.click()
        elif xibuwei == "右踝":
            self.youhuai.click()
        elif xibuwei == "左腕":
            self.zuowan.click()
        elif xibuwei == "右腕":
            self.youwan.click()
        elif xibuwei is not None:
            logger.error(f"无效的数据参数: {xibuwei}")
            raise ValueError(f"无效的部位参数: {xibuwei}")

    @allure.step("添加简单基本信息")
    def add_simple_base_info(self, fsbh: str, buweimingcheng: str, leibie: str, xibuwei=None):
        logger.info(f"添加简单基本信息：放射编号-{fsbh}，部位名称-{buweimingcheng}，类别-{leibie}，部位-{xibuwei}")
        self.fsbh_input.fill(fsbh)
        self.buweimingcheng_select(buweimingcheng)
        self.leibie_select(leibie)
        if xibuwei is not None:
            self.xi_select(xibuwei)
            self.xi_select_assure.click()

    @allure.step("只添加放射编号")
    def add_simple_base_info_only_fsbh(self, fsbh: str):
        logger.info(f"添加简单基本信息：放射编号-{fsbh}")
        self.fsbh_input.fill(fsbh)

    @allure.step("只添加放射编号和部位-颈椎")
    def add_simple_base_info_without_leibie(self, fsbh: str):
        logger.info(f"添加简单基本信息：放射编号-{fsbh}, 部位名称-颈椎")
        self.fsbh_input.fill(fsbh)
        self.buweimingcheng_select('颈椎')

    def page_get_form_info_content(self):
        """获取印象信息文本内容"""
        self.impression.wait_for(state="visible")
        # 返回元素的文本内容
        return self.impression.inner_text()

    def page_get_form_info_rule_title_top(self):
        """获取印象信息-上标题"""
        #读出的文本无冒号，所以暂时不用此接口
        self.top_title.wait_for(state="visible")
        return self.top_title.inner_text()

    def page_get_form_info_rule_title_bottom(self):
        """获取印象信息-下标题"""
        self.second_title.wait_for(state="visible")
        return self.second_title.inner_text()

    def page_get_form_info_rule_title_third(self):
        """获取印象信息-下标题"""
        self.third_title.wait_for(state="visible")
        return self.third_title.inner_text()

    def page_tijiao_report(self):
        with allure.step("点击提交报告"):
            logger.info(f"点击提交报告")
            self.tijiao_report.click()
            self.page_bi_tian_assure.click()

    def page_tijiao_report_without_bitian(self):
        with allure.step("点击提交报告"):
            logger.info(f"点击提交报告")
            self.tijiao_report.click()

    def page_get_form_info_louzhen(self):
        with allure.step("查看漏诊提示"):
            logger.info(f"查看漏诊提示")
            self.louzhen_assure_text.wait_for(state="visible")
            return self.louzhen_assure_text.inner_text()

    def page_get_form_info_impression_text(self):
        """影像学表现"""
        self.yingxiangxue_bianxian.wait_for(state="visible")
        return self.yingxiangxue_bianxian.inner_text()

    def assert_str_equal(self, actual, expected):
        """比较两个字符串并高亮显示差异"""
        if actual != expected:
            diff = difflib.ndiff(expected.splitlines(keepends=True),
                                 actual.splitlines(keepends=True))
            diff_text = ''.join(diff)
            logger.error(f"字符串不匹配，差异如下:\n{diff_text}")
            logger.error(f"字符串不匹配，实际值如下:\n{actual}")
            logger.error(f"字符串不匹配，期望值如下:\n{expected}")
            assert False, f"字符串不匹配，差异如下:\n{diff_text} \n 实际值：{actual} \n 期望值：{expected}"
        return True

    def page_pop_tips(self):
        """获取第一个message"""
        self.pop_tips.wait_for(state="visible")
        return self.pop_tips.inner_text()

    def get_clipboard_text(self):
        """获取剪贴板文本"""
        return self.page.evaluate("() => navigator.clipboard.readText()")


    def get_yingxiangxue_biaoxian_clipboard_text(self):
        """获取影像表现-复制按钮"""
        with allure.step("点击复制按钮-获取影像学表现"):
            logger.info(f"点击复制按钮-获取影像学表现")
            self.yingxiangxue_bianxian_copy_button.wait_for(state="visible")
            self.page.context.grant_permissions(['clipboard-read', 'clipboard-write']) #复制权限
            self.yingxiangxue_bianxian_copy_button.click()
            print(repr(self.get_clipboard_text()))
            return self.get_clipboard_text()


    def get_yinxiang_clipboard_text(self):
        """获取影像表现-复制按钮"""
        with allure.step("点击复制按钮-获取印象"):
            logger.info(f"点击复制按钮-获取印象")
            self.yinxiang_copy_button.wait_for(state="visible")
            self.page.context.grant_permissions(['clipboard-read', 'clipboard-write'])  # 复制权限
            self.yinxiang_copy_button.click()
            return self.get_clipboard_text()
