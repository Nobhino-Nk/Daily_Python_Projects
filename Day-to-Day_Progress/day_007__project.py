#-----------------------------------------------------------------------------------------------------------------------------------

# Day 7 Main Project (Student Database V1)
print("Day 7 Main Project (Student Database V1) \n\n")

"""
Take input:
    name
    age
    department
    roll number
    Store everything inside one dictionary

Output: show Key-Value pairs

# Bonus Challenge

Add:
    If age <18:
        Status → Minor Student
    Otherwise:
        Status → Adult Student
"""

# Project begins
std_info = {}

# Uset inputs
print("====== User Details ======")

std_info["name"] = input("Name : ")
std_info["age"] = int(input("Age : "))

# Precaution for User input in Age.
if std_info["age"] < 0 or std_info["age"] > 100 :
    print("Please Enter a Valid Age !")
# using nested condition 
else: 
    std_info["department"] = input("Department : ")
    std_info["roll_number"] = input("Roll no. : ")
    
    # Bonus Challenge
    if std_info["age"] < 18:
        status = "Minor Student"
    else:
        status = "Adult Student"
    
    # Adding student status in dictionary
    std_info["student_status"] = status
    
    print("")
    
    # final output , calling Key-Value pairs
    for key,value in std_info.items():
        print(f" {key: <20}  :  {value} ")
     


#-----------------------------------------------------------------------------------------------------------------------------------



