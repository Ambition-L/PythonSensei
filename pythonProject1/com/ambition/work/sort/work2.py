# 课后第一题

# 接受第一行数据 数组长度 和 显示长度
a = input("请输入数组长度：")

# 定义接收数据数组
nums = [0] * int(a)

# 定义输出数据角标数组
nums2 = [0] * int(a)

# 接收数据
for i in range(0, len(nums)):
    nums[i] = int(input("请输入第" + str(i + 1) + "个数："))


# 循环接收输出数据的角标 并放入数组
d = 0
# 最多输入数据不超过数组长度
while d < len(nums):
    num = int(input("请输入需要输出的第" + str(d + 1) + "个数位置，输入0结束："))
    # 如果输入0 结束循环
    if num == 0:
        break
    nums2[d] = num
    d += 1

# 数组转换
nums3 = [0] * d
for i in range(0, len(nums3)):
    nums3[i] = nums2[i]

# 排序 -- 插入排序
for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[j] > nums[i]:
            temp = nums[i]
            nums.pop(i)
            nums.insert(j, temp)

print(nums)

# 将用户输入的指定数据输出
for i in range(0, len(nums3)):
    print(nums[nums3[i] - 1])
