import allure
from utils.log import logger
from playwright.sync_api import Page
import re

class AddReportBasePage:
    def __init__(self, page: Page):
        self.page = page
        self.fsbh_input = self.page.get_by_role("textbox", name="* 放射编号")
        self.buweibingcheng = self.page.locator("div").filter(has_text=re.compile(r"^部位名称请选择$")).locator("span")
        self.xi = self.page.get_by_role("option", name="膝")
        self.kuan = self.page.get_by_role("option", name="髋")
        self.leibie = self.page.locator("div").filter(has_text=re.compile(r"^类别请选择$")).locator("span")
        self.tuibian = self.page.get_by_role("option", name="退变", exact=True)
        self.waishang = self.page.get_by_role("option", name="外伤", exact=True)
        self.tuibian_waishang = self.page.get_by_text("外伤合并退变")
        self.zuoxi = self.page.get_by_text("左膝")
        self.youxi = self.page.get_by_text("右膝")
        self.xi_select_assure = self.page.get_by_role("button", name="确认")



        #提交报告，确认按钮
        self.tijiao_report = self.page.get_by_role("button", name="提交报告")
        self.page_bi_tian_assure = self.page.get_by_role("button", name="确认")

        #报告内容
        self.impression = self.page.locator("div.impression-text.impressS")

    def buweibingcheng_select(self, buweibingcheng: str):
        self.buweibingcheng.click()
        if buweibingcheng == "膝":
            self.xi.click()
        elif buweibingcheng == "髋":
            self.kuan.click()


    def leibie_select(self, leibie: str):
        self.leibie.click()
        if leibie == "退变":
            self.tuibian.click()

    def xi_select(self, xibuwei=None):
        # self.zuoxi.click()
        if xibuwei == "左膝":
            self.zuoxi.click()
        elif xibuwei == "右膝":
            self.youxi.click()
        elif xibuwei is not None:
            raise ValueError(f"无效的膝部位参数: {xibuwei}")


    @allure.step("添加简单基本信息")
    def add_simple_base_info(self, fsbh: str, buweibingcheng: str, leibie: str, xibuwei=None):
        logger.info(f"添加简单基本信息：放射编号-{fsbh}，部位名称-{buweibingcheng}，类别-{leibie}，部位-{xibuwei}")
        self.fsbh_input.fill(fsbh)
        self.buweibingcheng_select(buweibingcheng)
        self.leibie_select(leibie)
        if xibuwei is not None:
            self.xi_select(xibuwei)
            self.xi_select_assure.click()

    def page_get_form_info_content(self):
        """获取印象信息文本内容"""
        self.impression.wait_for(state="visible")
        # 返回元素的文本内容
        return self.impression.inner_text()

    def page_tijiao_report(self):
        with allure.step("点击提交报告"):
            logger.info(f"点击提交报告")
            self.tijiao_report.click()
            self.page_bi_tian_assure.click()