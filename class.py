# List of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Corresponding ages
ages = [20, 16, 22, 17, 19]

# Age threshold
age_threshold = 18

# Iterate through the list of names and ages
for i in range(len(names)):
    # Print the processing message
    print(f"Processing {names[i]}...")
    
    # Check if the person's age is greater than or equal to the age threshold
    if ages[i] >= age_threshold:
        print(f"{names[i]} is eligible.")
    else:
        print(f"{names[i]} is ineligible.")