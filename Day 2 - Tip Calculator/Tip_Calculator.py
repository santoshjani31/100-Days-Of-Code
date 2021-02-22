# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1:
# https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? ")
perc_tip = input("What percentage top would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

each_person_pay = (float(total_bill) / int(people)) + ((float(total_bill) * (float(perc_tip) / 100)) / int(people))
each_person_pay = "{:.2f}".format(each_person_pay)

print(f"Each person should pay: ${each_person_pay}")
