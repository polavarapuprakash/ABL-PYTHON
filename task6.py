#import math

print("========== CAMPUS EVENT FINANCIAL PLANNING ==========\n")

# Event Expenses
venue_cost = float(input("Enter Venue Cost: ₹"))
equipment_cost = float(input("Enter Equipment Cost: ₹"))
catering_cost = float(input("Enter Catering Cost: ₹"))
transport_cost = float(input("Enter Transport Cost: ₹"))
certificate_cost = float(input("Enter Certificate Cost: ₹"))

# Funding Details
participants = int(input("\nEnter Expected Number of Participants: "))
registration_fee = float(input("Enter Registration Fee per Participant: ₹"))
sponsorship_amount = float(input("Enter Sponsorship Amount: ₹"))

# Total Cost
total_cost = (
    venue_cost +
    equipment_cost +
    catering_cost +
    transport_cost +
    certificate_cost
)

# Participant Contribution
participant_contribution = participants * registration_fee

# Total Funds Available
total_funds = participant_contribution + sponsorship_amount

# Surplus or Shortfall
difference = total_funds - total_cost

# Break-even Participants
if registration_fee > 0:
    break_even_participants = math.ceil(
        max(0, total_cost - sponsorship_amount) / registration_fee
    )
else:
    break_even_participants = 0

# Output Report
print("\n")
print("=" * 55)
print("           CAMPUS EVENT FINANCIAL REPORT")
print("=" * 55)

print(f"Venue Cost                 : ₹{venue_cost:.2f}")
print(f"Equipment Cost             : ₹{equipment_cost:.2f}")
print(f"Catering Cost              : ₹{catering_cost:.2f}")
print(f"Transport Cost             : ₹{transport_cost:.2f}")
print(f"Certificate Cost           : ₹{certificate_cost:.2f}")

print("-" * 55)
print(f"Total Event Cost           : ₹{total_cost:.2f}")

print("\nFUNDING DETAILS")
print("-" * 55)
print(f"Participants               : {participants}")
print(f"Registration Fee           : ₹{registration_fee:.2f}")
print(f"Participant Contribution   : ₹{participant_contribution:.2f}")
print(f"Sponsorship Amount         : ₹{sponsorship_amount:.2f}")

print("-" * 55)
print(f"Total Funds Available      : ₹{total_funds:.2f}")

if difference >= 0:
    print(f"Surplus Amount             : ₹{difference:.2f}")
else:
    print(f"Sponsorship Shortfall      : ₹{-difference:.2f}")

print("-" * 55)
print(f"Break-Even Registrations   : {break_even_participants}")
print("=" * 55)