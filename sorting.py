from datetime import datetime
import random
import pygsheets

# Initialize google sheet client
client = pygsheets.authorize(service_account_file='secret.json')
sheet = client.open_by_key('1kF05N3kjYWG_oTJTeteCX5PDcB2RqOCC1FPBxst6nUo')
wks = sheet.worksheet_by_title('Data')

# Quick sort algorithm
def quickSort(arr):
    # Declares 3 lists that contain values relating to the pivot
    less = []
    equal = []
    greater = []
    # Checks if list is longer than 1 element
    if len(arr) > 1:
        # Set pivot and compare current value to pivot
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        
        # Loop back around to sort the 3 lists we've created and return result
        return quickSort(less)+equal+quickSort(greater)
    else:
        # Returns original list if it's only 1 element long
        return arr

# Bubble sort algorithm
def bubbleSort(arr): 
    # Loop through array
    for i in range(len(arr)): 
        for j in range(0, len(arr)-i-1):
            # Switches elements if next element is smaller
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Return resulting list
    return arr

# Takes a list size, then returns time it takes to sort that list for bubble and quick
def sort(listSize):
    # Create list of random numbers
    numbers = []
    for i in range(0,listSize):
        n = random.randint(1,1000)
        numbers.append(n)
    # Measure time for quick sort
    startTime1 = datetime.now()
    quickSort(numbers)
    quickTime = datetime.now() - startTime1
    # Measure time for bubble sort
    startTime2 = datetime.now()
    bubbleSort(numbers)
    bubbleTime = datetime.now() - startTime2

    # Return list size and both times
    return [str(listSize), str(quickTime.microseconds), str(bubbleTime.seconds) + "," + str(bubbleTime.microseconds)]

# Adds results of sorts to google sheet
def addBatch(listSizes):
    for i in range(len(listSizes)):
        wks.insert_rows(i+1, values=sort(listSizes[i]))
sizes = []
for i in range(0, 101):
    sizes.append(i*100)
addBatch(sizes)