#test1 Largest of 3 numbers
n1=int(input("Enter the number n1:"))
n2=int(input("Enter the number n2:"))
n3=int(input("Enter the number n3:"))
if n1>n2 and n1>n3:
    print("N1 is largest")
elif n2>n1 and n2>n3:
    print("N2 is largest")
else:
    print("N3 is largest")

#test2:Student Grade
mark=int(input("Enter your mark:"))
if mark>=90 and mark<=100:
    print("A")
elif mark>=80 and mark<=89:
    print("B")
elif mark>=70 and mark<=79:
    print("C")
else:
    print("Fail")

#test3:ATM Withdrawal Check
savings=1500
withdraw=int(input("Enter the amount:"))

if withdraw <= savings:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
balance =savings - withdraw
print(f"Here is your balance amount:{balance}")

#test4:Username Verification
stored_username="mohan"
name=input("enter your name:")
if name==stored_username:
    print("Verified")
else:
    print("Not verified")

#test5:Smart Student Result System
name=input("Enter your name:")
mark=int(input("Enter your mark:"))
print("-----Smart Student Result System-----")
print(f"Name : {name}")
print(f"Marks : {mark}")
if mark>=90 and mark<=100:
    print("Grade : A")
    print("Result : Pass")
elif mark>=80 and mark<=89:
    print("Grade : B")
    print("Result : Pass")
elif mark>=70 and mark<=79:
    print("Grade : C")
    print("Result : Pass")
else:
    print("Grade : F")
    print("Result : Fail")
    
