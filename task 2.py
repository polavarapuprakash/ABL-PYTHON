reports = [
    ["Water Leakage", 3, 2, 4],
    ["Broken Fan", 1, 3, 2],
    ["Electrical Problem", 3, 3, 3],
    ["Damaged Bench", 1, 1, 1]
]

print("Campus Maintenance Priority")

for report in reports:
    name, severity, location, frequency = report

    score = severity * 3 + location * 2 + frequency

    if score >= 15:
        priority = "High"
    elif score >= 10:
        priority = "Medium"
    else:
        priority = "Low"

    print(name, "- Score:", score, "- Priority:", priority)