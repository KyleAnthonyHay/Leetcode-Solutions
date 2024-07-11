# Monotonic Array

## Description

![description](./desc.png)

## Solution

```py
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for idx in range(1, len(array)):
        if array[idx - 1] < array[idx]:
            isNonIncreasing = False
        if array[idx - 1] > array[idx]:
            isNonDecreasing = False
        
    return isNonDecreasing or isNonIncreasing
```

**Time Complexity:** O(n) `n` for iterating through the array<br/>
**Space Complexity:** O(1) for variables<br/>

1. The idea is to iterate through the array keeping two conditions in mind:<br>

Is the array Non-Decreasing?<br>
Is the array Non-Increasing?<br>

The Answer to these questions are tracked in variables `isNonDecreasing` and `isNonIncreasing`.

```py
isNonDecreasing = True
isNonIncreasing = True
```
2. Now, we start from index 1(since we are comparing `idx` and `idx-1`) and check if the **first** index is smaller than the **second** index. If so, we know it is Non-Decreasing. If the *opposite* is true, we know it is Non-Increasing.

```py
for idx in range(1, len(array)):
    if array[idx - 1] < array[idx]:
        isNonIncreasing = False
    if array[idx - 1] > array[idx]:
        isNonDecreasing = False
    
return isNonDecreasing or isNonIncreasing
```

Finally, we return true if at least one of the conditions is true. IF both are true we know either: <br>

- the array size is >= 2
- the array contains only on number eg. [2 ,2, 2, 2]

and we're **Done**!
