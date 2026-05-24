#-----------------------------------------------------------------------------------------------------------------------------------

# Day 5 Main Project (Student Marks Manager V1)
print("Day 5 Main Project (Student Marks Manager V1) \n\n")

"""
Take marks of 5 subjects and store in a list.
Calculate:
    Total marks
    Average marks
    Highest marks
    Lowest marks

# Bonus Challenge 
Add:
    Average ≥90 → Excellent
    Average ≥70 → Good
    Otherwise → Needs Improvement
"""

subjects = ["Maths","Physics","Chemistry","Biology","English"]
marks = []

# to track n add marks subject wise.
for i in range(5):
    take = int(input(f"Enter '{subjects[i]}' marks : "))
    
    if take < 0 or take > 100:
        print("Invalid marks")
        
    marks.append(take)


marks_total = sum(marks)
marks_avg = sum(marks) / len(marks)
marks_max = max(marks)
marks_min = min(marks)


# Bonus challenge part
if marks_avg >= 90:
    avg_status = "Excellent"
elif marks_avg >= 70:
    avg_status = "Good"
else:
    avg_status = "Needs Improvement"

# or another alternarive but not good one.
#avg_status = []
#if marks_avg >= 90:
#    avg_status.append("Excellent")
#elif marks_avg >= 70:
#    avg_status.append("Good")
#else:
#    avg_status.append("Needs Improvement")


print("\n\n")


# Final step, to show the Output:
print("""
=================================
  Student Report
================================= 
""")

print(f"Marks : {marks} \n")

print(f"Total Marks : {marks_total}/500")
print(f"Average Marks : {marks_avg}")
print(f"Highest Marks : {marks_max}")
print(f"Lowest Marks : {marks_min}")
print(f"Average Status : {avg_status}")

print("""
=================================
""")


#-----------------------------------------------------------------------------------------------------------------------------------




