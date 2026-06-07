# Project Works ( FOUNDATION LEVEL )

          ### FIRST PROJECT ###

## Personal Expense Tracker V1 ##
"""
>>> guided project work <<<

Project Structure :-

Expense Tracker / Records
├
├── Create file if not exists       ✓
├── Show Menu                           ✓
├── Rebuild system                    ✓
├── Add Expense                         ✓
├── View Expenses                     ✓
├── Update Expenses                 ✓
├── Delete Expenses                   ✓
├── Show Total Spending          ✓
└── Exit                                          ✓
"""

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
### PROJECT BEGINS ###


# ----------------------------------------------------------------
# To create a loop, for better user interaction. we use "while True:" loop with "break" statement when condition is met. whether it is user who wants to exit , or if user enters wrong input data. it will break the function.


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
## HERE WE HAVE PREAMBLE CODES ##

# import operating system to check the files existence.
import os
from datetime import datetime

# create file name box  (very impt to work with multiple files with just one general code)  
file_name = "expenses.txt"    




## GENERAL UNTILITY FUNCTIONS ##

# Decor Header(s) function...
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
width = 60 # global variable 

# works for both file and terminal.
def print_title(text): 
    return (
        "-" * width + "\n"
        + text.center(width, "-") + "\n"
        + "-" * width + "\n\n"
        )

def menu_title(text):
    return (
        "_"*width + "\n" 
        + text.center(width, "—")
        )

def selected_menu_title(text):
    return (
        text.center(width, "—")
        )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# create header ...
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main_header():
    with open(file_name, "w") as file_w:
            # here we give a permanent title.
            file_w.write(print_title(" Expense Tracker Records "))
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Date_Validation_simulator
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def date_validation(input_date):
    # Date
        # creates list of year,month,date by split at '-' symbol.
        parts = input_date.split("-")


        # checks if there is all three parts or not.
        if len(parts) != 3:
            print("Use format YYYY-MM-DD\n")
            return False

        # assign name to list element of date.
        year, month, day = parts

        # this checks the length of each year,month,date input. 
        if len(year) != 4:
            print("Year must contain exactly 4 digits.\n")
            return False
        
        if len(month) != 2:
            print("Month must contain exactly 2 digits.\n")
            return False
        
        if len(day) != 2:
            print("Day must contain exactly 2 digits.\n")
            return False

        # to check date is properly in numbered format. by using isdigit() method.
        if not (
            year.isdigit()
            and month.isdigit()
            and day.isdigit()
        ):
            print("Date must contain numbers only.\n")
            return False

        ## Now checking the each case for Correct Date format.  ( months and days )
        # For Months Limitation.
        if not (1 <= int(month) <= 12):
            print("Invalid month.\n")
            return False
        
        # For Days
        month_31 = (1,3,5,7,8,10,12)
        month_30 = (4,6,9,11)
        
        month_num = int(month)
        day_num = int(day)
        year_num = int(year)
        
        is_leap = (year_num % 400 == 0 or (year_num % 4 == 0 and year_num % 100 != 0)) # for Feb.
        
        # for Feb month Days limitation.
        if month == "02":
            if is_leap:
                if not (1 <= day_num <= 29):
                    print("February has maximum 29 days.\n")
                    return False
            else:
                if not (1 <= day_num <= 28):
                    print("February has maximum 28 days.\n")
                    return False
            
        # For 31 days Months limitations
        elif month_num in month_31:
            if not (1 <= day_num <= 31):
                print("Invalid day for this month.\n")
                return False            
             
        # For 30 days Months limitations.
        elif month_num in month_30:
           if not (1 <= day_num <= 30):
                print("Invalid day for this month.\n")
                return False


        return True # finally breaks while loop, when all if statements are satisfied.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def amount_validation(value):
        try:
            value = float(value)
            if value < 0:
                print("Amount cannot be negative.\n")
                return False
            
            else:
                return True
        
        except ValueError:
            print("Enter a valid amount.\n")
            return False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def category_validation(category):
        
        category = " ".join(category.split()).title()
        if category == "":
            print("Category cannot be empty.\n")
            return False
        else:
            return True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_current_time():
    return datetime.now().strftime(
    "%H:%M:%S")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Note : this system is build later so other functions doing same process of reordering data, is done multiple times .. ( will sort it out later PERHAPS °-°> )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rebuild_file():
    records = [] # new records list ... after operation is done

    with open(file_name, "r") as file_r:
        for line in file_r:

            # read data line and create a list of it's elements.
            if "|" in line:
                parts = [item.strip() for item in line.split("|")]

                # add data only in rebuild records which has ID numbers.
                if (len(parts) >= 5 and parts[0].isdigit()):
                    records.append(parts)

    records.sort(key=lambda record:(record[1],record[4])) # sorting records, using date & time..

    # now rebuild the whole file as sorted data file again.
    with open(file_name, "w") as file_w:
        file_w.write(print_title(" Expense Tracker Records "))

        current_date = "" # for date title check
        new_id = 1 # to create ids

        for record in records:
            expense_date = record[1]

            # this creates the header only if True:
            if expense_date != current_date:
                current_date = expense_date

                # if the date is new not the same.. then we create a sub header for the next day entery..
                file_w.write("\n\n" + f"DATE : {current_date}".center(width))
                file_w.write("\n"+ "_" * width + "\n")
                file_w.write(f"{'ID ': <3} | {'Date ': <10} | {'Category ':<12} | {'Amount':<10} | {'Time ':>1} \n")
                file_w.write("—" * width + "\n")

            # this rebuilds the whole file entry, as the data record is already sorted by date and time.. we only assign the new ids..
            file_w.write(
                f"{new_id:<3} | "
                f"{record[1]:<10} | "
                f"{record[2]:<12} | "
                f"{record[3]:<10} | "
                f"{record[4]:>1}  \n"
            )

            new_id += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#-------------------------------------------------------------------------------------------------------------------------------------
