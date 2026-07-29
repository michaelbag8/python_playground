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

