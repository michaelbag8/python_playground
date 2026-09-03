def add_underscore(word):
    new_word = "_"
    for i in range(0,len(word)):
        new_word = word[i] + "_"
    return new_word
print(add_underscore("Hello"))

sum_of_even=0 
def sum_even(n):
    for i in range(1,n):
        if i % 2 == 0:
            sum_of_even=sum_of_even + i
    return sum_of_even
print(sum_even(30))

#parent class 
class Dog:
#class attribute
  species= "Canis Familiaris"
  def __init__(self, name, age):
    self.name = name
    self.age = age

a = Dog("Bingo", 3)
#child classes
class Bulldog(Dog):
    pass

#extending functionality to the parent class in the child class
class JackRusellTerier(Dog):
    def speak(self, sound="wof"):
        return f"{self.name} says {sound}"
class Dachshund(Dog):
    pass

# Recursion in Python 
def search_folder(current_folder, target_file):
    # Base Case 1: If we find the file inside this folder, return it
    if target_file in current_folder.files:
        return current_folder.path_to(target_file)
        
    # Recursive Case: Loop over any nested sub-folders
    for sub_folder in current_folder.sub_folders:
        path = search_folder(sub_folder, target_file) # Recursive call!
        if path is not None:
            return path
            
    return None # Base Case 2: Folder is empty and has no sub-folders
def calculate_water(mugs):
    if mugs <= 0:
        return 0  # Base case: 0 mugs require 0 ml
        
    # Recursive Case: 10ml for the current mug + water for the rest of the stack
    return 10 + calculate_water(mugs - 1)

total_water_ml = calculate_water(stack_size)

def wash_mugs(stack_size):
    if stack_size <= 0:  # Base case catches zero and negative safety boundaries
        print("Stack is empty!")
        return
        
    print(f"Washing mug {stack_size}")
    wash_mugs(stack_size - 1)  # Safely approaches the base case

wash_mugs(3)

def count_down(cups):
    if cups <= 0:
        print("Done!")
        return
    print("Cup: " + str(cups))
    count_down(cups - 1)

count_down(3)

def wash_mug(stack_size):
    # 1. BASE CASE (The Stop Switch)
    if stack_size == 0:
        print("All mugs are washed! Drying hands.")
        return  # Stop the function completely
        
    # 2. RECURSIVE CASE (Action + Shrink)
    print(f"Washing mug number {stack_size}...")
    
    # Call ourselves with one less mug!
    wash_mug(stack_size - 1)

class Employee:
  def set_name(self, new_name):
    self.name = new_name

  def set_salary(self, new_salary):
    self.salary = new_salary 

  # Add a give_raise() method with amount as an argument
  def give_raise(self, amount):
    self.salary = self.salary + amount

# Create the emp object
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary
print(emp.salary)

# Give emp a raise of 1500
emp.give_raise(1500)
print(emp.salary)

class BetterDate:
  def __init__(self, year, month, day):
    self.year, self.month, self.day = year, month, day
    
  # Define a class method from_str
  @classmethod
  def from_str(cls, datestr):
    # Split the string at "-"
    parts = datestr.split("-")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    # Return the class instance
    return cls(year, month, day)

# Create the xmas object      
xmas = BetterDate.from_str("2024-12-25")   
print(xmas.year)
print(xmas.month)
print(xmas.day)

class Person:
  CURRENT_YEAR = 2024
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Add a class method decorator
  @classmethod
  # Define the from_birth_year method
  def from_birth_year(cls, name, birth_year):
    # Create age
    age = cls.CURRENT_YEAR - birth_year
    # Return the name and age
    return cls(name, age)

bob = Person.from_birth_year("Bob", 1990)
print(bob.age)
print(bob.name)
