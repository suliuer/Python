# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 19:36
# @Author  : suliuer
# @File    : 贪婪模式.py
# @Info    : 默认贪婪模式，加？非贪婪模式
import re

content = 'Hello 1234567 Wodld_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))

result2 = re.match('He.*?(\d+).*Demo$', content)
print(result2)
print(result2.group(1))