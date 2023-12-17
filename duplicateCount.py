def duplicate_count(text):
    count = {}
    duplicates = 0
    for character in text.upper():
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    for c in count.values():
        if c >= 2:
            duplicates += 1

    return duplicates


print(duplicate_count("Indivisibilities"))


def duplicate_count(text):
    count = {}
    duplicates = 0
    for character in text.upper():
        if character in count:
            count[character] += 1
            if count[character] == 2:
                duplicates += 1
        else:
            count[character] = 1

    return duplicates


print(duplicate_count("Indivisibilities"))

# pythonic

# 1
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(duplicate_count("Indivisibilities"))

# 2
def duplicate_count(text):
    text = text.lower()
    return (sum([text.count(c) > 1 for c in set(text)]))


print(duplicate_count("Indivisibilities"))
