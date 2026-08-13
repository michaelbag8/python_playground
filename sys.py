import sys
from process_text import process


if len(sys.argv) != 3:
    print("Usage: python main.py input.txt output.txt")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, "r") as file:
    text = file.read()

result =process(text)

with open(output_path, "w") as file:
    file.write(result)

print("\033[1;032mSuccess!\033[0m")