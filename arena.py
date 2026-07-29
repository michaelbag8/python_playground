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
