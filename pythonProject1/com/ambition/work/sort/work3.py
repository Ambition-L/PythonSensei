# 课后练习第五题 暴力解法

# n个数据
a = input("请输入n：")

# 初始化存储用户输入数组 int(a) 表示将字符串转为int类型 因为input函数接收的是字符串
nums = [0] * int(a)

# 循环接受用户输入数据并放入数组
for i in range(0, int(a)):
    print("请输入第 " + str(i + 1) + "个数:")
    nums[i] = int(input())

# 定义记录逆序对的整数
count = 0


#  暴力解法 把每个数都与这个数的后一个数进行比较 如果比后面的数大就记录
# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] > nums[j]:
#             count += 1


def work3(num):
    global count
    if len(num) <= 1:
        return num
    mid = int(len(num) / 2)
    llist, rlist = work3(num[:mid]), work3(num[mid:])
    if len(llist) + len(rlist) > len(num):
        if len(llist) > len(rlist):
            llist.pop(0)
        else:
            rlist.pop(0)

    result = []
    i, j = 0, 0
    while i < len(llist) and j < len(rlist):
        if rlist[j] < llist[i]:
            result.append(rlist[j])
            j += 1
            # 当左边数据大于右边 说明这是个逆序对 记录
            count += 1
        else:
            result.append(llist[i])
            i += 1
            # 每次左数组指针移动时 重新比较右数据数据 （将右数组指针重制为0）
            j = 0

    # 如果左边集合未比较完 则把未比较完的次数累计添加上
    if i < len(llist):
        count += (len(llist) - 1 - i) * len(rlist)

    result += llist[i:] + rlist[j:]
    return result


work3(nums)
print(count)