# Create File : This section is done ✓

def create_file():
    
    # this checks and creates the file in OS(operating system), only if the file doesn't exists in the same root directory as .py file. 
    if not os.path.exists(file_name):

            # here we give a permanent title 
            main_header()
            
create_file() # call/activate the function.
#-------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------
# Show Menu: This section is done ✓

# function to display instructions as a Menu to Proceed.
def show_menu():
    
    print(menu_title(" PERSONAL EXPENSE TRACKER "))
    
    # this section is for instruction box.
    print("\n> Kindly refer to the instructions below before proceeding:")
    print("• Write 'New' to Add Expense.  ")
    print("• Write 'Read' to View Expenses. ")
    print("• Write 'Edit' to Update Expenses. ")
    print("• Write 'Remove' to Delete Expenses. ")
    print("• Write 'Show' to Show Total Spending. ")
    print("• Write 'Exit' to Exit.  ")
    print("-"*width + "\n") # end line of instruction box.
    
show_menu() # to show menu instructions once only in the very start.. 

#-------------------------------------------------------------------------------------------------------------------------------------



# PART A ( part of Add Expense ) BEGINS
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# Generate Expense ID : This section is done ✓

def generate_expense_id():
    count = 0 # id numbering
    
    with open(file_name, "r") as file_r:
        for line in file_r:
            parts = line.split("|")
            if len(parts) >= 5 and parts[0].strip().isdigit(): # condition 
                count += 1
    return count + 1
#-------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
def selected_menu_add():

    print(selected_menu_title(" Selected Menu: ADD EXPENSE "))
    print("• To Stop Choose 'n' or 'y' to Continue, Adding New Expense.\n" )
    print("-"*width)

#-------------------------------------------------------------------------------------------------------------------------------------



# PART A: Add Expense System Complete (entry)
#-------------------------------------------------------------------------------------------------------------------------------------
# Add Expense : This section is done ✓


