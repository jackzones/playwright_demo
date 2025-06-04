import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1920,"height":1080})
    page = context.new_page()
    page.goto("http://192.168.1.104:9104/login")
    page.get_by_role("textbox", name="* 账号").click()
    page.get_by_role("textbox", name="* 账号").fill("admin")
    page.get_by_role("textbox", name="* 账号").press("Tab")
    page.get_by_role("textbox", name="* 密码").fill("User123456")
    page.get_by_role("textbox", name="* 密码").press("Enter")
    page.get_by_role("button", name="结构化报告").click()
    page.get_by_role("textbox", name="* 放射编号").click()
    page.get_by_role("textbox", name="* 放射编号").fill("444")
    page.locator("div:nth-child(7) > .el-form-item__content > .el-select > .el-select__wrapper > .el-select__selection > div:nth-child(2)").click()
    page.get_by_role("option", name="肩").click()
    page.locator("div").filter(has_text=re.compile(r"^类别请选择$")).locator("span").click()
    page.get_by_role("option", name="退变", exact=True).click()
    page.get_by_role("button", name="确认").click()
    page.get_by_text("肩峰下脂肪间隙").click()
    page.get_by_role("row", name="狭窄").locator("span").nth(1).click()
    page.get_by_text("骨质").click()
    page.get_by_text("肩胛骨肩峰下缘").click()
    page.get_by_role("row", name="骨质增生 骨质增生，骨髓未见明显异常信号影 查看").locator("span").nth(1).click()
    page.get_by_text("肩袖", exact=True).click()
    page.get_by_text("肩袖部", exact=True).first.click()
    page.get_by_role("row", name="局部全层撕裂IV").locator("span").nth(1).click()
    page.get_by_role("button", name="提交报告").click()
    page.get_by_role("button", name="确认").click()
    expect(page.get_by_text("左肩肩峰下撞击综合征")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
