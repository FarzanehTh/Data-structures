class Node:

    """
    A Node representaion of a tree.

    """

    def __init__(self, val, right, left):
        self.value = val
        self.right = right
        self.left = left

# return number of unival trees given the root node, all three functions work together to return such a result

def is_basic_tree(node):
    if node.left.left is None and node.left.right is None:
        if node.right.left is None and node.right.right is None:
            return True
    return False


def check_unival_tree(node):
    if node.value == node.right.value == node.left.value:
        return True
    else:
        return False



def num_of_unival_tree(node):
    if node is None:
        return 1
    elif node.left is None and node.right is None:
        return 1
    elif is_basic_tree(node):
        if check_unival_tree(node):
            return 1
        else:
            return 0
    else:
        n1 = num_of_unival_tree(node.right) + num_of_unival_tree(node.left.value)
        if check_unival_tree(node):
            return n1 + 1
        return n1




# run
some_node = Node(10, None, None)
print(num_of_unival_tree(some_node))





