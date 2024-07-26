# Taking input for the number of elements in the array
n = int(input("Enter number of elements-"))

# Taking input for the elements of the array
arr = list(map(int, input().split()))

# Initializing variables to store the largest number and its count
largest = arr[0]
count = 1

# Finding the largest number and its count
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
        count = 1
    elif arr[i] == largest:
        count += 1

# Printing the largest number and its count
print(largest, count)
