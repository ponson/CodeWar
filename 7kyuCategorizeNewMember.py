def open_or_senior(data):
    category = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            category.append("Senior")
        else:
            category.append("Open")

    return category


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))