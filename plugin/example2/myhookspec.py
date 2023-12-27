import pluggy

hookspec = pluggy.HookspecMarker("myproject")


@hookspec
def mytest_hook_func1(arg1, arg2):
    pass