shopping_list = []

# Loop through each ingredient and amount in the recipe
for ingredient, amount in recipe.items():
    # Calculate the amount needed for the party
    needed_amount = amount * scale_factor
    
    # Check if we need to buy this ingredient
    if ingredient not in pantry or needed_amount > pantry[ingredient]:
        shopping_list.append(ingredient)

print("Shopping list for your party:")
print(shopping_list)
