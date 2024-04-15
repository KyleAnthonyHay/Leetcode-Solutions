# Validate BST

## Description

![description](./desc.png)

## Solution

```py
def validateBst(tree):
    if tree == None:
        return True

    if tree.left is not None and tree.left.value >= tree.value:
        return False
    if tree.right is not None and tree.right.value < tree.value:
        return False

    return validateBst(tree.left) and validateBst(tree.right)
```

**Time: O(logn)** <br/>
**Space: O(1)** <br/>

The idea is
