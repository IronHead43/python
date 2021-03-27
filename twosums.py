#twosum question from leetcode.com
#input an array of numbers then a target then the program will output the index of which 2 numbers add up to make the target (presuming there is only 1)
#note this example is heavily unoptimized, you can't enter 2 digit numbers, if the numbers are in a strange order it wont be able to find the answer

# Improved version

# Convert the numbers into a list by splitting them every whitespace using the .split() method, so that if we type in "2 3" we get a list ["2", "3"]
nums = input("").split()
target = int(input(""))

# Loop over all the unique elements of the list [that's why we convert into a set using the set() function, it removes all the duplicates from the list]
for num in set(nums):
    # Convert the current element into an integer
    num = int(num)
    # Calculate the complementary, i.e the number that needs to be added to it in order to get the target and converts it into a string [because our original list is made up of strings]
    complementary = str(target-num)
    # If the complementary that we calculated is in the list, we've found the solution!
    if complementary in nums:
        # Print the index of the elements we've found
        print([nums.index(str(num)), nums.index(complementary)])
        break
