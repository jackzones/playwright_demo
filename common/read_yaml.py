
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
