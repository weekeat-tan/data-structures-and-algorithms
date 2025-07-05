# Fast & Slow Pointers
## Introduction
The **Fast & Slow** pointer appraoch, also known as the **Hare & Tortoise algorithm**, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds.

## What is the Fast & Slow Ponters Pattern?
The **Fast and Slow Pointers** pattern involves using two pointers (or iterators) that move through a data structure at different speeds.

> Commonly, the "fast" pointer moves two steps at a time, while the "slow" pointer moves one step at a time. 

This technique is usually applied to _linked lists_ (though it can be used in arrays or other sequential data structures) and is a clever way to **detect conditions like cycles** or **find a specific position (e.g., the middle)**.

## Why use Fast & Slow Pointers?
1. **Cycle Detection:** The pattern helps in detecting cycles _without extra space_. You don't need additional data structures like hash sets to keep track of visited nodes.
2. **Efficiency:** By traversing the structure in a single pass, you reduce time complexity. You only use constant extra space - just two pointers!
3. **Finding Critical Positions:** Using different movement speeds allows you to pinpoint interesting locations, such as the middle of a list or the start of a cycle.

## Key Scenarios where this Pattern shines
1. **Linked List Cycle Detection:** Whenver a problem states, "Given a linked list, determine if it has a cycle," you should think about the Fast & Slow Pointers pattern.
2. **Middle of a Linked List:** If you need to find the middle node of a list in one pass, the Fast & Slow Pointers is perfect.
3. **Length of a Cycle:** After detecting a cycle, you can continue with the fast pointer to measure the cycle length.
4. **Reorder or Split Linked List:** When partitioning or rearranging a linked list, finding the middle node is often crucial.

## How the Fast & Slow Pointers work
### Step-by-Step Movement
1. **Initialisation:** Set both pointers to the head of the list.
2. **Movement:** In each iteratio:
    - The slow pointer (`slow`) moves by 1 node.
    - The fast pointer (`fast`) moves by 2 nodes.
3. **Check condition:**
    - If `fast` (or `fast.next`) becomes `null`, it means there's no cycle (you've reached the end).
    - If `slow` meets `fast`, there is a cycle or a special condition we're looking for.

You continue until:
- `fast` is `null` (no cycle), or
- `slow == fast` (cycle detected or specific position reached).