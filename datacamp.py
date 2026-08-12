#DataCamp Python Programming Fundamentals 
#Python for Developers
import string 
import pandas as pd
total_confirmations = 10
guest_count = 0

# Count confirmations using a while loop
while guest_count < total_confirmations:
    guest_count += 1 
    print(guest_count, "guests so far!")

print("We have", guest_count, "guests coming!")shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor
    
    # Check if we need to buy this ingredient
    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)

# Create an empty shopping list
shopping_list = []

# Loop through each ingredient and required quantity
for ingredient, required_qty in recipe.items():
    # Check if we need more than what we have
    if required_qty > pantry_stock[ingredient]:
        # Add the ingredient to our shopping list
        shopping_list.append(ingredient)

# Display the shopping list
print("Shopping list:", shopping_list)

total_ingredients = 7
ingredients_checked = 0

# Set up the loop
while ingredients_checked < total_ingredients:
    # Increment the counter
    ingredients_checked += 1
    # Check if less than 4 ingredients reviewed
    if ingredients_checked < 4:
        print("More than half remaining")
    # Check if 6 or fewer ingredients reviewed
    elif ingredients_checked <= 6:
        print("Nearly finished checking")
    else:
        print("All ingredients verified!")


def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False

# Call the function and store the result
is_valid = validate_password("user_password")
print("Is the password valid? ", is_valid)

full_name = "Alan Turing"

# Define the generate_email function
def generate_email(full_name):
    name_parts = full_name.split()
    email = name_parts[0].lower() + '.' + name_parts[1].lower() + '@techcompany.com'
    
    # Return the email address
    return email

# Call the function on the full_name string
print(generate_email(full_name))

test_durations = [245.50, 189.99, 312.75, 156.20, 428.90, 201.35, 167.80]

 # Complete the function
def test_report(durations):
    num_tests = len(durations)
    
    # Calculate total test time
    total_time =sum(durations)
    
    print("=== Test Report ===")
    print("Total Tests: ", num_tests)
    print("Total Execution Time (s): ", total_time)

# Generate the report for recent test runs
test_report(test_durations)

def clean_text(text, lower=True):
    # Add a multi-line docstring
    """
    Clean text by swapping spaces to underscores and converting to lowercase.
    
    Args:
    	text (str): A string to be cleaned.
    	lower (bool): Whether to convert the text to lowercase.
    
    Returns:
    	text(str): Cleaned string.
    """
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()
      
print(help(clean_text))

def calculate_discount(price, discount_percent=15, round_result=True):
    # Add a single-line docstring
    """Calculate the discounted price of a product."""
    
    discounted_price = price - (price * (discount_percent / 100))
    if round_result == True:
        return round(discounted_price, 2)
    else:
        return discounted_price

# Access the docstring
print(calculate_discount.__doc__)

original_price = 899.99

# Define the function with default arguments
def calculate_discount(price, discount_percent=15, round_result=True):
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        # Round the result to two decimal places
        return round(discounted_price, 2)
    else:
        return discounted_price

# Call the function with keyword arguments
final_price = calculate_discount(price=original_price,discount_percent=25,round_result=False)
print(final_price)

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries("tweets.csv", 10, "lang")

# Print result_counts
print(result_counts)
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {value: len(value) for value in fellowship}

# Print the new dictionary
print(new_fellowship)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)


