Birth_year = int(input("Please enter your birth year: "))
This_year = int(input("Enter current year: "))
Age = This_year - Birth_year
print("You are", Age, "years old" )
if Age > 18:
    print("You are and Adult")
elif Age >= 13:
    print("You are a teenager")
elif Age < 13:
    print("You are a minor")