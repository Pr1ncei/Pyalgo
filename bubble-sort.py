# Prince Pamintuan, CS-201
"""
FIN - Lab Activity 2 - Bubble Sort
1. Write a Python program that:
  - Defines a function bubble_sort(arr) to implement Bubble Sort
  - Prints the array after each pass of the outer loop.
  - Returns the sorted array
2. Challenge: Count and display the number of swaps performed
"""

def bubble_sort(arr):
  n = len(arr)
  count = 0
  for i in range(n):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j+1], arr[j]
        count += 1
    print(f"Pass {i+1}: {arr}")

  print(f"Total swaps: {count}")
  return arr

def main():
  data = list(map(int, input("Enter numbers separated by spaces: ").split()))
  print("Original:", data)
  sorted_data = bubble_sort(data)
  print("Sorted:", sorted_data)

if __name__ == "__main__":
  main()