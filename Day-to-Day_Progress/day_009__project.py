#-----------------------------------------------------------------------------------------------------------------------------------

# Day 9 Main Project (Student Result Calculator V1)
print("Day 9 Main Project (Student Result Calculator V1) \n\n")

"""
Create functions:
    calculate_total(marks)
    calculate_average(total,subjects)
    check_grade(average)

Take marks of 5 subjects

Display:
    Marks : [ ]
    Total : __
    Average : __
    Grade : __

Grade rules:
    Average ≥90 → A
    Average ≥70 → B
    Average ≥50 → C
    Otherwise → Fail


# Bonus Challenge 

Add one more function:
    student_status(average)

Rules:
    Average ≥90 → Excellent Student    
    Average ≥70 → Good Student    
    Otherwise → Needs Improvement
"""

#-----------------------------------------------------------------------------------------------------------------------------------

### PROJECT WORK BEGINS ### 

# Extra requirements for the clean input/output interfere.
prompts = [
    ">>> Enter Your Subject Marks (out of 100)", #0
    "Mathematics", #1
    "Physics", #2
    "Chemistry", #3
    "Biology", #4
    "English" #5
]
final_outputs = [
    "_______________ STUDENT REPORT _______________", #0
    "Marks (subject wise)", #1
    "Total Marks", #2
    "Average Marks", #3
    "Grade",#4
    "Status" #5
]
std_details = ["",[],] # storing student details.


# total subject for avg function
subjects = len(prompts) - 1

# Creating marks placeholder variable
sub_marks = []



# ---------------------------------------------------------------
## Defining the user_input function (no error format)

def user_input():
    print(prompts[0])
    
    # for loop to generate user inputs
    for i in range(1, len(prompts)):
        user_marks = int(input(f"{prompts[i]: <15} : "))
        
        # sentence statement to enter valid marks/values.
        if (user_marks < 0) or (user_marks > 100):
            print("\n Please Enter Valid Marks")
            print("\n SHUTTING DOWN ")
            exit() # Closes the terminal session completely
        else:
            std_details[1].append(user_marks)
            sub_marks.append(user_marks) #storing the values in marks list.

user_input() # calling the function to use the values(marks) for further code.

print("\n\n")
# ---------------------------------------------------------------
## Creating Required Functions

# Function to Calculate Total Marks
def calculate_total(sub_marks):
    total_marks = sum(sub_marks)
    std_details.append(total_marks)
    return total_marks 
# Creating Total Marks instance.
final_t_marks = calculate_total(sub_marks)

# Fucntion to Calculate Avg Marks 
def calculate_avg(final_t_marks,subjects):
    avg_marks = final_t_marks / subjects
    std_details.append(avg_marks)
    return avg_marks
# Creating Avg Mark instance.
final_avg_marks = calculate_avg(final_t_marks,subjects)

# Fucntion to Check Grade
def calculate_grade(final_avg_marks):
    if final_avg_marks >= 90:
        std_grade = "A"
    elif final_avg_marks >= 70:
        std_grade = "B"
    elif final_avg_marks >= 50:
        std_grade = "C"
    else:
        std_grade = "Fail"
    std_details.append(std_grade)
    return std_grade
# Creating Student Grade instance.
student_grade = calculate_grade(final_avg_marks)
 
# Bonus Challenge, Function to define Student Status
def student_status(final_avg_marks):
    if final_avg_marks >= 90:
        std_stats = "Excellent Student"
        std_details.append(std_stats)
    elif final_avg_marks >= 70:
        std_stats = "Good Student"
        std_details.append(std_stats)
    else:
        std_stats = "Need Improvement"
        std_details.append(std_stats)
    return std_stats
# Creating Student Status instance 
std_status = student_status(final_avg_marks)


## Now displaying Output
def show_output():
    print(f"{final_outputs[0]}")
    for i in range(1,len(std_details)):
         print(f"{final_outputs[i]: <22} : {std_details[i]}")

# Final Call:
show_output() 


#-----------------------------------------------------------------------------------------------------------------------------------







