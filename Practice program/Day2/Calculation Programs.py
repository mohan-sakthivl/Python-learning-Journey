#Program 12: Age After 5 Years
age=int(input("Enter your age:"))
after_5years=(age+5)
print(f"Your age after 5 years =",after_5years)

#Program 13: Daily Study Hours Tracker
hour=int(input("Enter the number of hours you are studying per day :"))
days=int(input("Enter the number of days you are studying :"))
total_study_hours=hour*days
print(f"Total Study Hours =",total_study_hours)

#Program 14: Monthly Expense Calculator
food=int(input("Enter the food expense:"))
travel=int(input("Enter the travel expense:"))
internet=int(input("Enter the internet expense:"))
total_expense=food+travel+internet
average_expense=total_expense/3
print(f"Total Expense =",total_expense)
print(f"Average Expense =",average_expense)

#Program 15: Simple Bill Calculator
quantity=int(input("Enter the number of quantity:"))
price=int(input("Enter the price amount:"))
bill=quantity*price
print("Total Bill =",bill)