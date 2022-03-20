scores = {
 'Harry': 81,
 'Ron': 78,
 'Hermione': 99,
 'Draco': 74,
 'Neville': 62
}

grades = {}

for student in scores:
    score = scores[student]
    if score > 91:
        grades[student] = "Outstand"

print(f"{grades.keys()}: {grades.values()}")