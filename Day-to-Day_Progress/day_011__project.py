import os # required for clean format

#-----------------------------------------------------------------------------------------------------------------------------------

# Day 11 Main Project (Student Record Saver V1)
print("Day 11 Main Project (Student Record Saver V1) \n\n")

"""
Take input:
    Name
    Age
    Department
    Marks

Store into:
    student_records.txt

Format:
    Name: Nobhino
    Age:21
    Department:CSE
    Marks:95

Then read file and display all records.


## Bonus Challenge 

Add:
    Marks ≥90 → Outstanding
    Otherwise → Regular

Store status in file too:
    Status: Outstanding


## personal requiment : to make it clean and always useful, with no errors to be found at base levels requirements.

"""

#-----------------------------------------------------------------------------------------------------------------------------------

## Main Project Begins

# ----------------------------------------------------------------
# PART A: Create the student_records.txt file.
"""
• run this code once, it creates the file in same root directory. Then comment it out, to prevent mistakenly deleting old content.
"""
#with open("student_records.txt","w") as  stdrc_w:
#    stdrc_w.write("        Student Records File \n")

# To solve this above issue, we have alternative method, by using import os ;
check_file = "student_records.txt"
if not os.path.exists(check_file):
    with open("student_records.txt","w") as  stdrc_w:
        stdrc_w.write("_"*25 + " STUDENT RECORDS LOG " + "_"*25 )
# this method requires no hardwork at all.


# ----------------------------------------------------------------
# PART B: Dynamically Count Existing Records to determine Topic ID

std_count = 1 # base default if file is empty.

with open("student_records.txt", "r") as  stdrc_r:
    file_content = stdrc_r.read()
    # counts how many times "Student #"
    std_count += file_content.count("Student #")


# ----------------------------------------------------------------
# PART C: Collect User Inputs with Clean Formatting.

print("\nEnter your Details ")
# required lists for input format
std_details = ["Name","Age","Department"]
std_subjects = ["Mathematics","Physics","Chemistry","Biology","English"]
std_marks = []
std_marks_only = [] # to calculate avg_marks for status.
std_final_details = []

# User input function, to store student details
def student_bio():
    # collecting student details
    for details in std_details:
        # to keep the data type correct
        if details == "Age":
            details_input = int(input(f"{details: <18} : "))
            std_final_details.append(details_input)
        else:
            details_input = input(f"{details: <18} : ").title() 
            std_final_details.append(details_input)
    return
student_bio()

print("\nEnter your Subjects Marks (out of 100)")
# User input function, to store Marks.
def mark_system():
    for sub in std_subjects:
        user_input = int(input(f"{sub: <18} : ")) 
        
        if user_input < 0 or user_input > 100:
            print("Please Enter Valid Marks")
            print("Shutting Down!!")
            exit() # use it wisely, bcz this kills the terminal, and shuts down the program.  
        else:
            std_marks.append(f"{sub:<15} : {str(user_input)}")
            std_marks_only.append(user_input)
    return # finish with function.
mark_system() # to call the function.

# Clean marks table with subject names.
mark_summary = "\n".join(std_marks)


# ----------------------------------------------------------------
# PART D: Bonus Challenge 

# total marks
marks_t = 0
for i in std_marks_only: # yeah i know, we can use sum() but it's a long story why i its like this :) 
    marks_t += i
#  total subjects 
sub_t = len(std_subjects)
# average marks of all subject
avg_marks = marks_t / sub_t

# conditiom for avg marks status 
if avg_marks >= 90:
    std_status = "Outstanding"
else:
    std_status = "Regular"
    

# ----------------------------------------------------------------
# PART E: Append with Clean Formatting

with open("student_records.txt","a") as stdrc_a:
    # adding data with initial border line and subtitle
    stdrc_a.write("\n\n\n" + "-"*71 + "\n")
    stdrc_a.write(f"{'-'*26 : <26} Student #{std_count} Entry {'-'*26 : >26} \n\n\n")
    
    stdrc_a.write("\n\n--------- Student Details --------- \n")
    # now here goes student details
    for i in range(len(std_details)):
        stdrc_a.write(f"{std_details[i]: <15} : {std_final_details[i]} \n")
    
    # adding status
    stdrc_a.write(f"{'Status': <15} : {std_status} \n")
    
    # marks sheet details
    stdrc_a.write("\n\n----- Student Marks Sheet ----- \n")
    stdrc_a.write(f"{mark_summary}")


# ----------------------------------------------------------------
# PART F: Final Read all file..

with open("student_records.txt","r") as stdrc_r:
    display_file = stdrc_r.read()

print(display_file)


#----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------






