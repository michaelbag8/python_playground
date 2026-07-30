# Arena Drill Solutions 
def unique_tags(tags):
    unique = []

    for tag in tags:
        cleaned = tag.strip().lower()

        if not cleaned:
            continue

        if cleaned not in unique:
            unique.append(cleaned)

    return sorted(unique)

def top_scorer(scores):
    if not scores:
        return "No scores"

    top_name = None
    top_score = None

    for name, score in scores.items():
        if top_score is None:
            top_name = name
            top_score = score
        elif score > top_score:
            top_name = name
            top_score = score
        elif score == top_score and name < top_name:
            top_name = name

    return top_name

def set_comparison(a, b):
    set_a = set(a)
    set_b = set(b)

    return {
        "both": sorted(set_a & set_b),
        "only_a": sorted(set_a - set_b),
        "only_b": sorted(set_b - set_a),
    }
    
    def exact_calculator(left, operator, right):
    try:
        left = float(left)
        right = float(right)
    except ValueError:
        return "Invalid number"

    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    elif operator == "/":
        if right == 0:
            return "Cannot divide by zero"
        result = left / right
    elif operator == "%":
        if right == 0:
            return "Cannot divide by zero"
        result = left % right
    elif operator == "**":
        result = left ** right
    else:
        return "Invalid operator"

    return round(result, 2)

def score_summary(name, a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Invalid score"

    if a < 0 or a > 100 or b < 0 or b > 100 or c < 0 or c > 100:
        return "Invalid score"

    average = round((a + b + c) / 3, 2)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"

    return (
        f"Student: {name}\n"
        f"Average: {average}\n"
        f"Grade: {grade}"
            )

def password_strength(password):
    if len(password) < 8:
        return "Weak"

    has_letter = False
    has_digit = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    if has_letter and has_digit:
        return "Strong"
    else:
        return "Medium"

def vote_eligibility(age, country):
    age = int(age)
    country = country.strip().lower()

    if age >= 18 and country == "nigeria":
        return "Eligible"
    else:
        return "Not eligible"

def point_summary(point):
    x, y = point
    return {
        "x": x,
        "y": y,
        "manhattan": abs(x) + abs(y),
    }
    
def deep_flatten(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)

    return result

def calculate_inventory():
    customers = 3
    cereal_per_person = 2.5
    milk_per_person = 1.25

    total_cereal = 0
    total_milk = 0

    starting_cereal = 10.0
    starting_milk = 15.0

    total_cereal = cereal_per_person * customers
    total_milk = milk_per_person * customers

    remaining_cereal = starting_cereal - total_cereal
    remaining_milk = starting_milk - total_milk

    return remaining_cereal, remaining_milk

def set_kettle_temp(self, selected_drink):
    target_temp = 100

    if selected_drink == "Green Tea":
        target_temp = 80

    return target_temp

def bunk_assignment(service_number):
    room = (service_number - 1) // 8 + 1
    bunk = (service_number - 1) % 8 + 1
    return f"Room {room}, Bunk {bunk}"

def muster_record(name, service_number):
    return (
        f"RECRUIT: {name}\n"
        f"SERVICE NUMBER: {service_number}\n"
        f"QUARTERS: {bunk_assignment(service_number)}"
    )

def convert_number(value):
    try:
        number = float(value)
        return number * 2
    except ValueError:
        return "Invalid number"

def triangle_pattern(n):
    if n < 1:
        return ""

    lines = []

    for row in range(1, n + 1):
        line = "*" * row
        lines.append(line)

    result = "\n".join(lines)
    return result

def primes_up_to(n):
    primes = []

    for number in range(2, n + 1):
        is_prime = True

        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break

            divisor += 1

        if is_prime:
            primes.append(number)

    return primes


prime = primes_up_to(34)

print(prime)

def count_up(n):
    nums = []
    if n < 1:
        return nums
    for num in range(1, n+1):
        nums.append(num)
    return nums

def sum_multiple(limit, divisor):
    add = 0
    if divisor == 0:
        return "Invalid divisor"
    for i in range(1,limit+1):
        if i % divisor == 0:
            add += i
    return add

def collect_until_stop(items):
    result = []
    for item in items:
        if item.strip().lower()=="stop":
            break
        result.append(item)
    return result 
        
def skip_event(start, end):
    result = []
    if start > end:
        return result
    for even in range(start, end+1):
        if even%2==0:
            continue
        result.append(even)
    return result
