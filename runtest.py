
import os
import pytest
import time
from allure_des.allure_des import set_report_env_on_results, \
    set_report_executer_on_results, \
    set_report_categories_on_results
from config.config import cm


def run():
    # pytest.main(['testcase/web/test_login/test_jiegouhuarreport_jing_zui_tui_bian.py', '-m', 'not old_feature', '--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['testcase/web/test_login/', '-m', 'not old_feature', '--alluredir=%s' % cm.dir_report_json, '--reruns=1', '--reruns-delay=2'])
    pytest.main([
        'testcases/',
        # '-m', 'titles',
        # '--lf',
        '--alluredir', cm.dir_report_json  # 分开作为两个列表元素
    ])
    # pytest.main(['testcase/web/test_login/', '-m', 'smoke','--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['testcase/web/test_login/', '-m', 'not old_feature', '--lf', '--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['testcase/web/test_login/', '-m', 'bug', '--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['testcase/web/test_login/', '-m', 'not old_feature', '--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['testcase/web/test_login/test_jiegouhuarreport.py', '-m', 'not old_feature', '--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['--allure-stories=文件上传成功', '--alluredir=%s' % cm.dir_report_json])
    # pytest.main(['--allure-stories=用户-启用状态查询成功', '--alluredir=%s' % cm.dir_report_json])
    # 在json目录下创建categories.json文件
    set_report_categories_on_results()
    # 在json目录下创建environment.properties文件
    set_report_env_on_results()
    # 在json目录下创建executor.json文件
    set_report_executer_on_results()
    time.sleep(3)
    os.system("allure generate %s -o %s --clean" % (cm.dir_report_json, cm.dir_report_html))


if __name__ == '__main__':
    run()

