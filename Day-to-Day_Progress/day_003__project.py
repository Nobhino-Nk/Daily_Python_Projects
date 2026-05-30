#-----------------------------------------------------------------------------------------------------------------------------------

# Day 3 Main Project (College Eligibility Checker V1)
print("Day 3 Main Project (College Eligibility Checker V1) \n\n")

"""
Take input:
    Student name
    Age
    Marks
    Attendance %
    
Rules:
    Age >=18
    AND
    Marks >=60
    AND
    Attendance >=75 → Eligible
    
    Otherwise → Not Eligible     

Bonus Challenge (Add nested conditions)
If student is eligible:
    Marks ≥90 → Scholarship Eligible
otherwise → No Scholarship
"""

# input details
name = input("Enter your name : ")
age = int(input("Enter your age : "))
marks = float(input("Enter your marks : "))
attendance = float(input("Enter your attendance(%) :"))

print("") # for spacing 

print("""
=================================
  Eligibility Result ( in maths )
================================= 
""")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Marks : {marks}")
print(f"Attendance : {attendance}%")

if (age >= 18) and (marks >= 60) and (attendance >= 75):
    print("Status : Eligible")
    
    #bonus task
    if marks >= 90:
        print("Scholarship Eligible : Yes")
    else:
        print("Scholarship Eligible : No")
    
else:
    print("Status : Not Eligible")


print("""
=================================
""")

#-----------------------------------------------------------------------------------------------------------------------------------


