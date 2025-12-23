"""
Sort an array containing only 0's, 1's, and 2's in a single traversal.

Problem:
Given an array consisting only of 0s, 1s, and 2s, sort the array
without using any built-in sorting function.

Example:
    Input:  [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Approach:
This problem is solved using the Dutch National Flag Algorithm.

Three pointers are maintained:
- low  : boundary for 0s
- mid  : current index
- high : boundary for 2s

Rules:
- If arr[mid] == 0:
    Swap arr[low] and arr[mid], then increment both low and mid.
- If arr[mid] == 1:
    Increment mid.
- If arr[mid] == 2:
    Swap arr[mid] and arr[high], then decrement high.

Algorithm:
1. Initialize low = 0, mid = 0, high = len(arr) - 1
2. Traverse the array while mid <= high
3. Apply swaps based on the value at arr[mid]

Time Complexity:
    O(n) — single pass through the array

Space Complexity:
    O(1) — in-place sorting

Notes:
- Also known as the Dutch National Flag Algorithm (Edsger Dijkstra)
- Optimal solution for this constrained sorting problem
"""



def sort_0_1_2(arr):
    n = len(arr)
    low, mid, high = (0, 0, n - 1)

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid += 1
            low += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

a = [2, 0, 2, 1, 1, 0]
sort_0_1_2(a)
print(a)
















