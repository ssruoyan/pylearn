# 二叉树数据结构相关

# 二叉树结构
class BinaryTreeNode:
  def __init__(self, left, right, value):
    self.left = left
    self.right = right
    self.value = value

class BinaryTree:
  def __init__(self, root):
    self.root = root
    

# 二叉树遍历（遍历都是从左往右）

# 1.最简单的递归遍历（也可以称之为前序遍历）
# 即每次先递归访二叉树的 根节点 => 左子树 => 右子树

def recursive_travel(root: BinaryTreeNode):
  if (root == None): return

  print(root.value)
  recursive_travel(root.left)
  recursive_travel(root.right)

# 中序遍历。即先左边 => 根节点 => 右子树
def recursive_mid_travel(root: BinaryTreeNode):
  if (root == None): return

  recursive_mid_travel(root.left)
  print(root.value)
  recursive_mid_travel(root.right)

# 后续遍历。即先右边 => 根节点 => 左子树
def recursive_right_travel(root: BinaryTreeNode):
  if (root == None): return

  recursive_right_travel(root.right)
  print(root.value)
  recursive_right_travel(root.left)


#2. 非递归版本实现

# 前序遍历的迭代遍历版本。递归和迭代算法往往可以相互转换使用
def iteration_travel(root: BinaryTreeNode):
  stack = []

  while (root != None and len(stack) > 0):
    if (root != None):
      print(root.value)
      stack.append(root)
      root = root.left
    else:
      root = stack.pop().right