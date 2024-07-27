def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raise an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Example usage
a = 10
b = 0

print(f"The sum of {a} and {b} is: {add(a, b)}")
print(f"The difference of {a} and {b} is: {subtract(a, b)}")
print(f"The product of {a} and {b} is: {multiply(a, b)}")
print(f"The quotient of {a} and {b} is: {divide(a, b)}")


# Define a list named num_list containing 3 integers
num_list = [10, 20, 30]
# Fixed number to use in operations
fixed_number = 2
# Perform operations using the defined functions and a loop
for num in num_list:
    print(f"Performing operations on {num} with {fixed_number}:")
    
    # Call each function with the element and the fixed number
    sum_result = add(num, fixed_number)
    diff_result = subtract(num, fixed_number)
    prod_result = multiply(num, fixed_number)
    quot_result = divide(num, fixed_number)
    
    # Print the result of each function for each number in the list
    print(f"  {num} + {fixed_number} = {sum_result}")
    print(f"  {num} - {fixed_number} = {diff_result}")
    print(f"  {num} * {fixed_number} = {prod_result}")
    print(f"  {num} / {fixed_number} = {quot_result}\n")