from myhookspec import hookimpl


@hookimpl
def global_hook_func1(arg1, arg2):
    print("global_hook_func1 in other.py, args:", arg1, arg2)
    return "other.py"