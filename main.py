# days, weeks and months remaining if you have 90 years to life
age = input("What is your current age? ")

# 90 years = 32850 days
# 90 years = 4680 weeks
# 90 years = 1080 months

x = 32850 - (365 * int(age))
y = 4680 - (52 * int(age))
z = 1080 - (12 * int(age))

result = f"You have {x} days, {y} weeks and {z} months left"
print(result)

#Another way
age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = 360 * years_remaining
weeks_remaining = 53 * years_remaining
months_remaining = 12 * years_remaining

result = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left"
print(result)










