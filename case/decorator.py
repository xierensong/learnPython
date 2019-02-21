import datetime
import functools

def log(func):   # 装饰器函数，参数是一个函数
    @functools.wraps(func)  # 将装饰器修饰过的函数wapper名字改成参数的名字
    def wapper(*args, **kw):    # wapper是装饰器函数，包含装饰的代码和调用被装饰函数的语句。
        print("I am in position.")   # 装饰的代码，比如日志打印
        func(*args, **kw)   # 原始的函数
    return wapper  # 返回装饰后的函数

@log    # 指定那个装饰器
def func():    # 被装饰的函数
    print(datetime.datetime.now())

def log1(text):   # 装饰器带参数
    def decorator(func):  # 中间多了一层函数定义
        @functools.wraps(func)   # 修改装饰函数名称为被装饰的函数名称
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))   # 在装饰器代码中使用了装饰器参数
            return func(*args, **kw)
        return wrapper
    return decorator

@log1("execute")  # 函数定义时指定参数
def func1():
    print(datetime.datetime.now())



func()   # 函数执行结果包含了装饰器新增的代码
print(func.__name__)   # 检查装饰后的函数名没被装饰中的中间函数影响


func1()   # 调用被装饰过的函数
print(func1.__name__)   # 检查装饰后的函数名没被装饰中的中间函数影响