# main add expense system
def add_expense():
    
    # Category
    while True:
        category = input("Category : ")
        
        if category_validation(category):
            category = " ".join(category.split()).title()
            break
    
    # Amount
    while True:
        value = input("Amount : ").strip()
        if amount_validation(value):
            amount = float(value)
            break
        

    # Date
    while True:
        expense_date = input("Enter a date (YYYY-MM-DD) : ").strip()
        if date_validation(expense_date):
            break

    # Generate ID
    expense_id = generate_expense_id()

    # Time
    expense_time = get_current_time()

    # Save Record
    with open(file_name, "a") as file_a:
        file_a.write(
            f"\n{expense_id:<3} | "
            f"{expense_date:<10} | "
            f"{category:<12} | "
            f"{amount:.2f} | " # upto 2 decimal
            f"{expense_time:<8} "
        )

    print("\nExpense Added Successfully.\n")
    rebuild_file() # call rebuild to redesign file
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------



# PART B ( part of View Expenses ) BEGINS
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# Read Menu: This section is done ✓

def read_menu():
    print(selected_menu_title(" Selected Menu: VIEW EXPENSE "))
    print("> Follow the given instructions below to proceed :")
    print("• Write 'All' to View All Records")
    print("• Write 'Date' to Search By Date")
    print("• Write 'Menu' to Return To Main Menu")
    print("-"*width + "\n")

#-------------------------------------------------------------------------------------------------------------------------------------

# PART B ( part of View Expenses )
#-------------------------------------------------------------------------------------------------------------------------------------
# View All Records : This section is done ✓

def view_all_records():

    with open(file_name,"r") as file_r:
        content = file_r.read() # reads whole file

    print("")
    print(content)  # shows all data.
    print("")
    
    return
#-------------------------------------------------------------------------------------------------------------------------------------

# PART B ( part of View Expenses )
#-------------------------------------------------------------------------------------------------------------------------------------
# Search by Date : This section is done almost

def search_by_date():
    # verify date
    while True:
        search_date = input(
            "Enter Date (YYYY-MM-DD): "
        ).strip()
    
        if date_validation(search_date):
            break
    print(f"Fecthing your Expense Records of {search_date} ... \n")
    
    # this keeps track of date found in file. if found not even once this remains False.
    found = False

    with open(file_name,"r") as file_r:
        
        #title box for expenses (manually)
        print("_"*width)
        print(f"{'ID ': <7}  {'Date ': <9}   {'Category ':<13}  {'Amount':<11} Time " )
        print("_"*width)
        
        # it reads file line by line; using iterations
        for line in file_r: 
            parts = line.split("|") # splits file records line whenever it sees '|' , and converts them into list.
            
            # as of after split, we get atleast 5 elements, ID, Date, Category, Amount, time.
            if len(parts) >= 5 and parts[0].strip().isdigit() :
                file_date = parts[1].strip()
                
                # if the search date matches it prints
                if file_date == search_date:
                    print(line.strip())
                    
                    # if found even one entery of required date, then it becomes true.
                    found = True
        print("-"*width + "\n")
            
    # here 'not' reverses the found case. 
    # ex: if not False: -> if True: -> runs 
    # we can also use, if found == False:
    if not found:
        print("No records found.\n")
#-------------------------------------------------------------------------------------------------------------------------------------

# PART B: View Expense System Complete (Read)
#-------------------------------------------------------------------------------------------------------------------------------------
def read_expenses():
    
    read_menu() # to call the read menu only once.
    
    # loop for the user continuous query.
    while True:
        option = input(
            "\nChoose how you would like to proceed : "
        ).strip().lower()

        if option == "all":
            print("Fetching all yours Personal Expense Records... ")
            view_all_records()
            
        elif option == "date":
            search_by_date()
            
        elif option == "menu":
            print("Returning back to main menu.\n\n" + "—" * width + "\n" + "—" * width + "\n\n")
            break
        else:
            print("\nInvalid Option.")
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------



# PART C ( part of Delete Expense ) BEGINS
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# show all expenses before removal.
def display_expenses():
    with open(file_name, "r") as file_r:
        
        #title box for expenses. ( including entry time n updated status ..)
        print("_"*width)
        print(f"{'ID ': <7}  {'Date ': <9}   {'Category ':<13}  {'Amount':<11} Time " )
        print("_"*width)
        
        # prints the expense records only
        for line in file_r:
            parts = line.split("|")
            if len(parts) >= 5 and parts[0].strip().isdigit():
                print(line.strip())

        print("-"*60 + "\n")
