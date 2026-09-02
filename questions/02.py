students = [
    ("Ash", 85),
    ("Rahul", 92),
    ("Priya", 78),
    ("Ravi", 95)
]

highest_score = students[0][1]
best_student = students[0][0]

for name, score in students:
    if score > highest_score:
        highest_score = score
        best_student = name

print(best_student)