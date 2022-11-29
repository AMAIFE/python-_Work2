
# Write a function that calculate the power of a number.
# Then write a unit test to check the correctness of the function


base = 5
exponent = 3

result = 1

while exponent != 0:
    result *= base
    exponent -= 1

print("Answer = " + str(result))
