# Validate Subsequence

**Time Complexity:** O(n)  
**Space Complexity:** O(n) because of the hashtable

## Description

![description](./desc.png)

## Solution 1

Create a **Hashtable** that will hold all the numbers that have been visited already. This allows us to use a particular formula. <br/>

```
x + y = TargetSum
x = the current value in the array
y = TargetSum - x: which is the currently obsrved number n the array minus the TargetSum
```

At each point in the for loop, the algorithm cehcks if the `y` is in the hashtable. If it is, the algorithm returns `True`. Otherwise, it adds the `x`, the currenlt viewed number, to the hashtable.

- If, `y` is in the hashtable then we have found our match and it returns true
- If, `y` is not in the hashtable then we add the `x` to the hashtable and continue the loop

## Solution 2

1. Sort the array in ascending order
2. Create two pointers at both ends of the array
3. check the sum of two pointers
4. madjust ove pointers accordingly while match is not found
5. if match is not in array return empty array

Create a for loop that will iterate through the array and check if the sum of the two numbers is equal to the target sum. If it is, return `True`. <br/>

If it is false then there are `2` more conditions to check:

```
currentSum = array[left] + array[right]
if currentSum > targetSum: move right pointer down
if currentSum < targetSum: move left pointer up
```

Finally, if the pointers cross, then we have checked ebveruy value in the array amd there is no match. Hence, we return an empty array
