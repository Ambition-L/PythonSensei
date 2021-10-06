# 课后练习 第四题 优化版 （使用桶排序）

# 接收n，m n行数 m 列数
a = int(input("请输入n："))
b = int(input("请输入m："))

# 接收a，b 操作坐标
x = int(input("请输入a："))
y = int(input("请输入b："))

# 定义接收数据数组
nums = [0] * (a * b)

# 遍历接收 (这里将n行m列数据全部放在一个数组里)
for i in range(a * b):
    print("请输入第 " + str(i + 1) + "个数: ")
    nums[i] = int(input())

# 计算 a，b 角标在数组中的位置 取出 a，b坐标值 （计算方式为 坐标行数*列数 - （列数 - 坐标列数））
lens = (x * b) - (b - y) - 1
keyAb = nums[lens]

# 输出数组查看数据 和角标
print(nums)
print(keyAb)

# 定义存储 a行 b列数组 （十字架框选的数据）
nums2 = [0] * (a + b)

# 定义获取y列数据的角标 因为存储在一个数组中所以要单独计算a行b列 在数组中的位置并取出来放入新的数组
index = 0
for i in range(len(nums2)):
    # 取出a行数据
    if i <= a:
        nums2[i] = nums[((x - 1) * b) + i]
    else:
        # 取出b列数据
        nums2[i] = nums[(y - 1) + index]
        index += b

print(nums2)

# 寻找数组中的最大值和最小值
minv,maxv = min(nums2), max(nums2)

# 缺人桶大小
countn = [0] * (maxv - minv + 1)

count = 0

# 统计每个数出现的次数
for i in nums2:
    # 调整最小值位置
    countn[i - minv] += 1
print(countn)

# 取出桶内的数据 当取出的数据与目标a，b坐标相等时 则结束 并输出当前位置
# 桶排序 相同的数据放在同一个桶中 那么当前坐标的桶就是最小坐标 输出即可
for i in range(len(countn)):
    # 如果遍历到a，b坐标值 结束循环
    if i + 1 == keyAb:
        count += 1
        break
    # 当桶中有数据时 记录 +1
    if countn[i] != 0:
        count += 1

print(count)
