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
