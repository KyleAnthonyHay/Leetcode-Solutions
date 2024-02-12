# Validate Subsequence

**Time Complexity:** O(n)  
**Space Complexity:** O(n) because of the hashtable

## Description

![description](./desc.png)

## Solution

Create a **Hashtable** that will hold all the numbers that have been visited already. This allows us to use a particular formula. <br/>

```
x + y = TargetSum
x = the current value in the array
y = TargetSum - x: which is the currently obsrved number n the array minus the TargetSum
```

- If, at any point, `seqPointer` equals the length of the sequence, the algorithm concludes that the sequence is a valid subsequence of the array and returns `True`.
- If the loop completes and `seqPointer` has not reached the end of the sequence, it indicates that not all elements of the sequence were found in the array, and the algorithm returns `False`.

## Pointers

To enhance efficiency, the algorithm performs an initial check to compare the lengths of the array and the sequence. If the array is shorter than the sequence, it immediately returns `False`, avoiding unnecessary computations.
