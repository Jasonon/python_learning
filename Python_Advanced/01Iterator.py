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

# 2、迭代器模块itertools
# itertools包自带三个可以无限迭代的迭代器
# ①count(初值=0，步长=1)
from itertools import count
for i in count(10,2):
    if i > 20:
        break
    else:
        print(i)

# ②islice(遍历的对象，迭代次数)
from itertools import islice
for i in islice(count(10),5):
    print(i)

# ③cycle(可迭代对象)
from itertools import cycle
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1
