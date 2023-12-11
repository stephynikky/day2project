print("Welcome to the tip calculator!!")
bill = float((input("What was your total bill?")))
tip = int((input("What tip percentage would you like to give? 10, 12, or 15?")))
people = int((input("How many total people?")))
total_bill = (bill*(1+tip/100))
per_person = total_bill / people 
final_amount = round (per_person, 2)
final_amount = "{:.2f}".format(per_person)
print(f"Each person should pay{final_amount}.")

