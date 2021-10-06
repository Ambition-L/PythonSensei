### 课后练习 第四题

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

# 计算 a，b 角标在数组中的位置 取出 a，b坐标值
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

# 将十字架数组进行排序 (快排)
def quitSort(num1):
    if len(num1) <= 1:
        return num1

    mid = int(len(num1) / 2)
    llist, rlist = quitSort(num1[:mid]), quitSort(num1[mid:])

    result = []
    left, right = 0, 0
    while left < len(llist) and right < len(rlist):
        if llist[left] < rlist[right]:
            result.append(llist[left])
            left += 1
        else:
            result.append(rlist[right])
            right += 1

    result += llist[left:] + rlist[right:]
    return result

# 排序好的数组
nums3 = quitSort(nums2)
print(nums3)

k = len(nums3)
j = 0
# 将比a，b坐标小的数据全部去除
for i in range(j, k):
    if nums3[j] >= keyAb:
        nums3.pop(j)
        j -= 1
        k -= 1
    j += 1

# c记录当前数字重复出现的次数 g 记录上次遍历位置 l当前角标
c, g, l = 0, 0, 0

# 选出数组中比a，b坐标值小的数据 并将这些数据中重复的数据进行角标同步 最后确定a，b坐标的最小值
for i in range(l, len(nums3)):
    g = 0
    for j in range(l + 1, len(nums3)):
        # 相同数据出现 记录
        if nums3[i] == nums3[j]:
            c += 1
            g += 1
    l = i + g + 1

# 最后输出的下列数据的意思为：
# 因为这个数组中所有的数据都比目标a，b坐标小 所有将该数组的长度减去重复数据出现的次数
# 那么就代表这个数组中所有的存储数据都是比目标a，b坐标小并且不重复的数据
# 最后+1 代表目标a，b坐标存放的位置
print(len(nums3) - c + 1)
