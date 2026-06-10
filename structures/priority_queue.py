"""
Module 5: Max Priority Queue (Binary Heap Implementation)
Implement a Max-Heap to sort ride requests by priority scores.
Do NOT use Python's built-in heapq module.
"""

class RideRequest:
    def __init__(self, rider_name: str, priority_score: float):
        self.rider_name = rider_name
        self.priority_score = priority_score  # Higher score = Higher priority

    def __repr__(self):
        return f"({self.rider_name}: {self.priority_score})"


class DispatchPriorityQueue:
    def __init__(self):
        # Internal array representation of the binary heap
        self.heap = []

    def _get_parent_idx(self, idx: int) -> int: return (idx - 1) // 2
    def _get_left_child_idx(self, idx: int) -> int: return (2 * idx) + 1
    def _get_right_child_idx(self, idx: int) -> int: return (2 * idx) + 2

    def insert(self, request: RideRequest) -> None:
        """
        Inserts a new ride request into the heap.
        TODO: 
        1. Append the request to the end of self.heap.
        2. Call self._sift_up on the last index to restore heap properties.
        """
        # YOUR CODE HERE
        pass

    def extract_max(self) -> RideRequest:
        """
        Removes and returns the highest priority ride request.
        TODO:
        1. Handle the empty heap edge case (return None).
        2. If only 1 item exists, pop and return it.
        3. Otherwise, swap the root element with the last element.
        4. Pop the last element (the old max value) to save it.
        5. Call self._sift_down on the new root (index 0) to re-heapify.
        6. Return the saved old max value.
        """
        # YOUR CODE HERE
        pass

    def _sift_up(self, idx: int) -> None:
        """
        TODO: Compare the element at idx with its parent. 
        If the element has a higher priority_score than its parent, swap them 
        and recursively continue sifting up from the parent's index.
        """
        # YOUR CODE HERE
        pass

    def _sift_down(self, idx: int) -> None:
        """
        TODO: Compare the element at idx with its left and right children.
        Find the child with the largest priority_score. If that child is larger
        than the element at idx, swap them and continue sifting down.
        """
        # YOUR CODE HERE
        pass

    def is_empty(self) -> bool:
        return len(self.heap) == 0
