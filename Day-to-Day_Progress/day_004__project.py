#-----------------------------------------------------------------------------------------------------------------------------------

# Day 4 Main Project (College Attendance Counter V1)
print("Day 4 Main Project (College Attendance Counter V1) \n\n")
 
"""
Take input:
    How many classes?
 
Then using a loop ask:
    Present? (P/A)
 
Count:
    Total Present
    Total Absent
    Attendance %
 
# Bonus Challenge
Add:
    Attendance >=75 → Good Attendance
    Otherwise → Low Attendance

"""

c = 1             # for incrementing while loop
count_a = 0 # to store Absent(s) value
count_p = 0 # to store Present(s) value
name = input("Your name : ")
total_classes = int(input("Total Classes : "))
print("")

print("Attendance Entry of each class (A/P) !!")
while c <= total_classes:
    attended = input(f"Class {c} : ")
    if attended.lower() == "a": # to count A
        count_a += 1
    elif attended.lower() == "p": # to count P
        count_p += 1        
   else:
        print("Invalid input")
    c += 1    

attendance_p = (count_p/total_classes)*100

print("")
print("""
=================================
   Attandance Report
================================= 
""")

print(f"Name           : {name}")
print(f"Present        : {count_p}")
print(f"Absent         : {count_a}")
print(f"Attendance     : {attendance_p}%")

if attendance_p >= 75:
    print(f"Status         : Good Attendance ")
else :
    print(f"Status         : Low Attendance ")


print("""
=================================
""")

#-----------------------------------------------------------------------------------------------------------------------------------




