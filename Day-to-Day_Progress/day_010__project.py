#-----------------------------------------------------------------------------------------------------------------------------------

# Day 10 Main Project (Student Club Registration V1)
print("Day 10 Main Project (Student Club Registration V1) \n\n")

"""
Take 5 student names from user.Store them in a set.

Display:
         Club Members (title)
    Members : __
    Total unique members : __

Purpose:
    If same student enters name twice,Output automatically removes duplicate entry values.


# Bonus Challenge 

Check:
    If total unique members >=5
    Status → Full Registration
    
    Otherwise
    Status → Duplicate Entries Found
"""

#-----------------------------------------------------------------------------------------------------------------------------------
## Project Work Begins


# Members Details in a list, useful to find dups in find_dup fucntion.
members = []

# For Entery user input 
def registration():
    c = 1
    while c <= 5:
        raw_entries = input(f"{c}. Entry : ")
        
        # this makes sure no white space makes the duplicate entries be unseen.
        clean_entries = " ".join(raw_entries.split()).title()
        # split() cuts out ALL messy spaces (front, back, and middle), converts in list.
        # 2. join() glues the words back together with exactly 1 space.
        
        members.append(clean_entries)
        c += 1
# Creating an instance for Registration
club_reg = registration()


# To count Unique members
unique_members = len(set(members))


# Bonus Challenge
def mem_status():
    if unique_members >=5:
        status = "Full Registration"
    else:
        status = "Duplicate Entries Found"
    return status
# Creating instance of member status
club_status = mem_status()


## An extra portion to decorate
seen = set()
dups = set()

def find_dup():
    for name in members:
        # to check dups in members
        if name in seen:
            dups.add(name)
        else:
            seen.add(name)
# Creating instance of find_dup
duplicates = find_dup()


print("")

# final output
print(f" {'_'*15: <15} {'Club Members':^15} {'_'*15: >15}   ")
print(f"{'Members':<22} : {members}   ")
print(f"{'Total Entries ':<22} : {len(members)}   ")
print(f"{'Total Unique Members':<22} : {unique_members}   ")
print(f"{'Status':<22} : {club_status}   ")
print(f"{'Duplicate Entries': <22} : {dups}")

#-----------------------------------------------------------------------------------------------------------------------------------








