# Day-3-Selection-Sort
Here Python Program for Selection Sort. Day 3 of Day 365.
- Initial Setup: Start with an unsorted array.
- Finding the Minimum: Begin with the first element and iterate through the array to find the smallest element.
- Swapping: Swap this smallest element with the first element of the array.
- Moving the Boundary: Move the boundary of the sorted and unsorted sections one element to the right.
- Repeating Steps: Repeat the process for the remaining unsorted portion of the array:
  - Find the smallest element in the unsorted section.
  - Swap it with the first unsorted element.
  - Move the boundary again.
- Completion: Continue this process until the entire array is sorted.

Here is a visual representation of the steps with an example array [64, 25, 12, 22, 11]:

1. Initial Array: [64, 25, 12, 22, 11]
2. Find 11: [64, 25, 12, 22, 11] (Swap 11 with 64)
3. Array After 1st Step: [11, 25, 12, 22, 64]
4. Find 12: [11, 25, 12, 22, 64] (Swap 12 with 25)
5. Array After 2nd Step: [11, 12, 25, 22, 64]
6. Find 22: [11, 12, 25, 22, 64] (Swap 22 with 25)
7. Array After 3rd Step: [11, 12, 22, 25, 64]
8. No Swap Needed: [11, 12, 22, 25, 64] (25 is already in place)
9. Final Sorted Array: [11, 12, 22, 25, 64]
