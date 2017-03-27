# 1、迭代器的介绍
a = iter([1,2,3])
print(a)
try:
	print(a.__next__())
	print(a.__next__())
	print(a.__next__())
	print(a.__next__())
except StopIteration:
	print('遍历完毕')

# # 一、无限迭代器
# 2、迭代器模块itertools
# itertools包自带三个可以无限迭代的迭代器
print('①count(初值=0，步长=1)')
from itertools import count
for i in count(10,2):
    if i > 20:
        break
    else:
        print(i)

print('②islice(遍历的对象，迭代次数)')
from itertools import islice
for i in islice(count(10),5):
    print(i)

print('③cycle(可迭代对象)')
from itertools import cycle
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1

print('④repeat(对象[，次数])')
# repeat 迭代器会一遍遍地返回传入的对象直至永远，除非你设定了 times 参数。
from itertools import repeat
iterator = repeat(5,5)
try:
    for i in range(10):
        print(iterator.__next__())
except Exception as e:
    print('迭代完毕')
else:
    pass
finally:
    pass

# # 二、可终止的迭代器
# 1、accumulate(可迭代对象[, 函数])
# 2、chain.from_iterable(可迭代对象)
# 3、compress(数据, 选择器)
# 4、dropwhile(断言, 可迭代对象)
# 5、filterfalse(断言, 可迭代对象)
# 6、groupby(可迭代对象, 键=None)
。。。。。。