# Two Colorable

## Description

![description](./desc.png)

## Solution
```py
def twoColorable(edges):
    colors = [None for _ in edges]
    colors[0] = True
    stack = [0]

    while len(stack) > 0:
        node = stack.pop()
        for connection in edges[node]:
            if colors[connection] is None:
                colors[connection] = not colors[node]
                stack.append(connection)
            elif colors[connection] == colors[node]:
                return False
                
    return True
```

**Time Complexity:** O(V + E) **Width** * **Height** for visitng every index in the `matrix`<br/>
**Space Complexity:** O(V) for creating the `stack`<br/>

### Approach

The idea is to check the list of edges(`connection`) at each `node`, and set its color to the opssoite color of our currently observed `node`. If at any point we find that the color of a edge(`connection`) has been previously changed to the same color as our node we can return False.<br> 

We know this because if a **neighboring node** has been previously changed to the same colour as the current node, that means that **neighnoring node** has a adjecent node with the opposoite color as our current node. So, if we change the color of that **neighnoring node**, we would break the condtion.<br>

Let's break it down step by step.


1. Create a colors array initialized with None, for every node in the graph. Also set the first node to True and put it on the stack.

- True = Blue
- False = Red
- The stack is used to traverse the graph

```py
def twoColorable(edges):
    colors = [None for _ in edges]
    colors[0] = True
    stack = [0]
```

2. Now create a loop that checks the list of edges for each node. If the color of each connection has been not been changed we set it to the opposite of our currently observed node. We also add it to teh stack.

```py
while len(stack) > 0:
    node = stack.pop() # select currently observed node
    for connection in edges[node]:
        if colors[connection] is None:
            colors[connection] = not colors[node] # change to opposite color
            stack.append(connection) # add to stack
```

3. If the color has been previosuly changed AND it is equal to our `node`, we return False since the condition was broken.

```py
elif colors[connection] == colors[node]:
    return False
```

Alternitavely, If we reach check every node and do not brea teh condition, we can then return True.

```py
return True
```

and we're **Done!**