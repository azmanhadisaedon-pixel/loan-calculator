# Compare 2 Loans

print("=== Loan 1 ===")
loan1 = float(input("Loan 1 amount (RM): "))
months1 = int(input("Loan 1 months: "))
monthly1 = float(input("Loan 1 monthly (RM): "))

total1 = monthly1 * months1
interest1 = total1 - loan1

print("\n=== Loan 2 ===")
loan2 = float(input("Loan 2 amount (RM): "))
months2 = int(input("Loan 2 months: "))
monthly2 = float(input("Loan 2 monthly (RM): "))

total2 = monthly2 * months2
interest2 = total2 - loan2

print("\n--- Result ---")
print("Loan 1 Total:", round(total1,2), "| Interest:", round(interest1,2))
print("Loan 2 Total:", round(total2,2), "| Interest:", round(interest2,2))

if total1 < total2:
    print("\n👉 Loan 1 is cheaper")
elif total2 < total1:
    print("\n👉 Loan 2 is cheaper")
else:
    print("\n👉 Both are same")