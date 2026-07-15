birth_year= int(input("enter your birth year "))
current_year = 2026
age=current_year - birth_year
print(age)
if age >= 18:
    print("You are eligible to vote yet")
else:
    print("You are not  eligible to vote  yet.")