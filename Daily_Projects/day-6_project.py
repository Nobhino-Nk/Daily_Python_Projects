#-----------------------------------------------------------------------------------------------------------------------------------

# Day 6 Main Project (Username Analyzer V1)
print("Day 6 Main Project (Username Analyzer V1) \n\n")

"""
Take username from user.

Display:
    Username
    Total characters
    First letter
    Last letter
    Uppercase version
    Lowercase version

Check:
    Length <5 → Weak username
    Otherwise → Good username

# Bonus Challenge
Check:
    If username contains spaces:
        Invalid Username
"""

# Starting 
username = input("Username : ")
print("")

# Bonus Challenge
if " " in username:
    print("Invalid Username")

# if user does not enter anything.
elif len(username) == 0:
    print("Username cannot be empty")

# Using Nested Condition, to avoid display invalid username.
else:
    print("------ Username Display ------ \n")
    
    # check username status
    if len(username) < 5:
        status = "Weak Username"
    else:
        status = "Good username"
    
    print(f"Username : {username}")
    print(f"Total Characters : {len(username)}")
    print(f"First Letter : {username[0]}")
    print(f"Last Letter : {username[-1]}")
    print(f"Uppercase : {username.upper()}")
    print(f"Lowercase : {username.lower()} \n")
    
    print(f"Username Status : {status}")


#-----------------------------------------------------------------------------------------------------------------------------------







