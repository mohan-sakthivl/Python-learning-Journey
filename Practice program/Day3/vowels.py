#vowels
dream_job=input("Enter your dream job :")
first_letter=dream_job[0].lower()
if first_letter in "aeiou":
    article="an"
else:
    article="a"
print("I want to become",article,dream_job+".")