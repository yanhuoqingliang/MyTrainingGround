#!/usr/bin/env python
# -*- coding:utf-8 -*-

import inspect
import pluggy
import myhookspec
import other


class PytestPluginManager(pluggy.PluginManager):
    """
    插件类，实现不用@HookimplMarkerInstance装饰的函数也可以当做函数体
    """

    def parse_hookimpl_opts(self, plugin, name):
        # 规定免@hookimpl装饰的 hooks 函数总是以 mytest_打头，这样以避免访问非可读属性

        if not name.startswith("mytest_"):
            return

        method = getattr(plugin, name)
        opts = super().parse_hookimpl_opts(plugin, name)

        # 考虑hook只能为函数(consider only actual functions for hooks)
        if not inspect.isroutine(method):
            return

        # 收集未被标记的，以mytest打头的hook函数，(collect unmarked hooks as long as they have the `pytest_' prefix)
        if opts is None and name.startswith("mytest_"):
            opts = {}
        return opts


# 初始化 PluginManager
pm = PytestPluginManager("myproject")

# 登记hook集合
pm.add_hookspecs(myhookspec)

# 登记hook的实现
pm.register(other)

pm.hook.mytest_hook_func1(arg1="addr", arg2="sz")