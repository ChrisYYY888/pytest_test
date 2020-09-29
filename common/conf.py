# -*- coding: utf-8 -*-
import configparser
import os

project_path = os.path.dirname(os.path.dirname(__file__))
# 基础路径
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
# 导出、下载文件目录
export_path = project_path + '/testFile/export'
# 导入文件目录
template_path = project_path + '/testFile/import'


# 获取单个配置信息
def get_config(target_section, target_option):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(project_path, 'config.ini'), encoding='utf-8')
    r = cf.get(target_section, target_option)
    return r


# 获取单节配置信息
def get_config_section(target_section):
    cf = configparser.ConfigParser()
    cf.read(os.path.join(project_path, 'config.ini'), encoding='utf-8')
    return cf.items(target_section)


# 更新配置信息
def update_config(target_section, target_option, target_value):
    # 读取配置文件
    cf = configparser.ConfigParser()
    cf.read(os.path.join(project_path, 'config.ini'), encoding='utf-8')
    # 更新配置文件
    cf.set(target_section, target_option, target_value)
    # 循环写入
    with open(os.path.join(project_path, 'config.ini'), 'w', encoding='utf-8') as fw:
        cf.write(fw)


if __name__ == '__main__':
    pass
