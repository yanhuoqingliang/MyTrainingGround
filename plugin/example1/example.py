#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import pluggy
import myhookspec
import myhookimpl
import other

# 初始化 PluginManager
pm = pluggy.PluginManager("myproject")

# 登记hook集合
pm.add_hookspecs(myhookspec)

# 登记hook的实现
pm.register(myhookimpl) # 插件也可以是模块
pm.register(other)

print(pm.hook.global_hook_func1(arg1="name", arg2="shouke"))