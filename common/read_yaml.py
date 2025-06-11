
import yaml
from config.config import cm


class ReadYaml:

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self, key):
        arr = []
        with open(self.yaml_file, 'r', encoding='utf-8') as f:
            datas = yaml.load(f, Loader=yaml.FullLoader)  # 避免报警告，需要加入Loader=yaml.FullLoader
            value = datas[key]
            for data in value:
                arr.append(tuple(data.values())[1:])
            return arr

yaml_para = ReadYaml(cm.test_web_yaml_file)

new_report_title_4_1 = yaml_para.read_yaml('new_report_title_4_1')
new_report_title_kuan_1 = yaml_para.read_yaml('new_report_title_kuan_1')
new_report_title_kuan_2 = yaml_para.read_yaml('new_report_title_kuan_2')
new_report_title_kuan_3 = yaml_para.read_yaml('new_report_title_kuan_3')
new_report_title_kuan_4 = yaml_para.read_yaml('new_report_title_kuan_4')
new_report_title_kuan_5 = yaml_para.read_yaml('new_report_title_kuan_5')
new_report_title_kuan_6 = yaml_para.read_yaml('new_report_title_kuan_6')
new_report_bi_tian_title1 = yaml_para.read_yaml('new_report_bi_tian_title1')
new_report_bi_tian_title2 = yaml_para.read_yaml('new_report_bi_tian_title2')
new_report_bi_tian_title3 = yaml_para.read_yaml('new_report_bi_tian_title3')

new_report_title_jian_1 = yaml_para.read_yaml('new_report_title_jian_1')
new_report_title_jian_2 = yaml_para.read_yaml('new_report_title_jian_2')
new_report_title_jian_3 = yaml_para.read_yaml('new_report_title_jian_3')

new_report_title_jian_wai_shang_1 = yaml_para.read_yaml('new_report_title_jian_wai_shang_1')
new_report_title_jian_wai_shang_2 = yaml_para.read_yaml('new_report_title_jian_wai_shang_2')
new_report_title_jian_wai_shang_3 = yaml_para.read_yaml('new_report_title_jian_wai_shang_3')
new_report_title_jian_wai_shang_4 = yaml_para.read_yaml('new_report_title_jian_wai_shang_4')

new_report_title_huai_wai_shang_1 = yaml_para.read_yaml('new_report_title_huai_wai_shang_1')
new_report_title_huai_wai_shang_2 = yaml_para.read_yaml('new_report_title_huai_wai_shang_2')
new_report_title_huai_wai_shang_3 = yaml_para.read_yaml('new_report_title_huai_wai_shang_3')
new_report_title_huai_wai_shang_4 = yaml_para.read_yaml('new_report_title_huai_wai_shang_4')

new_report_title_wan_tuibian_1 = yaml_para.read_yaml('new_report_title_wan_tuibian_1')
new_report_title_wan_tuibian_2 = yaml_para.read_yaml('new_report_title_wan_tuibian_2')
new_report_title_wan_tuibian_3 = yaml_para.read_yaml('new_report_title_wan_tuibian_3')
new_report_title_wan_tuibian_4 = yaml_para.read_yaml('new_report_title_wan_tuibian_4')
new_report_title_wan_tuibian_5 = yaml_para.read_yaml('new_report_title_wan_tuibian_5')
new_report_title_wan_tuibian_6 = yaml_para.read_yaml('new_report_title_wan_tuibian_6')
new_report_title_wan_tuibian_7 = yaml_para.read_yaml('new_report_title_wan_tuibian_7')
new_report_title_wan_tuibian_8 = yaml_para.read_yaml('new_report_title_wan_tuibian_8')
new_report_title_wan_tuibian_9 = yaml_para.read_yaml('new_report_title_wan_tuibian_9')