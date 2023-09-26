import math

result = 1
base = 5
exponent = 3

# Method 1: Using a for loop
for x in range(exponent):
    result *= base 
print(result, "result 1")

# Method 2: Using Exponentiation operator (**)
result2 = base ** exponent
print(result2, "result 2")

# Method 3: Using pow() function
result3 = pow(base, exponent)
print(result3, "result 3")
    
# Method 4: Using math.exp() function
result4 = math.exp(exponent)
print(result4, "result 4")
