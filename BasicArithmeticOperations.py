# Get input for bigNum and smallNum, convert them to integers
bigNum = int(input("Enter Big Number: "))
smallNum = int(input("Enter Small Number: "))

# Print the numbers (convert integers to strings for concatenation)
print("Big Number is: " + str(bigNum))
print("Small Number is: " + str(smallNum))

# Perform arithmetic operations
n = bigNum / smallNum
print(bigNum, '/', smallNum, '=', n)

f = bigNum // smallNum
print(bigNum, '//', smallNum, '=', f)

p = bigNum ** smallNum
print(bigNum, '**', smallNum, '=', p)

# Corrected the order of operations for proper calculation
l = (smallNum ** (1/4)) * bigNum
print(smallNum, '**(1/4)*', bigNum, '=', l)

m = bigNum % smallNum
print(bigNum, '%', smallNum, '=', m)

# Get a floating point number and a word from the user
x = float(input("Give a num: "))
y = input("Give me a word: ")

# Print the additional inputs
print(x)
print("2x num is: ", (x * 2))
print("The word is", "'", y, "'")
