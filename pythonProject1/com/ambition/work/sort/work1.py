## 课后练习第一题

# 接受第一行数据 数组长度 和 显示长度
a = input("请输入数组长度：")
b = input("显示长度：")

# 初始化存储用户输入数组 int(a) 表示将字符串转为int类型 因为input函数接收的是字符串
nums = [0] * int(a)
# 初始化显示数组
nums2 = [0] * int(b)

# 循环接受用户输入数据并放入数组
for i in range(0, int(a)):
    print("请输入第 " + str(i + 1) + "个数:")
    nums[i] = int(input())

# 排序
for i in range(0, len(nums)):
    min = i
    for j in range(i, len(nums)):
        if nums[j] < nums[min]:
            min = j
    temp = nums[min]
    nums.pop(min)
    nums.insert(i, temp)
print(nums)

# 排序好的数组数据放入用户想要看到长度的数组中
for i in range(0, len(nums2)):
    nums2[i] = nums[i]

# 输出数组
print(nums2)
