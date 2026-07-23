total = 0
def add_to_total(n):
    total= total + n

add_to_total(5)
print(total) # return error 


# to fix the error 
total = 0
def add_to_total(n):
    global total
    total= total + n

add_to_total(5)
print(total)