#-------------------------------------------------------------------------------------------------------------------------------------

# PART C: Delete Expense system complete (remove)
#-------------------------------------------------------------------------------------------------------------------------------------
def remove_expense():
    # to be deleted, by it's unique ID
    delete_id = input("Enter Expense ID To Delete : ").strip()
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # now we store the left records in list.
    updated_records = []
    found = False
        
     # read file
    with open(file_name, "r") as file_r:
          # line by line , only expenses rocords.
          for line in file_r:
              # split line into parts.
              parts = line.split("|")

              if len(parts) >= 5 and parts[0].strip().isdigit():
                  # define id part.
                  expense_id = parts[0].strip()
    
                  # only delete if true.
                  if expense_id == delete_id:
                       found = True
                  else:
                       updated_records.append(parts)
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # if deleted, then rearrange ID numbers.
    if found:
         
          # 1st rewrite the Header.
          with open(file_name, "w") as file_w:
              # header of the file.
              file_w.write(print_title(" Expense Tracker Records "))
                
              # 2nd rearrange the data by unique ID
              for index, record in enumerate( updated_records, start=1):
                  file_w.write(
                            f"{index:<3} | "
                            f"{record[1].strip():<10} | "
                            f"{record[2].strip():<12} | "
                            f"{record[3].strip():<10} | "
                            f"{record[4].strip()}\n" )

          # successfull msg of deletion.
          print(f"Expense ID {delete_id} Deleted Successfully.\n")
          rebuild_file() # call rebuild to redesign file

    else:
           print("Expense ID Not Found. \n" )


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------



# PART D: Total Expenses System (show) Begins
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def show_total_spending():

    total_spending = 0
    total_records = 0

    with open(file_name, "r") as file_r:
        for line in file_r:

            parts = line.split("|")

            if len(parts) >= 5 and parts[0].strip().isdigit():
                amount_value = float(parts[3].strip())

                total_spending += amount_value
                total_records += 1

    print("\n" + "-" * width)
    print("TOTAL SPENDING REPORT".center(width))
    print("-" * width)

    print(f"\nTotal Expense Records : {total_records}")

    print(f"Total Spending : ₹{total_spending:.2f}" )

    print( "-" * width + "\n")

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------



# PART E ( part of Edit Expenses ) BEGINS
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def selected_menu_edit():

    print(selected_menu_title(" Selected Menu: EDIT EXPENSE "))
    print("• Enter Expense ID To Update")
    print("• Press Enter To Keep Existing Value")
    print("-" * width)
#-------------------------------------------------------------------------------------------------------------------------------------

