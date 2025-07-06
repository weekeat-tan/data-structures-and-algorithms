# Stack
## Introduction
**Stack** is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed.

Basic Stack Operations:
- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes the topmost element from the stack.
- **Peek (or Top)**: Returns the topmost element **without removing it**.
- **IsEmpty**: Checks if the stack is empty.
- **IsFull**: Checks if the stack is full.
    
The Stack operations above run in O(1) time complexity and O(1) space complexity.


## Implementations
The Stack data structure can be implemented using arrays and linked list:
- Array-based stacks are simple but have a fixed size, which may lead to stack overflow if it runs out of space.
- Linked list-based stacks provide dynamic memory but require extra space for pointers.

## Applications of Stack
### Memory Management (Function Call Stack)
- Manages function calls in programming by **pushing function calls onto the stack** and **popping them after execution**.
- Enables **recursion**, where each function call gets a new stack frame.
- Helps in tracking **local variables and return addresses** for each function.

### Expression Evaluation & Syntax Parsing
- Ensures correct execution order in **arithmetic epxressions** by managing operator precedence.
- Used in **parsing programming languages**, particularly for **validating brackets and expressions**.
Covnerts **infix expressions to postfix notation**, which is easier for computers to evaluate.

### Undo/Redo Mechanism in Software
- Stores user actions as **stack operations** in text editors, image editors, and IDEs.
- Pressing **Undo** pops the last action from the stack and reverses it.
- **Redo** re-applies an action by pushing it back onto the stack.

### Backtracking Algorithms
- Used in problems that require **trying different possibilities and reverting if needed**.
- Common in **Sudoku solvers, maze pathfinding, and the N-Queens problem**.
- Stores previous states, allowing the algorithm to **revert to an earlier positon** when a dead end is reached.

### Depth-first Search (DFS) in Graphs
- DFS explores a graph **deep into one path before backtracking**.
- Uses a stack to **store nodes** that need to be visited.
- Helps in **finding connected components, cycle detectino, and solving maze problems**.

### Web Page History (Back Button in Browsers)
- Every visited web page is **pushed onto the history stack**.
- Clicking "Back" **pops the last visited page**, returning the user to the previous one.
- This method allows users to **navigate webpages in reverse order efficiently**.