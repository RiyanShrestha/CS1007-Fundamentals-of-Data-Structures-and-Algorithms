#Write a program to find the largest and smallest element in an array. 
def find_largest_and_smallest(arr):
    if not arr: 
        return None, None  # Return None if the array is empty 
    
    return max(arr), min(arr)

#Example usage:
array = [3, 5, 1, 8, -3, 7, 2]
largest, smallest = find_largest_and_smallest(array)
print("Largest element:", largest)
print("Smallest element:", smallest)