# PART D: Edit Expense System (show) Begins
#-------------------------------------------------------------------------------------------------------------------------------------
def edit_expense():
    display_expenses() # for an overview 

    edit_id = input(
        "\nEnter Expense ID To Edit : "
    ).strip()

    found = False
    updated_records = []

    # read file data records, one by one
    with open(file_name, "r") as file_r:
        for line in file_r:

            # convert in list for each line of data.
            parts = line.split("|")

            # ensures the it's the data record only.. no header or other titles.
            if len(parts) >= 5 and parts[0].strip().isdigit():
                expense_id = parts[0].strip()

                if expense_id == edit_id:
                    found = True

                    # if true, then show current record for reference/verification.
                    print("\nCurrent Record")
                    print("-" * width)
                    print(f"Category : {parts[2].strip()}")
                    print(f"Amount   : {parts[3].strip()}")
                    print(f"Date     : {parts[1].strip()}")
                    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    # Validation for each, and condition to keep old data, with user input.
                    # Category 
                    while True:
                        new_category = input("\nNew Category : ").strip()
                        if new_category == "":
                            new_category_f = parts[2].strip()
                            break
                        if category_validation( new_category ):
                            new_category_f = " ".join(new_category.split()).title()
                            break
                    
                    # Amount
                    while True:
                        new_amount = input("New Amount : ").strip()
                        if new_amount == "":
                            new_amount_f = parts[3].strip()
                        if amount_validation( new_amount ):
                            new_amount_f = float( new_amount )
                            break
                    
                    # Date
                    while True:
                        new_date = input("New Date (YYYY-MM-DD) : ").strip()
                        if new_date == "":
                            new_date_f = parts[1].strip()
                        if date_validation(new_date):
                            new_date_f = new_date
                            break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    
                    # Saves updated record
                    parts[1] = new_date_f
                    parts[2] = new_category_f
                    parts[3] = f"{float(new_amount_f):.2f}"

                # when not true.. the record is stored as it is, in updated records. No changes 
                updated_records.append(parts)

    # when found False, This prints, as if ID is not found.
    if not found:
        print("Expense ID Not Found.\n")
        return
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Rewrite file
    with open(file_name, "w") as file_w:
        file_w.write(
            print_title(" Expense Tracker Records " ))

        for index, record in enumerate(  updated_records, start=1 ):

            file_w.write(
                f"{index:<3} | "
                f"{record[1].strip():<10} | "
                f"{record[2].strip():<12} | "
                f"{record[3].strip():<10} | "
                f"{record[4].strip()}\n"
            )

    rebuild_file() # final redesign whole file..

    print(f"\nExpense ID {edit_id} Updated Successfully.\n" )

#-------------------------------------------------------------------------------------------------------------------------------------#-------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------
## THESE PREAMBLE CODES WILL BE USED IN FINAL OUTPUT CODING SYSTEM ## 
#-------------------------------------------------------------------------------------------------------------------------------------




## FINAL CODE OUTPUT SYSTEM ##
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# done ✓


# using infinite loop, to continue the progress till user wants to exit. 
while True:
    # main menu        
    choice = input("\n\n\n\nPlease enter your preferred action: ").strip().lower() # using strip() removes unwanted characters from the beginning and end of a string. and lower() converts input in lowercase. 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if choice == "new":
        print(">>> Let's record a New Expense.\n")
        selected_menu_add()
        #add_expense() # this adds first expense
        # now here we ask for another expense to add or not.
        while True:
            ask = input("Do you want to Add New Expense (y/n) : ").strip().lower()
            if ask == "y" :
                add_expense()
            elif ask == "n":
                print("Returning back to main menu.\n\n" + "—" * width + "\n" + "—" * width + "\n\n")
                break
            else:
                print("Invalid Option please choose (y/n)\n")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    elif choice == "read":
        print(">>> Fetching your Expense Records Details... \n")
        read_expenses()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif choice == "edit":
        print(">>> Let's update an existing expense.\n")
        selected_menu_edit()
        
        while True:
            ask = input("Do you want to Edit Expense Record (y/n) : ").strip().lower()
    
            if ask == "y":
                edit_expense()
            elif ask == "n":
                print("Returning back to main menu.\n\n" + "—" * width + "\n"+ "—" * width + "\n\n" )
                break
    
            else:
                print("Invalid Option please choose (y/n)\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif choice == "remove":
        print(">>> Fetching your all Expense Records Details... ")
        print(">>> Select the expense you'd like to remove... ")
        print(">>> Enter '0' to Return to Main Menu... \n")
        
        while True:
            ask = input("Do you want to Delete Expense Record (y/n) : ").strip().lower()
            if ask == "y" :
                display_expenses()
                remove_expense()
            elif ask == "n":
                print("Returning back to main menu.\n\n" + "—" * width + "\n" + "—" * width + "\n\n")
                break
            else:
                print("Invalid Option please choose (y/n)\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif choice == "show":
        print(">>> Calculating your total spending...\n")
        show_total_spending()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif choice == "exit":
        print(">>> Thank you for using Personal Expense Tracker.")
        print("    Have a productive day!" + "\n\n" + "—" * width + "\n"+ "—" * width + "\n\n")
        break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print("\nI couldn't recognize that action.")
        print("Please choose one of the available options.\n")

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------







#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------










