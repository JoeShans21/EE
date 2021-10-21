import random
import pygsheets

# Initialize google sheet client
client = pygsheets.authorize(service_account_file='secret.json')
sheet = client.open_by_key('1kF05N3kjYWG_oTJTeteCX5PDcB2RqOCC1FPBxst6nUo')
best = sheet.worksheet_by_title('Best Case Set')




# Prepare to count comparisons
comparisons = 0
# Quick sort algorithm
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

# Takes a list size, then returns time it takes to quicksort
def sort(listSize):
    # Reset comparison variable from last sort
    global comparisons
    comparisons = 0
    # Create list of random numbers
    numbers = []
    for i in range(0,listSize):
        n = random.randint(1,1000)
        numbers.append(n)
    quickSort(numbers)

    # Return list size and both times
    return comparisons




for i in range(0, 21):
    arr = []
    for j in range(0, 100):
        arr.append(sort(i*100))
    arr.sort(reverse = True)
    total = 0
    for k in range(0, 5):
        total += arr[k]
    avg = total / 5
    print(str(avg))

