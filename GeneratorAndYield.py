# 什么是Generator 通过next,是一个迭代器
# 怎么用
import memory_profiler as mem # 内存监控
import time
nums=[1,2,3,4,5,6]
# squre_nums=[n**2 for n in nums]
squre_nums=(n**2 for n in nums)
# 把[]换成()就是Generator
print(next(squre_nums)) # for 本质上就是不断的调用next
print(next(squre_nums)) # for 本质上就是不断的调用next
print(next(squre_nums)) # for 本质上就是不断的调用next
print(next(squre_nums)) # for 本质上就是不断的调用next
print(next(squre_nums)) # for 本质上就是不断的调用next
print(next(squre_nums)) # for 本质上就是不断的调用next
try:
    print(len(squre_nums))
except TypeError as e:
    print("格式有问题") # Generator是一个生成器，能生成一个个东西

# for i in squre_nums:
#     print(i)


yi=100000000
time1=time.time()
mem1=mem.memory_usage()
# 数量变大时,使用列表
nums1=list(range(yi))
squre_nums1=[n**3 for n in nums1]
time2=time.time()
mem2=mem.memory_usage()
print(f"时间使用{time2-time1}")
print(f"内存使用{mem2[0]-mem1[0]}")
# 使用迭代器
nums2=list(range(yi))
squre_nums2=(n**3 for n in nums2)
time3=time.time()
mem3=mem.memory_usage()
print(f"时间使用{time3-time2}")
print(f"内存使用{mem3[0]-mem2[0]}")

# 所以列表中的数据是真的生成了,而在生成器中只是生成了生成器,每当需要数字的时候调用这个生成器