#DataCamp Python Programming Fundamentals 
#Python for Developers
import string 
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
