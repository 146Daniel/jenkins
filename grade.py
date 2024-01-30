grade = int(input("what is your grade? "))


if grade >= 90:
    print("your grade in A ")
elif 80 <= grade < 90:
    print("your grade is B ")
elif 70 <= grade < 80:
     print("your grade is C ")
elif 60 <= grade < 70:
    print("your grade is D ")
elif grade < 60:
    print("your grade is F ")