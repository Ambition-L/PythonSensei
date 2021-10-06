nums = [1, 1, 2, 5, 5, 6, 7]

# 寻找数组中的最大值和最小值
minv, maxv = min(nums), max(nums)

a2 = [0] * (maxv - minv + 1)

for i in nums:
    a2[i - minv] += 1

print(a2)
