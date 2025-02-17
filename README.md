# Data Structure and Algorithms Using Python

A comprehensive collection of data structures and algorithms implemented in Python, focusing on educational purposes and practical applications.

## 🎯 Project Overview

This repository contains implementations of fundamental to advanced algorithms and data structures, organized in a structured manner for easy learning and reference. Each implementation includes detailed documentation, time/space complexity analysis, and usage examples.

## 🏗️ Project Structure

The project is organized into three main categories:

### 1. Foundational Algorithms
- **Sorting Algorithms**:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Merge Sort
  - Quick Sort
  - Heap Sort
- **Searching Algorithms**:
  - Linear Search
  - Binary Search
  - Depth First Search (DFS)
  - Breadth First Search (BFS)

### 2. Intermediate Algorithms
- **Graph Algorithms**: 
  - Dijkstra's Algorithm (Shortest Path)
  - Floyd-Warshall Algorithm (All-Pairs Shortest Path)
  - Kruskal's Algorithm (Minimum Spanning Tree)
  - Prim's Algorithm (Minimum Spanning Tree)
  - Bellman-Ford Algorithm
- **Divide and Conquer**:
  - Binary Search Tree Operations
  - Merge Sort and Quick Sort
- **Dynamic Programming**:
  - Fibonacci Sequence
  - Longest Common Subsequence
  - Knapsack Problem
  - Matrix Chain Multiplication
  - Coin Change Problem
- **Greedy Algorithms**:
  - Activity Selection
  - Huffman Coding
  - Fractional Knapsack

### 3. Advanced Algorithms
- **String Algorithms**:
  - KMP Pattern Matching
  - Rabin-Karp Algorithm
  - Longest Palindromic Substring
- **Backtracking**:
  - N-Queens Problem
  - Rat in a Maze
  - Sudoku Solver
- **Advanced Graph Algorithms**:
  - Tarjan's Algorithm (SCC)
  - Kosaraju's Algorithm
  - Edmonds-Karp (Max Flow)
- **Other Topics**:
  - Trie Operations
  - Segment Trees
  - Fenwick Trees
  - Union-Find

## 🚀 Key Features

1. **Comprehensive Documentation**
   - Each algorithm includes detailed explanations
   - Time and space complexity analysis
   - Implementation characteristics and use cases

2. **Practical Examples**
   - Every algorithm comes with usage examples
   - Real-world application scenarios
   - Test cases demonstrating functionality

3. **Educational Focus**
   - Clear code structure and comments
   - Step-by-step implementation details
   - Optimization techniques and best practices

## 💻 Usage Example

Here's a quick example using the Binary Search Tree implementation:

```python
from BST_Algorithm import BinarySearchTree

# Initialize BST
bst = BinarySearchTree()

# Insert elements
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)

# Search for elements
print(bst.search(40))  # True
print(bst.search(90))  # False

# Get sorted elements (inorder traversal)
print(bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]
```

## 🛠️ Implementation Details

Each algorithm is implemented with a focus on:
- Clean, readable code
- Efficient implementation
- Proper error handling
- Extensive documentation
- Performance optimization

## 📚 Learning Resources

The repository serves as a learning resource for:
- Computer Science students
- Software developers
- Interview preparation
- Algorithm enthusiasts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
 
