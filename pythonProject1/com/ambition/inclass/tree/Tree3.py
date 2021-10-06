# 构建二叉树 并且遍历方法二

class Node2:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def insert(self, data):
        # 将新值与父节点进行比较
        if self.data:  # 非空
            if data < self.data:  # 新值较小，放左边
                if self.left is None:  # 若空，则新建插入节点
                    self.left = Node2(data)
                else:  # 否则，递归往下查找
                    self.left.insert(data)
            elif data > self.data:  # 新值较大，放右边
                if self.right is None:  # 若空，则新建插入节点
                    self.right = Node2(data)
                else:  # 否则，递归往下查找
                    self.right.insert(data)
        else:
            self.data = data  # 如果父节点为空 则该节点作为父节点


class BST:
    def __init__(self, tList):
        self.root = Node2(tList[0])
        for i in tList[1:]:
            self.root.insert(i)

    def pres(self, node):
        if node is None:
            return
        print(node.data)
        self.pres(node.left)
        self.pres(node.right)


nums = ['1', '2', '3', '4', '5', '6', '7']
bst = BST(nums)
bst.pres(bst.root)
