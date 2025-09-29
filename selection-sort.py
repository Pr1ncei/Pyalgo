# Prince Pamintuan, CS-201
"""
FIN - Lab Activity 4 - Selection Sort
1. Write a Python function selection_sort(arr) that:
  - Finds the minimum value in the unsorted part
  - Swaps it with the first unsorted element
  - Prints the array after each selection and swap
2. Challenge: Count and display the number of swaps performed
"""

# Pseudocode
"""
INPUT data
PRINT("Original:", data)
n = SIZE of data
count = 0 
for i of 0 to n - 1:
    min = i
    for j in i + 1 to n:
        if data[j] IS LESS THAN data[min]:
            min = j 
            count += 1
    SWAP arr[i] and arr[min]
    PRINT(f"Step {i+1}: {data}")
    
PRINT total swaps
RETURN sorted_data 
PRINT sorted_data
"""
def selection_sort(arr):
    n = len(arr)
    count = 0 
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            count += 1
        print(f"Step {i+1}: {arr} (min_index={min})")
    print(f"Total swaps: ", count)
    return arr
            
def main():
    data = list(map(int, input("Enter numbers separated by spcaces: ").split()))
    print("Original:", data)
    sorted_data = selection_sort(data)
    print("Sorted:", sorted_data)

if __name__ == "__main__":
    main()