# Function to perform Selection Sort
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Get the list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
# Convert the string input to a list of integers
arr = list(map(int, user_input.split()))

# Print the unsorted list
print("Unsorted list:", arr)
# Sort the list using Selection Sort
sorted_arr = selection_sort(arr)
# Print the sorted list
print("Sorted list:", sorted_arr)
