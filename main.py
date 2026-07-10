sum_of_even = 0

for n in range (1, 100):
    if n % 2 == 0:
        sum_of_even = sum_of_even + n

print(sum_of_even)


for w in range (1, 10):
    if w == 5:
        break
    print(w)

print(f"printing {w} after the break")

for m in range (2, 10):
    if m == 6:
        continue
    print(m)
print(f"printing {m} after the continue")


phrase = "It's good to be home"

for c in phrase:
    if c == "h":
        break
else:
    print(f"there is not {c}")

for n in range(3):
    name = input("Enter name: ")
    password = input("Enter Password: ")
    if password == "Jurassic":
        print(f"Welcome Back {name}")
        break
        
else:
    print("Suspicious activity. The authorities have been alerted.")



while True:
    user =input("Enter a word or q to quit: ")
    if user == "q":
        break