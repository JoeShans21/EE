import random
def quickSort(arr):
    global comparisons
    # Declares 3 lists that contain values relating to the pivot
    less = []
    equal = []
    greater = []
    # Checks if list is longer than 1 element
    if len(arr) > 1:
        # Set random pivot and compare current value to pivot
        pivot = random.choice(arr)
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
            comparisons += 1
        
        # Loop back around to sort the 3 lists we've created and return result
        return quickSort(less)+equal+quickSort(greater)
    else:
        # Returns original list if it's only 1 element long
        return arr
def sort(listSize):
    # Reset comparison variable from last sort
    global comparisons
    comparisons = 0
    # Create list of random numbers
    numbers = []
    for i in range(0,listSize):
        n = random.randint(1,1000)
        numbers.append(n)
    # Measure time for quick sort
    quickSort(numbers)
    return comparisons

print(sort(1000))