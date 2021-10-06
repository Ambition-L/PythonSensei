class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self):

        # 用于接收用户传入的数组
        nums = input().split()

        # 用于存储树节点
        node = []

        for item in nums:
            # 创建节点
            temp = TreeNode(item)
            # 添加节点
            node.append(temp)

        print(nums)

        index = 1

        # 遍历节点数组 为节点添加左右子节点
        for item in node:
            # 如果当前节点为null 则跳过
            if item == 0 or item.val == 'null':
                continue
            # 如果当前节点还存在左子节点 并且左子节点不为空 则将该左子节点添加为当前节点的左子节点
            if index * 2 - 1 < len(nums) and node[index * 2 - 1].val != "null":
                # 添加节点
                item.left = node[index * 2 - 1]
            # 如果当前节点还存在右子节点 并且右子节点不为空 则将该右子节点添加为当前节点的右子节点
            if index * 2 < len(nums) and node[index * 2].val != "null":
                item.right = node[index * 2]
            # 指针指向下一个节点
            index += 1

        node.insert(0, TreeNode(-1))
        return node

    def pres(self, node, i):
        if i >= len(node) or node[i] is None:
            return
        print(node[i].val)
        self.pres(node, i * 2)
        self.pres(node, i * 2 + 1)


root = TreeNode(1)
nodes = root.insert()
root.pres(nodes, 1)
