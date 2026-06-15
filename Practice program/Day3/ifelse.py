#Problem 1: Voting Eligibility
age=int(input("Enter your age:"))
if age>=18:
    print("Your are Eligible to Vote")
else:
    print("Your are not Eligible to Vote")

#Problem 2: Positive or Negative
n=int(input("Enter a Number:"))
if n>0:
    print("Positive Number")
elif n<0:
    print("Negative Number")
else:
    print("Zero")

#Problem 3: Even or Odd
n=int(input("Enter the number:"))
if n%2==0:
    print("Even")
else:
    print("odd")

#Problem 4: Pass or Fail
mark=int(input("Enter your mark:"))
if mark>=35:
    print("pass")
else:
    print("fail")

#Problem 5: Age Checker
age=int(input("Enter your age: "))
if age>=18:
    print("Major")
else:
    print("Minor")

#Problem 6: Largest of 2 Numbers
n1=int(input("Enter your number:"))
n2=int(input("Enter your number:"))
if n1>n2:
    print(f"{n1} is largest")
else:
    print(f"{n2} is largest")

#Problem 7: Smallest of 2 Numbers
n1=int(input("Enter your number:"))
n2=int(input("Enter your number:"))
if n1<n2:
    print(f"{n1} is smallest")
else:
    print(f"{n2} is smallest")

#Problem 8: Number is Zero or Not
n=int(input("Enter your number:"))
if n==0:
    print("Number is zero")
else:
    print("Number is not zero")

#Problem 9: Salary Eligibility
salary=int(input("Enter your salary:"))
if salary>=25000:
    print("Eligible")
else:
    print("Not Eligible")

#Problem 10: Password Check
password=int(input("Enter your password:"))
if password==1234:
    print("Access Granted")
else:
    print("Access Denied")
    
#vowels
dream_job=input("Enter your dream job :")
first_letter=dream_job[0].lower()
if first_letter in "aeiou":
    article="an"
else:
    article="a"
print("I want to become",article,dream_job+".")



