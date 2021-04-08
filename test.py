from datetime import datetime
import random
import pygsheets

# Initialize google sheet client
client = pygsheets.authorize(service_account_file='secret.json')
sheet = client.open_by_key('1kF05N3kjYWG_oTJTeteCX5PDcB2RqOCC1FPBxst6nUo')
point = sheet.worksheet_by_title('Point Data Set')
comp = sheet.worksheet_by_title('Comparison Data Set')

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

# Takes a list size, then returns time it takes to sort that list for bubble and quick
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
    startTime1 = datetime.now()
    quickSort(numbers)
    quickTime = datetime.now() - startTime1

    # Return list size and both times
    return [str(listSize), str(quickTime.microseconds), str(comparisons)]

# Add a group of rows with given list sizes
def addBatch(listSizes):
    for i in range(len(listSizes)):
        comp.insert_rows(i+1, values=sort(listSizes[i]))

# Create a data set that is used to compare point data set to
sizes = []
for i in range(0, 21):
    sizes.append(i*100)
addBatch(sizes)

# Input point data set
for i in range(1000):
  point.insert_rows(i+1, values=sort(1000))