#-----------------------------------------------------------------------------------------------------------------------------------

# Day 2 Main Project (Student Grade Analyzer V1)
print("Day 2 Main Project (Student Grade Analyzer V1) \n\n")

"""
Take input:
    Student name
    Marks
Rules:
    90+ → A Grade
    70-89 → B Grade
    50-69 → C Grade
    Below 50 → Fail
"""

s_name = input("Enter you name : ")
s_marks = int(input("Enter you Maths Subject Marks : "))
print("")

print("""
=================================
  Student Result ( in maths )
================================= 
""")

# Student Name
print(f"Name : {s_name}")

# Student Marks ( in maths )
print(f"Marks : {s_marks}")

# Grade Declaration.
if s_marks > 100 or s_marks < 0:
    print("!! Please Enter Valid Marks !!")
elif s_marks >= 90:
    print("Grade : A")
elif s_marks >= 70:
    print("Grade : B")
elif s_marks >= 50:
    print("Grade : C")
else:
    print("Grade : Fail")

print("""
=================================
""")
print("\n\n\n")

#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

# Tiny Upgrade Challenge (before Day 3 unlock)
print("Modify your Student Grade Analyzer V1 into V2 \n\n")
"""
Modify your Student Grade Analyzer V1 into V2

Add:
    95-100 → Outstanding
    90-94 → A Grade
    70-89 → B Grade
    50-69 → C Grade
    Below 50 → Fail    
Output should become:
    ==================
                RESULT
    ==================
    Name: Nitin
    Marks: 96
    Grade: Outstanding
"""


print("""
=================================
  Student Result ( in maths )
================================= 
""")

# Student Name
print(f"Name : {s_name}")

# Student Marks ( in maths )
print(f"Marks : {s_marks}")

# Grade Declaration.
if (s_marks > 100) or (s_marks < 0):
    print("!! Please Enter Valid Marks !!")
elif s_marks >= 95:
    print("Grade : Outstanding")
elif s_marks >= 90:
    print("Grade : A")
elif s_marks >= 70:
    print("Grade : B")
elif s_marks >= 50:
    print("Grade : C")
else:
    print("Grade : Fail")

print("""
=================================
""")


 #-----------------------------------------------------------------------------------------------------------------------------------
 
 
 
 
 