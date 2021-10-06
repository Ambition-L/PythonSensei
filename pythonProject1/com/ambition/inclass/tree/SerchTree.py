# 二叉搜索树的完整功能 crud 自测无问题
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # 遍历 先中后
    def pres(self, node):
        if node is None:
            return
        print(node.val)
        self.pres(node.left)
        self.pres(node.right)

    # 插入数据到二叉搜索树
    def insertVal(self, val):
        if self.val:
            if val < self.val:  # 小于当前节点 进入左子树
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insertVal(val)
            else:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insertVal(val)
        else:
            node = TreeNode(val)

    # 查询一个数据是否在二叉搜索树中 因为后续需求 故无论查找到或者未查找到 都返回父节点和当前节点
    # node 当前节点，parent父节点，val 需要查找的值
    def searchVal(self, node, parent, val):
        # 如果查找完了所有节点依旧没有找到 则返回-1
        if node.val is None:
            return -1, node, parent

        # 如果找到 返回1 和当前节点
        if val == node.val:
            return 1, node, parent

        # 如果比节点大 进入右子树
        if val > node.val:
            return self.searchVal(node.right, node, val)

        # 如果比节点小则进入左子树
        if val < node.val:
            return self.searchVal(node.left, node, val)

    # 寻找二叉搜索树中某个节点的前继节点 （比当前节点小的所有节点中最大的一个节点）
    # 如果目标节点的左子树为空 那么他的前驱节点一定在 根节点到目标节点的路径上
    # 如果目标节点的左子树不为空 那么它的前驱节点一定在左子树的右子树的最后一个节点
    def searchFirstQ(self, node, val, maxn):
        # 如果节点全部查找完 依旧没有找到与传入的节点相等的数据 则返回-1 和路径上最大的数
        if node is None:
            return -1, maxn

        # 如果找到与目标节点相等的数
        if node.val == val:
            # 如果该节点存在左子树
            if node.left is not None:
                # 定义最大值
                temp = node.left
                # 遍历左子树的右子树 直至最后一个节点
                while temp.right is not None:
                    # 更新最大值
                    temp = temp.right
                return 1, temp
            else:
                # 如果不存在左子树 返回路径上的最大数
                return -1, maxn

        # 如果目标节点小于当前节点 进入左子树
        if val < node.val:
            return self.searchFirstQ(node.left, val, maxn)

        # 如果目标节点大于当前节点 进入右子树 并且当前节点作为最大前驱
        if val > node.val:
            return self.searchFirstQ(node.right, val, node.right.val)

    # 寻找二叉搜索树中某个节点的后继节点 （比当前节点大的所有节点中最小的一个节点）
    # 如果目标节点没有右子树 那么它的后继节点一定在根节点到目标节点的路径上
    # 如果目标节点有右子树 那么它的后继节点一定在 目标节点的右子树的左子树的左子树。。。的最后一个左子树上
    def searchLastJ(self, node, val, minx):
        # 如果没有找到 返回-1 和 路径最小值
        if node is None:
            return -1, minx

        # 如果找到了
        if node.val == val:
            # 存在右子树
            if node.right is not None:
                temp = node.right
                while temp.left is not None:
                    temp = node.left
                return 1, temp
            # 不存在右子树
            else:
                return -1, minx

        # 目标节点比当前节点大 进入右子树
        if val > node.val:
            return self.searchLastJ(node.right, val, minx)

        # 目标节点比当前节点小 进入左子树 并且当前节点作为最小后继
        if val < node.val:
            return self.searchLastJ(node.left, val, node.left.val)

    # 删除节点数据
    # 如果被删除节点的子节点树小于2，则直接删除 将被删除节点改为被删除节点的右右节点 无右节点改为子节点 无子节点直接删除
    # 如果被删除节点的子节点数大于二 但是不存在右节点 那么将被删除节点左节点地址指向被删除节点
    # 如果被删除节点的子节点数大于二 但是不存在左子树 那么将被删除节点的右节点地址指向被删除节点
    # 如果被删除节点的子节点数大于二 而且存在左右子树 进入右子树 如果不存在左子树 那么右节点为后继节点 将右节点指向被删除节点
            # 将被删除节点的右节点指向 右节点的右节点
            # 进入右子树 如果存在左子树 那么找到被删除节点的后继节点 将被删除节点改为后继节点
            #  将该后继节点的右子节点指向后继节点的左子节点 最后将该后继节点删除
    # root 根节点 val 删除的值
    def delNode(self, root, val):
        # 查找删除节点的位置
        exist, n, p = self.searchVal(root, root, val)

        # 如果没找到要删除的值
        if exist == -1:
            print("dont search val")

        # 如果找到了
        if exist == 1:
            # 如果不存在右子树
            if n.right is None:
                # 如果当前节点是父节点的左节点
                if n == p.left:
                    # 将被删除节点的左节点指向被删除节点的父节点的左节点
                    p.left = n.left
                    # 删除当前节点
                    del n
                elif n == p.right:
                    # 将被删除节点的左子节点 指向被删除节点的父节点的
                    p.right = n.left
                    # 删除当前节点
                    del n
            elif n.left is None:  # 如果不存在左子树
                # 如果当前节点是父节点的左节点
                if n == p.left:
                    # 将被删除节点的左节点指向被删除节点的父节点的左节点
                    p.left = n.right
                    # 删除当前节点
                    del n
                elif n == p.right:
                    # 将被删除节点的左子节点 指向被删除节点的父节点的
                    p.right = n.right
                    # 删除当前节点
                    del n
            else:  # 左右子树均不为空 则寻找被删除节点的后继节点
                # 进入右子树
                temp = n.right
                #  寻找后继节点
                if temp.left is None:  # 如果n的右子树没有左子树 那么n的右节点为后继节点
                    # 将n的节点修改为后继节点
                    n.val = temp.val
                    # 将n的右子树 修改为后继节点右子树
                    n.right = temp.right
                    # 删除右子树
                    del temp
                else:
                    # 如果n的右子树存在左子树 那么进入这个左子树
                    next = temp.left
                    # 寻找后继节点
                    while next.left is not None:
                        # 更新后继节点的父节点
                        temp = next
                        # 更新后继节点的值
                        next = next.left

                    # 将后继节点的值复制给 被删除节点n
                    n.val = next.val
                    # 将后继节点的右节点 指向后继节点的父节点的左子节点
                    temp.left = next.right
                    # 删除后继节点
                    del next


# 测试

# 插入
root = TreeNode(9)
root.insertVal(2)
root.insertVal(14)
root.insertVal(5)
root.insertVal(19)
root.insertVal(3)
root.insertVal(8)
root.insertVal(17)
root.insertVal(15)

# 遍历
# root.pres(root)

# 查找
# exist, n, p = root.searchVal(root, root, 15)
# print(exist)
# print(n)
# print(n.val)
# print(p)
# print(p.val)

# 查找前驱节点
# exist, maxv = root.searchFirstQ(root, 15, -1)
# print(exist)
# print(maxv)
# print(maxv.val)

# 查找后继节点
# exist, minx = root.searchLastJ(root, 5, -1)
# print(exist)
# print(minx)
# print(minx.val)

# 删除节点
root.delNode(root, 14)
root.pres(root)
