def percent_diff(value1, value2):
    # Avoid division by zero
    if (value1 + value2) == 0:
        return 0
    
    percentage_difference = float((value1 - value2) / ((value1 + value2) / 2)) * 100
    return percentage_difference

# Example values
value1 = int(input("value1 = "))
value2 = int(input("value2 = "))

# Calculate percentage difference
percentage_difference = percent_diff(value1, value2)

# Print the result
print(f"The percentage difference between {value1} and {value2} is {percentage_difference:.2f}%")