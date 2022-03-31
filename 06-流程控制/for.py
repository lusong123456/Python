import random
from line_profiler import LineProfiler
from functools import wraps


# 查询接口中每行代码执行的时间
def func_line_time(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        func_return = f(*args, **kwargs)
        lp = LineProfiler()
        lp_wrap = lp(f)
        lp_wrap(*args, **kwargs)
        lp.print_stats()
        return func_return

    return decorator


a = [1,2,3,4,5,6,7,8,9]
for i in a:
    if i %3==0:
        print(i)
        a.remove(i)