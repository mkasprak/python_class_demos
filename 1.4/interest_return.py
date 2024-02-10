# Function to calculate simple interest
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Example usage of the function
principal_amount = int(input("Enter the principal amount: "))
interest_rate = int(
    input("Enter the interest rate as a whole number (5% would be 5): "))
investment_time = int(input("Enter the investment time in whole years: "))

# Calculating the interest
calculated_interest = calculate_interest(
    principal_amount, interest_rate, investment_time)

# Displaying the result
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
at an interest rate of {interest_rate}% over a period of {investment_time} years is: ${calculated_interest:,.2f}")
