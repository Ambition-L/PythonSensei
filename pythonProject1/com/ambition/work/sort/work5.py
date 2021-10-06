# 课后第三题
# n个数据
a = input("请输入n：")

# 初始化存储用户输入数组 int(a) 表示将字符串转为int类型 因为input函数接收的是字符串
nums = [0] * int(a)

# 循环接受用户输入数据并放入数组
for i in range(0, int(a)):
    print("请输入第 " + str(i + 1) + "个数:")
    nums[i] = int(input())

# 桶排序 相同的数据放在同一个桶中 那么当前坐标的桶就是最小坐标 输出即可
result = []
minv, maxv = min(nums), max(nums)
countn = [0] * (maxv - minv + 1)
for i in nums:
    # 调整角标
    countn[i - minv] += 1
for i in range(0, len(countn)):
    if countn[i]:
        result += [i + minv] * countn[i]

print(result)
