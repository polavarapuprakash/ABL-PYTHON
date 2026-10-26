# Attendance Recovery Computation

# Input Details
total_classes = int(input("Enter total classes conducted: "))
classes_attended = int(input("Enter classes attended: "))
required_percentage = float(input("Enter eligibility percentage (e.g., 75): "))

# Current Attendance
current_percentage = (classes_attended / total_classes) * 100

print("\n===== ATTENDANCE REPORT =====")
print(f"Classes Conducted : {total_classes}")
print(f"Classes Attended  : {classes_attended}")
print(f"Current Attendance: {current_percentage:.2f}%")

# Eligibility Check
if current_percentage >= required_percentage:
    print("Status            : Eligible")
else:
    print("Status            : Not Eligible")

    # Find minimum consecutive classes 