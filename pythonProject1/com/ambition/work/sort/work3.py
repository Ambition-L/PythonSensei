## 课后练习第五题

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

def work3(num):
    global count
    if len(num) <= 1:
        return num
    mid = int(len(num) / 2)
    llist, rlist = work3(num[:mid]), work3(num[mid:])
    result = []
    i, j = 0, 0,
    while i < len(llist) and j < len(rlist):
        if rlist[j] < llist[i]:
            result.append(rlist[j])
            j += 1
            # 当左边数据大于右边 说明这是个逆序对 记录
            count += 1
        else:
            result.append(llist[i])
            i += 1
    result += llist[i:] + rlist[j:]
    return result


print(work3(nums))
print(count)
