#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pluggy
from pluggy import HookspecMarker
from pluggy import HookimplMarker

hookspec = HookspecMarker("myproject")
hookimpl = HookimplMarker("myproject")


class MySpec(object):
    """hook 集合"""
    @hookspec
    def myhook(self, arg1, arg2):
        pass
    @hookspec
    def my_hook_func1(self, arg1, arg2):
        pass
    @hookspec
    def my_hook_func2(self, arg1, arg2):
        pass


# 插件类
class Plugin_1(object):
    """hook实现类1"""
    @hookimpl
    def myhook(self, arg1, arg2):
        print("Plugin_1.myhook called")
        return arg1 + arg2

    @hookimpl
    def my_hook_func2(self, arg1, arg2):
        print("Plugin_1.my_hook_func2 called, args:", arg1, arg2)

    def my_hook_func3(self, arg1, arg2):
        print("Plugin_1.my_hook_func3 called, args:", arg1, arg2)


class Plugin_2(object):
    """hook实现类2"""
    @hookimpl
    def myhook(self, arg1, arg2):
        print("Plugin_2.myhook called")
        return arg1 - arg2

    @hookimpl
    def my_hook_func2(self, arg1, arg2):
        print("Plugin_2.my_hook_func2, args:", arg1, arg2)


# 初始化 PluginManager
pm = pluggy.PluginManager("myproject")
# 登记hook集合(hook函数声明)
pm.add_hookspecs(MySpec)
# 注册插件(hook函数实现)
pm.register(Plugin_1())
pm.register(Plugin_2())
# 调用自定义hook
results = pm.hook.myhook(arg1=1, arg2=2) # 调用两个插件类中的同名hook函数 # 后注册的插件中的函数会先被调用
print(results) # 输出 [-1, 3]
results = pm.hook.my_hook_func1(arg1="name", arg2="shouke")
print(results)
pm.hook.my_hook_func2(arg1="addr", arg2="sz")
