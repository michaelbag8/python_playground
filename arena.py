def unique_tags(tags):
    unique = []

    for tag in tags:
        cleaned = tag.strip().lower()

        if not cleaned:
            continue

        if cleaned not in unique:
            unique.append(cleaned)

    return sorted(unique)
