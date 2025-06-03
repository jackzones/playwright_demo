import allure
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
        self.leibie = self.page.locator("div").filter(has_text=re.compile(r"^类别请选择$")).locator("span")
        self.tuibian = self.page.get_by_role("option", name="退变", exact=True)
        self.gugutou_huaisi = self.page.get_by_role("option", name="股骨头坏死")
        self.waishang = self.page.get_by_role("option", name="外伤", exact=True)
        self.tuibian_waishang = self.page.get_by_text("外伤合并退变")
        self.zuoxi = self.page.get_by_text("左膝")
        self.youxi = self.page.get_by_text("右膝")
        self.zuojian = self.page.get_by_text("左肩")
        self.youjian = self.page.get_by_text("右肩")
        self.xi_select_assure = self.page.get_by_role("button", name="确认")

        #提交报告，确认按钮
        self.tijiao_report = self.page.get_by_role("button", name="提交报告")
        self.page_bi_tian_assure = self.page.get_by_role("button", name="确认")

        #漏诊
        self.louzhen_assure_text = self.page.locator("//div[@class='el-dialog__body']//div").first

        #弹出的标题选择
        self.select_title = self.page.locator("//header[@class='el-dialog__header']/span[@class='el-dialog__title']")
        self.title_ok_btn = self.page.locator("//div[@class='el-overlay']//button[1]")

        #报告内容
        self.yingxiangxue_bianxian = self.page.locator("//div[@class='impression-text']")
        self.impression = self.page.locator("//div[@class='impression-text impressS']")
        self.impression_rule_title = self.page.locator("//span[@class='rule_title']")


    def buweimingcheng_select(self, buweimingcheng: str):
        self.buweimingcheng.click()
        if buweimingcheng == "膝":
            self.xi.click()
        elif buweimingcheng == "髋":
            self.kuan.click()
        elif buweimingcheng == "肩":
            self.jian.click()

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

    def xi_select(self, xibuwei=None):
        if xibuwei == "左膝":
            self.zuoxi.click()
        elif xibuwei == "右膝":
            self.youxi.click()
        elif xibuwei == "左肩":
            self.zuojian.click()
        elif xibuwei == "右肩":
            self.youjian.click()
        elif xibuwei is not None:
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

    def page_get_form_info_content(self):
        """获取印象信息文本内容"""
        self.impression.wait_for(state="visible")
        # 返回元素的文本内容
        return self.impression.inner_text()

    def page_get_form_info_rule_title(self):
        """获取印象信息-标题"""
        self.impression_rule_title.wait_for(state="visible")
        return self.impression_rule_title.inner_text()

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

    def page_get_form_info_content_title(self):
        """印象信息 标题"""
        self.impression.wait_for(state="visible")
        return self.impression_rule_title.inner_text()

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
            assert False, f"字符串不匹配，差异如下:\n{diff_text}"
        return True