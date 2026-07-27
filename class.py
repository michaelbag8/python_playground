def add_underscore(word):
    new_word = "_"
    for I in range(0,len(word)):
        new_word = word[i] + "_"
    return new_word
print(add_underscore("Hello")

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
