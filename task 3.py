students = [
    ["Ravi", 65, 75, True],
    ["Sita", 35, 80, True],
    ["Kiran", 70, 60, True],
    ["Anu", 80, 85, False]
]

print("Academic Progression Report")

for student in students:
    name, marks, attendance, prerequisite = student

    if marks >= 40 and attendance >= 75 and prerequisite:
        print(name, "- Eligible for progression")
    else:
        print(name, "- Not eligible")

        if marks < 40:
            print("  Requirement: Pass the examination")

        if attendance < 75:
            print("  Requirement: Improve attendance")

        if not prerequisite:
            print("  Requirement: Complete prerequisites")