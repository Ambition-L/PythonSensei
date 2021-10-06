## 构建二叉树并且遍历 方法一
## 先创建节点树
## 再为节点树添加孩子节点
## 遍历：先序 DLR 中序 LDR 后序 LRD 针对的是父节点的先后顺序

# 注意点 ： 构建完二叉树之前 需要将根节点插入空数据 方便孩子节点的构建
# 遍历时 注意结束条件

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


nums = ['1', '2', '3', '4', '5']
tree = ['null']
for item in nums:
    tree.append(Node(item))

index = 1

for item in tree:
    if item == "null":
        continue

    if 2 * index < len(nums) and tree[2 * index].val is not None:
        item.left = tree[2 * index]

    if 2 * index + 1 < len(nums) and tree[2 * index + 1].val is not None:
        item.right = tree[2 * index + 1]

    index += 1


def pres(node, i):
    if i >= len(node) or node[i] == "null":
        return

    print(node[i])
    pres(node, i * 2)
    pres(node, i * 2 + 1)


pres(tree[1])
