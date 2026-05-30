#-----------------------------------------------------------------------------------------------------------------------------------

# Day 8 Main Project (Fixed Student Record System V1)
print("Day 8 Main Project (Fixed Student Record System V1) \n\n")

"""
Create a tuple:
    student = (
    "Alex",
    21,
    "Computer Science",
    95
    )

then print:
    Name 
    Age
    Department
    Marks

# Bonus Challenge

Check:
    Marks >=90 → Outstanding
    Otherwise → Good
"""

#-----------------------------------------------------------------------------------------------------------------------------------

## Project work Begins
name = input("Name : ")
age = int(input("Age : "))
dept =input("Department : ")
marks = int(input("Marks : "))

# creating Student Tuple (for user input):
student = (name, age, dept, marks)
print("") # just for line spacing in output

# Error Handling by using Selection conditions.
if age > 100 or age < 0:
    print("Invalid Age!! Please Enter Valid Age!!")
elif marks >100 or marks<0:
    print("Invalid Marks!! Please Enter Valid Marks!!")

else: # Using Nested Condition        
    if marks >= 90:
        status = "Outstanding"
    elif marks >= 50:
        status = "Good" 
    else:
        status = "Poor"

    # Displaying Outputs
    print(f"------------------- Student Record ------------------- \n")
    
    print(f"Name : {student[0]}")
    print(f"Age : {student[1]}")
    print(f"Department : {student[2]}")
    print(f"Marks : {student[3]}")
    print(f"Status : {status}")
    
    
#-----------------------------------------------------------------------------------------------------------------------------------

## Or acces the Student records Alternatively ( Note: Everything is still in Nested Condition to avoid the errors.)
    
    print(f"\n----------- Student Record (Using Alternative Way)----------- \n")
    # By using cleaner technique called tuple unpacking:
    name, age, dept, marks = student

    # Now simply call out variables
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Department : {dept}")
    print(f"Marks : {marks}")
    print(f"Status : {status}")

# Both the ways works same in output results, But the second is more efficient, Because this becomes very useful later in databases, loops, data analysis, APIs.


#-----------------------------------------------------------------------------------------------------------------------------------


