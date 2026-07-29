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
