# TODO:
# print('1024 * 768 = ',1024*768)
# import math
#
#
# def quadratic(a, b, c):
#     x = (-b + math.sqrt(b**2-4*a*c)) / (2*a*c)
#     y = (-b - math.sqrt(b**2-4*a*c)) / (2*a*c)
#     return x, y
#
# print(quadratic(1,2,1))


# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s


# def findMinAndMax(L):
#     if len(L)==0:
#         return None,None
#     else:
#         (min,max)=(L[0],L[0])
#         for x in L:
#             if max<x:
#                 max=x
#             if min>x:
#                 min=x
#         return min,max
#
#
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-5, 6, abs))

# def normalize(name):
#     for i in name:
#         name = name.lower()
#     new_name = name[0].upper() + name[1:]
#     return new_name
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce
#
# def prod(L):
#     num = reduce(lambda x,y:x*y,L)
#     return num
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# from functools import reduce
#
# def str2float(s):
#     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     i=s.index('.')
#     s=s.replace('.','')
#     def num(x):
#         return DIGITS[x]
#     return reduce(lambda x, y: x*10+y, map(num, s))/10**(len(s)-i)
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
#
# def is_palindrome(n):
#     s = str(n) # 将数字转换为字符串
#     print(s[::-1])
#     return s == s[::-1]
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(t):
#     return t[0]
# def by_score(t):
#     return t[1]
#
# L2 = sorted(L, key=by_name)
# print(L2)

# def createCounter():
#     x = 0
#     def counter():
#         nonlocal x
#         x += 1
#         return x
#     return counter
#
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')



# L = list(filter(lambda x:x%2==1, range(1, 20)))
#
# print(L)

# import time, functools
#
#
# def metric(fn):
#     if callable(fn):  # 判断传入的参数是否是函数
#         return metric('call')(fn)  # 如果是函数, 则调用metric('call')(fn)函数
#
#     def decorator(func):  # 定义一个装饰器函数
#         @functools.wraps(func)  # 使用functools.wraps(func)装饰器, 将原函数的元信息复制到装饰器函数上
#         def wrapper(*args, **kw):  # 定义一个包装函数
#             exec_time_s = time.time()  # 获取当前时间
#             result = func(*args, **kw)  # 调用原函数
#             exec_time_e = time.time() - exec_time_s  # 计算执行时间
#             print('%s, %s executed in %s ms' % (fn, func.__name__, exec_time_e))  # 打印执行时间
#             return result  # 返回原函数的执行结果
#
#         return wrapper  # 返回包装函数
#
#     return decorator  # 返回装饰器函数
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# @metric('execute')
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print('测试成功!')


