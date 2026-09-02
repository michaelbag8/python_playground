def fix_articles(sentence):
    words = sentence.split()

    for i in range(len(words) - 1):
        if words[i].lower() in ("a", "an"):
            next_word = words[i + 1]

            if next_word[0].lower() in "aeiou":
                words[i] = "an"
            else:
                words[i] = "a"

    return " ".join(words)


text = "I saw a apple and an dog."
print(fix_articles(text))
#Refactor later to include capital A and AN
