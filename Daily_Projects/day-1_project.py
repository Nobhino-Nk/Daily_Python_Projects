# DAY - 1 Project (Student Information System V1)
"""
Requirements:
Take input:
    Student Name
    Roll Number
    Age
    Department
    Favorite Subject
"""

# Only to showcase the Project Name in Output terminal.
print("DAY - 1 Project (Student Information System V1) \n\n")

std_name = input("Enter your Name : ")
clg_roll_no = int(input("Enter your College roll number : "))
uni_roll_no = int(input("Enter your University roll number : "))
std_age = int(input("Enter your age :"))
std_dept = input("Enter your department : ")
std_fav_sub = input("Enter your favorite Subject : ")

current_year = 2026 # to calculate expected birth year.
birth_year = current_year - std_age

print("\n ---------------Student details---------------","\n")
print("Name : ",std_name)
print("College Roll no. : ", clg_roll_no)
print("University Roll no. : ",uni_roll_no)
print("Age : ",std_age)
print("Department : ",std_dept)
print("Favorite subject : ",std_fav_sub)
print("Estimated Birth Year : ",birth_year)
print("\n\n") # for lining space in outputs

###############################################################################################################
###############################################################################################################

#Micro Challenge (Required before Day 2)
"""
Create :-
    Student Information System V2
Add :-
    Student city
    Student hobby
Print :-
    Name, Age, Department, City, Hobby, Birth Year
"""

# Only to showcase the Project Name in Output terminal.
print("Micro Challenge (Required before Day 2) \n")

# User inputs to fetch data.
std_city = input("Enter you city/state : " )
std_hobby = input("What's your hobbies : ")

print("\n ---------------Student details--------------- \n")
print(f"Name : {std_name}")
print(f"Age : {std_age}")
print(f"Department : {std_dept}")
print(f"City/State : {std_city}")
print(f"Birth Year : {birth_year}")
print(f"Hobbies : {std_hobby}")







