# Part 1

# Calculates average rainfall over a period of user-inputted years
print('Average Rainfall Calculator')

# Get the number of years from the user
years = int(input('\nEnter the number of years to calculate: '))

# Initialize variables
total_months = 0
total_rainfall = 0

# Loop to iterate over each year
for year in range(1,years + 1):
    print(f'\nYear {year}')

    # Loop to iterate over each month
    for month in range(1, 13):
        # Get the rainfall for the month from the user
        rainfall = float(input(f'Enter the rainfall (inches) for month {month}: '))
        # Add the rainfall for the month to the total rainfall
        total_rainfall += rainfall
        # Increment the total month count
        total_months += 1

# Calculate the average rainfall
avg_rainfall = total_rainfall / total_months

# Diplay results
print(f'\nTotal number of months: {total_months}')
print(f'Total inches of rain: {total_rainfall}')
print(f'Average rainfall per month: {avg_rainfall:.2f} inches.\n' )

# Part 2

# Calculate points based on the number of books purchased
def calculate_points(books_purchased):
    if books_purchased == 0:
        return 0
    elif 1 < books_purchased <= 3:
        return 5
    elif 3 < books_purchased <= 5:
        return 15
    elif 5 < books_purchased <= 7:
        return 30
    elif books_purchased >= 8:
        return 60
    else:
        print('Invalid number of books.')
        return 0

def main():
    # Ask user to enter the number of books purchased
    books_purchased = int(input("Enter the number of books purchased this month: "))

    # Calculate the points awarded
    points_awarded = calculate_points(books_purchased)

    # Display the points awarded
    print(f"Points awarded: {points_awarded}")

main()

