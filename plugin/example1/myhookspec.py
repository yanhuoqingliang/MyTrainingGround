import pluggy

hookspec = pluggy.HookspecMarker("myproject")  # hook 标签 用于标记hook
hookimpl = pluggy.HookimplMarker("myproject")  # hook 实现标签 用于标记hook的一个或多个实现


@hookspec
def global_hook_func1(arg1, arg2):
    pass