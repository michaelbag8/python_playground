def transform_text(text):
    result = []
    for index, letter in enumerate(text):
        if index % 2 == 0:
            result.append(letter.lower())
        else:
            result.append(letter.upper())

    return "".join(result[::-1])
    text = transform_text("Michael Bag")
    print(text)


filename = "notes.txt"

notes = [
    "Learn Python decorators",
    "Practice file handling",
    "Build a mini project"
]

with open(filename, "w") as file:
    for note in notes:
        file.write(note + "\n")

print("Notes saved successfully!")
print("\nSaved Notes:")
print("-" * 25)

with open(filename, "r") as file:
    for number, note in enumerate(file, start=1):
        print(f"{number}. {note.strip()}")
