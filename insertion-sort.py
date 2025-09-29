# Prince Pamintuan, CS-201
"""
FIN - Lab Activity 3 - Insertion Sort
1. Write a Python function bubble_sort(arr) that:
  - Use Insertion Sort to arrange values in ascending order
  - Prints the array after each insertion of the key element
2. Challenge: Count and display the number of swaps performed
"""

def insertion_sort(arr):
    n = len(arr)
    count = 0 
    
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            count += 1
           
        if arr[j+1] != key:
            arr[j+1] = key
            print(f"Inserting {key}: {arr}")
        
        
    
    print(f"Total shifts/swaps: {count}")
    return arr
        
def main():
    data = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Original:", data)
    sorted_data = insertion_sort(data)
    print("Sorted:", sorted_data)

if __name__ == "__main__":
    main()