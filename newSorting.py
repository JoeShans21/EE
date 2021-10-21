import random
import pygsheets

# Initialize google sheet client
client = pygsheets.authorize(service_account_file='secret.json')
sheet = client.open_by_key('1kF05N3kjYWG_oTJTeteCX5PDcB2RqOCC1FPBxst6nUo')
wks = sheet.worksheet_by_title('Average Set')




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
        # Set random pivot and
        
        # Average
        pivot = random.choice(arr)

        # Take list and pre-sort for handpicking pivots
        newArr = arr
        newArr.sort()
        # Worst Case
        pivot = newArr[len(newArr)-1]
        # Best Case
        pivot = newArr[int(len(arr) / 2)]

        # Compare current value to pivot
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
def sort(listSize, numMax):
    # Reset comparison variable from last sort
    global comparisons
    comparisons = 0
    # Create list of random numbers
    numbers = []
    for i in range(0,listSize):
        n = random.randint(1, numMax)
        numbers.append(n)
    quickSort(numbers)

    # Return list size and both times
    return comparisons



# List Size increased in intervals
def NSet():
    for i in range(0, 1001):
        total = 0
        for j in range(0, 100):
            total += sort(i*10)
        total /= 100
        print(str(total))

# List Size stable (point set)
def pointSet(listSize, iterations, numMax):
    arr = []
    for i in range(0, iterations):
        arr.append(str(sort(listSize, numMax)))
    return arr

def addBatch(arr):
    f = open("nums.txt", "a")
    for i in range(len(arr)):
        f.write(arr[i] + "\n")
    f.close()

addBatch(pointSet(1000, 10000, 100))
