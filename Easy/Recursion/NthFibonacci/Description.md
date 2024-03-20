# NthFibonacci

## Description

![description](./desc.png)

## Solution 1

**Time: O(2^n) Two Recursive Calls Per Call stack layer** <br/>
**Space: O(n)** <br/>

1. Take care of the base case of the first two Fib Numbers `F(1) = 0` & `F(2) = 1`. This is essential for recursion because it tells the function when to stop calling itself and start returning values back up the chain.

```py
if n == 1:
    return 0
elif n == 2:
    return 1
```

2. If the fib number(n) is any alrger than 2, then we perform the calculation of `F(n-1)` + `F(n-2)`.<br>

```py
return getNthFib(n-1) + getNthFib(n-2)
```

This return function builds the Fibonacci sequence by calling the same function to get the previous two Fibonacci numbers. It works because the function calls accumilate on the call stack. Each recursive call will end when the base case is reached. <br>

Keep in mind that at each step, `n` is being reduced by 1 and 2. Therefore `n` will eventually reach the base case of **n = 1** and **n = 2**. <br>

This initiates the process of `unwinding the call stack`, where each function call returns its result back to the call that invoked it. This cascade of returns continues until the original call is resolved, producing the final sum and completing the calculation of the Fibonacci number for `n`.

## Solution 2 (Optimal)

**Time: O(n)** <br/>
**Space: O(1)** <br/>

1. Create variables `a` and `b`. These will represent the `current(a)` Fibonacci number and the `next(b)`. It is initialized to the first 2 according to the Fibonnaci base case.

```py
a = 0
b = 1
```

2.  Create a for loop that executes n-1 times.

```py
for _ in range(n-1):
    temp = a # Saved so we can add it to b
    a = b # Current fib number assigned
    b += temp # Next fib number calculated
return a
```

Essentially, what's happening is that we are shifting the values to the left by one index. `LastTwoFibNumbers[a, b]` and afterwards, adding the value of `a` to `b`. We _add_ `a` to `b` because we want to add the value of the previous two Fibonacci numbers. This will result in varible `b` containing the NEXT Fibonacci number, which we may or may not use depending on if we are at the end of the `for loop`. <br>

The next step is to return the value of `a`. This is the current Fibonacci number. For the next iteration of the loop, the value of `a` will be given the value of `b` which is the "Next Fibonacci Number(b += temp)" of the last loop, which -in that case- is the "_Current_ Fibonacci Number". <br>

We run the loop `n-1` times because we already have the first two Fibonacci numbers. To futher illustrate this, we can see the following:

```
a = 0
b = 1

# lets say n = 2
for _ in range(n-1):
    temp = a
    a = b
    b += temp
```

This loop only runs once, and we see that `a` is assigned the value of `b`. And if `b` is the current fib number, we do not need to run this loop again. If `n = 100`, b would still hold the value of the current fib number up until `b += temp`.
