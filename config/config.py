"""
@File    : config.py
@Author  : Sarah
@Date    : 2023/7/10
@Desc    ：工程的文件目录，文件位置
"""

import os
# from utils.timer import dt_strftime

import datetime


class ConfigManager:
    """
    管理项目目录，文件
    """

    DIR_CURR = os.path.abspath(__file__)

    DIR_CONF = os.path.dirname(os.path.abspath(__file__))

    # 项目路径
    DIR_BASE = os.path.dirname(DIR_CONF)

    DIR_COMM = os.path.join(DIR_BASE, "common")

    DIR_UTIL = os.path.join(DIR_BASE, "utils")

    # 页面元素和页面对象路径
    DIR_PAGE = os.path.join(DIR_BASE, 'page_object')

    # 页面元素
    # DIR_ELEMENT = os.path.join(DIR_BASE, "page_element")

    # DIR_DRIVER = os.path.join(DIR_BASE, "driver")

    # @property
    # def web_ini_file(self):
    #     """ web 配置文件"""
    #     ini_file = os.path.join(self.DIR_CONF, 'web_cfg.ini')
    #     if not os.path.exists(ini_file):
    #         raise FileNotFoundError("配置文件%s不存在！" % ini_file)
    #     return ini_file
    #
    @property
    def dir_report_json(self):
        """allure报告目录 json文件"""
        report_dir = os.path.join(self.DIR_BASE, 'report')
        os.makedirs(report_dir, exist_ok=True)
        json_dir = os.path.join(report_dir, 'json')
        os.makedirs(json_dir, exist_ok=True)
        return json_dir

    @property
    def dir_report_html(self):
        """allure报告目录 html文件"""
        report_dir = os.path.join(self.DIR_BASE, 'report')
        os.makedirs(report_dir, exist_ok=True)
        html_dir = os.path.join(report_dir, 'html')
        os.makedirs(html_dir, exist_ok=True)
        return html_dir

    @property
    def dt_strftime(fmt="%Y%m"):
        """
        datetime格式化时间
        :param fmt “%Y%m%d %H%M%S
        """
        return datetime.datetime.now().strftime(fmt)

    @property
    def dir_log(self):
        """日志目录"""
        log_dir = os.path.join(self.DIR_BASE, 'logs')
        os.makedirs(log_dir, exist_ok=True)
        return log_dir
    #
    # @property
    # def log_file(self):
    #     """日志文件"""
    #     return os.path.join(self.dir_log, '{}.log'.format(dt_strftime()))
    #
    @property
    def dir_img(self):
        """截图目录"""
        img_dir = os.path.join(self.dir_log, 'screenshots')
        os.makedirs(img_dir, exist_ok=True)
        return img_dir
    #
    # @property
    # def img_file(self):
    #     """截图文件"""
    #     return os.path.join(self.dir_img, '{}.png'.format(dt_strftime('%Y%m%d%H%M%S')))
    #
    @property
    def dir_testdata(self):
        """测试数据目录"""
        test_data_dir = os.path.join(self.DIR_BASE, 'testdata')
        os.makedirs(test_data_dir, exist_ok=True)
        return test_data_dir

    @property
    def dir_web_testdata(self):
        """测试数据目录-web"""
        test_data_dir = os.path.join(self.dir_testdata, 'web')
        os.makedirs(test_data_dir, exist_ok=True)
        return test_data_dir

    @property
    def test_web_yaml_file(self):
        """ 测试数据文件.yaml """
        yaml_file = os.path.join(self.dir_web_testdata, 'test_data.yaml')
        if not os.path.exists(yaml_file):
            raise FileNotFoundError("测试数据文件%s不存在！" % yaml_file)
        return yaml_file
    #
    # @property
    # def test_web_yaml_file_login(self):
    #     """ 测试数据文件.yaml """
    #     yaml_file = os.path.join(self.dir_web_testdata, 'login.yaml')
    #     if not os.path.exists(yaml_file):
    #         raise FileNotFoundError("测试数据文件%s不存在！" % yaml_file)
    #     return yaml_file
    #
    # @property
    # def test_web_yaml_file_user(self):
    #     """ 测试数据文件.yaml """
    #     yaml_file = os.path.join(self.dir_web_testdata, 'user.yaml')
    #     if not os.path.exists(yaml_file):
    #         raise FileNotFoundError("测试数据文件%s不存在！" % yaml_file)
    #     return yaml_file
    #
    # @property
    # def test_web_yaml_file_role(self):
    #     """ 测试数据文件.yaml """
    #     yaml_file = os.path.join(self.dir_web_testdata, 'role.yaml')
    #     if not os.path.exists(yaml_file):
    #         raise FileNotFoundError("测试数据文件%s不存在！" % yaml_file)
    #     return yaml_file
    #
    # @property
    # def test_web_json_file(self):
    #     """ 测试数据文件.json """
    #     json_file = os.path.join(self.dir_web_testdata, 'test_data.json')
    #     if not os.path.exists(json_file):
    #         raise FileNotFoundError("测试数据文件%s不存在！" % json_file)
    #     return json_file

    # @property
    # def web_driver(self):
    #     """浏览器驱动"""
    #     os.makedirs(self.DIR_DRIVER, exist_ok=True)
    #     driver = os.path.join(self.DIR_DRIVER, 'chromedriver.exe')
    #     if not os.path.exists(driver):
    #         raise FileNotFoundError("浏览器驱动%s不存在！" % driver)
    #     return driver


cm = ConfigManager()
