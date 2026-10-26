import math

# Input Costs
venue_cost = float(input("Enter Venue Cost: "))
equipment_cost = float(input("Enter Equipment Cost: "))
catering_cost = float(input("Enter Catering Cost: "))
transport_cost = float(input("Enter Transport Cost: "))
certificate_cost = float(input("Enter Certificate Cost: "))

# Registration and Sponsorship Details
registration_fee = float(input("Enter Registration Fee per Participant: "))
participants = int(input("Enter Number of Participants: "))
sponsorship = float(input("Enter Sponsorship Amount: "))

# Total Event Cost
total_cost = (venue_cost + equipment_cost +
              catering_cost + transport_cost +
              certificate_cost)

# Participant Contribution
participant_contribution = registration_fee * participants

# Total Funds Available
total_funds = participant_contribution + sponsorship

# Shortfall / Surplus
difference = total_funds - total_cost

# Break-even Calculation
break_even_registrations = math.ceil(
    (total_cost - sponsorship) / registration_fee
)

# Output Report
print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")
print(f"Venue Cost              : ₹{venue_cost:.2f}")
print(f"Equipment Cost          : ₹{equipment_cost:.2f}")
print(f"Catering Cost           : ₹{catering_cost:.2f}")
print(f"Transport Cost          : ₹{transport_cost:.2f}")
print(f"Certificate Cost        : ₹{certificate_cost:.2f}")

print("------------------------------------------")
print(f"Total Event Cost        : ₹{total_cost:.2f}")

print("\nFunding Details")
print("------------------------------------------")
print(f"Participants            : {participants}")
print(f"Registration Fee        : ₹{registration_fee:.2f}")
print(f"Participant Contribution: ₹{participant_contribution:.2f}")
print(f"Sponsorship Amount      : ₹{sponsorship:.2f}")

print("------------------------------------------")
print(f"Total Funds Available   : ₹{total_funds:.2f}")

if difference >= 0:
    print(f"Event Surplus           : ₹{difference:.2f}")
else:
    print(f"Sponsorship Shortfall   : ₹{-difference:.2f}")

print("------------------------------------------")
print(f"Break-even Registrations: {break_even_registrations}")
print("==========================================")