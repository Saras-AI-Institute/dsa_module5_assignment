# Module 5 Lab: Real-Time Ride-Matching & Dispatch Engine

## 🎯 Objective & Overview
In this lab, you will build the core routing and dispatch system for a modern ride-sharing platform. This assignment covers **Section 1 (Graphs)** and **Section 2 (Priority Queues)** by requiring you to implement these data structures from scratch to solve matching and pathfinding problems.

You will manage two core components:
1.  **The Ride Request Triage (Priority Queue):** Managing incoming passenger requests and sorting them dynamically by their priority score (calculated via surge pricing and booking tier) so the highest-priority riders are matched first.
2.  **The City Navigation Grid (Graph):** Modeling city intersections and streets to find the fastest pickup path for a driver using graph traversal techniques.

---

## 📁 Repository Map

* **`structures/priority_queue.py`**: Implementation file for your binary heap-based Priority Queue.
* **`routing/city_graph.py`**: Implementation file for your city map graph and routing logic.
* **`test_dispatch.py`**: The `pytest` validation suite to verify your structures pass all edge cases.

---

## 🚀 System Components to Complete

### Task 1: The Ride Request Heap (`structures/priority_queue.py`)
Open `structures/priority_queue.py` and implement a Max-Binary Heap to back your Priority Queue. 
* **The Problem:** When ride requests flood the system, we cannot use a simple unsorted list (which requires $O(n)$ to find the highest priority) or a sorted list (which requires $O(n)$ to insert a new request). You must build a Max-Heap to ensure both insertions (`insert`) and extractions (`extract_max`) run in efficient $O(\log n)$ time.
* **Your Job:** Complete the manual up-heap (`_sift_up`) and down-heap (`_sift_down`) pointer shifting operations.

### Task 2: The City Navigation Network (`routing/city_graph.py`)
Open `routing/city_graph.py` and implement an adjacency-list-based weighted graph.
* **The Problem:** You need to calculate if a path exists between a driver and a rider, and find the total travel distance across a series of connected intersections.
* **Your Job:** Implement the graph building blocks (`add_intersection`, `add_road`) and write a graph traversal algorithm (such as Dijkstra's or a cost-tracking BFS) to return the shortest distance from a driver's starting intersection to the rider.

---

## 🧪 Running the Verification Suite

To verify your code correctness before submission, run the automated test suite.

1.  Ensure dependencies are installed:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the tests via your terminal:
    ```bash
    pytest test_dispatch.py
    ```
3.  Analyze any failing assertions to see where your heap properties or graph edge weights are breaking.
