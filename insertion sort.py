#I believe this is insertion big-o-noation algorithm, created 28/03/2021 (ascending)
#it has some bugs, eg if you input 123987123 it will just return 123987123 but it works with lots of things.
#the development was quick but very interesting, I inputed 987654321 and it would return 18273645.

# Take the array as input
numbers = list(input("input a base 10 array of integers to be sorted into ascending order"))

# Start iterating from the second element of the list to the end [using the index, so starting at 1]
for i in range(1, len(numbers)):
    # Save the current number
    current_number = numbers[i]

    # Create a new index representing the previous number
    j = i-1

    # Find all the previous elements that are bigger than the current number and move them one position ahead
    while current_number < numbers[j] and j >= 0:
        numbers[j+1] = numbers[j]
        j -= 1
    
    numbers[j+1] = current_number

print(numbers)
