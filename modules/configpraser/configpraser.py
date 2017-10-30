# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 19:46
# @Author  : suliuer
# @File    : configpraser.py
# @Info    :

import configparser

config = configparser.ConfigParser()
config.read('example.txt', encoding='utf-8')

# 获取所有节点 ['global', 'public']
ret = config.sections()  # 读取配置文件里所有的"[]"信息
print(ret)

# 获取指定节点下的所有键值对 [('workgroup', 'WORKGROUP'), ('security', 'share'), ('maxlog', '50')]
ret = config.items('global')  # 获取指定节点的所有键值对
print(ret)

# 获取指定节点下的所有键 ['comment', 'public', 'pi']
ret = config.options('public')  # 指定节点下的所有键
print(ret)

# 获取指定节点下指定key的值
ret = config.get('global', 'workgroup')  # 获取指定节点下key的值
# ret = config.getint('global','maxlog')#获取指定节点下key值，必须为整数否则报错
# ret = config.getfloat('public','pi')#获取指定节点下key值，必须为浮点数否则报错
# ret = config.getboolean('public','public')#获取指定节点下key值，必须为布尔值否则报错
print(ret)

# 检查，添加，删除节点
# 检查
check = config.has_section('global')  # 检查此节点下是否有值，返回布尔值
print(check)
# 输出：
# True

# 添加节点
config.add_section('local')  # 添加到内存
config.write(open('example.txt', 'w'))  # 写入文件中
ret = config.sections()
print(ret)
# 输出：
# ['global', 'public', 'local']

# 删除节点
config.remove_section('local')  # 删除节点
config.write(open('example', 'w'))  # 重新写入文件
ret = config.sections()
print(ret)
# 输出：
# ['global', 'public']

# 检查，删除，设置指定组内的键值对
# 检查
check = config.has_option('public', 'comment')  # 检查节点下的某个键，返回布尔值
print(check)
# 输出:
# True

# 删除
config.remove_option('global', 'workgroup')
config.write(open('example.txt', 'w'))
ret = config.options('global')
print(ret)
# 输出：
# ['security', 'maxlog']


# 设置指定节点内的键值对
ret1 = config.get('global', 'maxlog')
print(ret1)
config.set('global', 'maxlog', '100')
config.write(open('example.txt', 'w'))
ret2 = config.get('global', 'maxlog')
print(ret2)

# 输出：
# 50
# 100
