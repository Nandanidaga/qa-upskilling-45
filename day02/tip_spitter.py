bill = float(input("Enter total bill: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = (bill * tip_percent) / 100

total_bill = bill + tip

amount_per_person = total_bill / people


print("Total bill including tip:", total_bill)
print("Amount per person:", amount_per_person)