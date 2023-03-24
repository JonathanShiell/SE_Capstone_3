#=====importing libraries===========
'''This is the section where you will import libraries'''
import re
from textwrap import fill

# Variables required at multiple points
# Text split patterns (using the re module)
task_split_pattern = "\n+"
sub_split_pattern = ",\s*"

# Let us also define global variables that are to be used within functions
# These are to be file names as required.
user_file = "user.txt" # Stores login and password of user.
tasks_file = "tasks.txt" # Stores tasks.
task_reports = "task_overview.txt" # Target for task report.
user_reports = "user_overview.txt" # Target for users report.

# Task attributes for formatted output, in the same order that the tasks are 
# stored in `tasks.txt`
attributes = ["Assigned to:", "Task:", "Task description:", "Date assigned",
                "Due date:", "Task complete"]
# Print order for the above:
display_order = [1, 0, 3, 4, 5]

# Additional functions:
def print_line(n = 70):
    """ Prints a horizontal line, with blank lines above and below
* Line is 70 characters wide.
* Does not return any value. Returns None (a non-type object).
    """
    print()
    print("─" * n)
    print()
    
# Compare dates
def compare_dates (date1, date2):
    """Compares two dates
    
Accepts two string arguments of dd MMM yyyy, where the days and years are in 
numerals and the month is in the three character written format.

Returns:
*-1 if date1 previous to date2,
* 0 if both if the same,
* 1 if date1 after date2. 

Case insensitive.
    """
    # If the input strings are the same, we can return 0 first
    # Others may be detected later
    if date1.lower() == date2.lower():
        return 0
    
    # Let us hard code the relevant months in, this is taken from a previous 
    # call to the calendar module (now not required) and cast to lower case.
    months = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    
    # Let us parse the dates using the .split() method, and then compare in turn:
    day1, month1, year1 = date1.lower().split()
    day2, month2, year2 = date2.lower().split()
    
    # Let us proceed over the values by most significant first:
    # Consider years
    if int(year1) > int(year2):
        return 1
    elif int(year1) < int(year2):
        return -1
    
    # Let us consider the month next, using the index of `months`
    if months.index(month1) > months.index(month2):
        return 1
    if months.index(month1) < months.index(month2):
        return -1
    
    # Let us consider days, finally:
    if int(day1) > int(day2):
        return 1
    elif int(day1) < int(day2):
        return -1

    # Anything that has reached this point is treated as the same
    return 0
       
# Let us define the functions in the specification:
# `reg_user`,

def reg_user():
    """This function registers new users.

Will return (no value returned) without registering a new user if:
* The logged-in user is not admin
* The user name is already registered
* The two passwords supplied do not match.

Does not return any value. Returns None (a non-type object).
    """
    # Print line for clarity at start
    print_line()
    
    if entered_username != "admin":
        print("This can only be performed by user:admin")
        # Print line for clarity
        print_line()
        # Leave function early
        return

    # Read in users, use global variable user_file
    with open(user_file, "r") as f:
        import_string = f.read()

    # Get list of existing users and passwords
    users = re.split(task_split_pattern, import_string)

    # Strip to create a list of strings where each string stores a unique
    # username.
    users = [re.split(sub_split_pattern,user_record)[0] for user_record
             in users]

    new_user = input("Please enter a new username: ")

    # Check that the username is not already in use
    if new_user in users:
        # Exit function early if username already used.
        print("User already in database, please try again")
        return
    
    new_password = input(f"Please enter a password for {new_user}: ")
    confirm_password = input("Please confirm the password: ")

    if new_password != confirm_password:
        print("Sorry, passwords do not match")
        return

    #Write new user to user file
    with open(user_file, "at") as f:
        f.write(f"\n{new_user}, {new_password}")

    # Confirm that the user has been registered.
    print("User", new_user, "registered OK")

    # Print line for clarity at end
    print_line()

def add_task():
    """A function to add a new task
Writes the task in the specified format, using the separator ", " to the file
whose name is stored in the global variable `tasks_file`.
    """

    print_line()

    # Read in the username of the person whom the task is assigned to
    intended_user = input("Please enter a user name to assign the task to: ")

    # Read in the title of the task
    task_title = input(
            "Please enter a the task title (title only at this step): ")

    # Read in the description of the task
    description = input("Please enter a the task description: ")

    # Read in the due date
    due_date = input("Please enter a due date, format e.g. 10 Oct 2019: ")

    # Confirm Current date
    current_date = input(
        "Please confirm the current date, format format e.g. 10 Oct 2019: ")

    # Form list to format into task string at next step
    new_task = [intended_user, task_title, description, due_date, 
        current_date, "No"]

    # Generate task string
    task_string = "\n" + ", ".join(new_task)

    # Write (append mode) tasks to file.
    with open(tasks_file, "at") as f:
        f.write(task_string)
    
    # Confirm task added OK to user
    print("Task added OK")

    print_line()

def view_all():
    """To view all tasks
This takes all the tasks stated in tasks.txt, and prints them in a 
user-friendly form.
* Does not return any value. Returns None (a non-type object).
    """
    
    # Now let us read in the task file, first in a string variable `tasks_import`.
    with open(tasks_file, "r") as f:
        tasks_import = f.read()
        
    #   Now let us create a list of strings, each of which contains the details 
    # of a task.
    #   This will be done by splitting at new line characters, the use of 
    # re.split enables blank lines to be ignored safely.
    task_list = re.split(task_split_pattern,tasks_import)

    # Now let us iterate over the list of single-task strings.
    for item in task_list:
        sub_list = re.split(sub_split_pattern, item)
        
        # Start by printing a horizontal line above the task details for 
        # clarity.
        print_line()
            
        # Print the details other than description, then the description. 
        # Using the attributes and the order of printing stored in `attributes`
        # and `display_order` respectively.
        for i in display_order:
            print (attributes[i].ljust(19), sub_list[i])
        # Let us use different formatting for the description, as per the 
        # specification.
        else:
            print(attributes[2])
            print(fill(sub_list[2], initial_indent = " "))
    else:
        # To run after the last task, prints blank lines with a horizontal line in between 
        # the last task.
        print_line()
            
def view_mine():
    """This allows a user to view tasks assigned to that user, and to mark as 
complete or edit some other details of the tasks.
    
* Does not return any value. Returns None (a non-type object).
    """
    # Let us first read in all the tasks. As they are in plain text, it will be 
    # possible to detect if the username is absent, then there are no tasks and 
    # report accordingly. 
    # Other instances of no tasks being assigned may occur, and are dealt with later
    with open(tasks_file, "r") as f:
        tasks_import = f.read()
        
    if entered_username not in tasks_import:
        
        # Print line at start for clarity, and also consistency with other sections.
        print_line()
        
        # Notify that no tasks are assigned if this point is reached.
        print("No tasks assigned to this user")
    
        # Print line at end for clarity, and also consistency with other sections.
        print_line()
        
        # Return to main menu
        return
        
    #   Now let us create a list of strings, each of which contains the details 
    # of a task.
    #   This will be done by splitting at new line characters, the use of 
    # re.split enables blank lines to be ignored safely.
    task_split_pattern = "\n+"
    task_list = re.split(task_split_pattern,tasks_import)
    
    # Let us perform a second test, as the username should be the first word in each line
    users_assigned = [word.split(', ')[0] for word in task_list]
    
    if entered_username not in users_assigned:
        
        # Print line at start for clarity.
        print_line()
        
        print("No tasks assigned to this user")
    
        # Print line at end for clarity.
        print_line()
        # Return to main program
        return
    
    # Initialise integer to count number of tasks assigned
    task_count = 0

    # Now let us iterate over the list of single-task strings.
    for item in task_list:
        sub_list = re.split(sub_split_pattern, item)
        
        # Skip over items not for user:
        if sub_list[0] != entered_username:
            continue
            
        # Start by printing a line above the task details for clarity, followed by a blank line
        print_line()
        
        # Print a task number - this will be `task_count` + 1
        print(f"Task number: {task_count + 1}")
        
        # Increment the variable task_count upwards by 1:
        task_count += 1
        
        # Print the details other than description, then the description.
        for i in display_order:
            print (attributes[i].ljust(19), sub_list[i])
        # Let us use different formatting for the description, as per the 
        # specification.
        else:
            print(attributes[2])
            print(fill(sub_list[2], initial_indent = " "))
    else:
        # To run after the last task, prints an extra line for clarity after 
        # the last task.
        print_line()
        
    # If no tasks assigned, print message
    if task_count == 0:
        print("No tasks assigned to this user")
        # Print line at end for clarity, and also consistency with other sections.
        print_line()
        # Return to main program
        return
    
    # Run sub-menu for further option, store as lower case in `option`.
    while True:
        option = input("""Please select a further option
    mt  mark the task as complete or 
    et   edit the task
    -1  return to main program
        """).lower()
        # If quitting, leave the function
        if option == "-1":
            print_line()
            return
        
        if option not in ["mt", "et"]:
            print("\nSorry, option not recognised. Please try again.\n")
            print_line()
            continue
        break
    
    print_line()
    
    """
    New list `task_strings_out` to take task strings, non-user tasks to pass through 
    unaltered Non-user tasks to pass through without being altered as task string.
    User tasks to be altered as required, then re-formed into a new task string.
    New task string will then be appended to the list, the whole file will be over-written.
    """    
    
    # Create list object, `task_strings_out`, to store new task strings
    task_strings_out = []
    
    # TODO - get number, use `task_count` reset to zero as a counter to match.
    # Therefore subtract 1 to match to_change and task_count
    if option == "et":
        to_change = int(input("Which task do you want to edit? ")) - 1
    else:
        to_change = int(input("Which task do you want to mark complete? ")) - 1
        
    print_line()
    
    # Reset task count to give index point to edit.
    task_count = 0

    # Iterate over task list to reach required task
    for item in task_list:
        sub_list = re.split(sub_split_pattern, item)
        # Append and skip if not assigned to user
        if sub_list[0] != entered_username:
            task_strings_out.append(item)
            continue
            
        # Append and skip if not the indexed task
        if to_change != task_count:
            task_strings_out.append(item)
            task_count += 1
            continue
            
        # When indexed task reached, alter sub_string components and append the
        # new task string instead of the old one.
        if option == "et":
            pass #TODO
            while True:
                option = input(""" Which aspect of the task do you wish to alter?
                           dd - To change the due date
                           un - Change the assigned user
                           """)
                
                if option in ["dd", "un"]:
                    break
                
            if option == "dd":
                print (f"The present due date is {sub_list[4]}")
                new_date = ""
                
                while new_date == "":
                    new_date = input("Please enter a new due date in the same format:")
                    if new_date == "":
                        print("Please enter a date then press [Return]/[Enter]")
                        
                sub_list[4] = new_date
                
            elif option == "un":
                pass
                print (f"This task is assigned to is {sub_list[0]}")
                new_assign = ""
                
                while new_assign == "":
                    new_assign = input("Please enter a new due date in the same format:")
                    if new_assign == "":
                        print("Please enter a date then press [Return]/[Enter]")
                    if new_assign not in user_logins:
                        print("User not found. Please try again.")
                        continue
                
                # Assign new user name to sub_list, prior to recomposing task string
                sub_list[0] = new_assign
                
        else:
            sub_list[5] = "Yes"
            
        # Recompose task string
        new_item = ', '.join(sub_list)
        task_strings_out.append(new_item)
        # Increment `task_count` to prevent further changes to this line
        task_count += 1
            
    # Re-form file string
    # New list will be converted into '\n'-separated string and over-written in file.
    new_file_string = "\n".join(task_strings_out)
    
    # Write to file, over-write existing file
    with open(tasks_file, "w") as f:
        f.write(new_file_string)
        
def get_reports():
    """Generates the reports `task_overview.txt` and `user_overview.txt`.
    
Only functions as such if called by user 'admin'

Does not return any value. Returns None (a non-type object).
    """
    # Confirm that the administrator is the logged-in user.
    if entered_username != "admin":
        # Print message and lines for clarity
        print_line()
        print("This function may only be used by user:admin")
        print_line()
        
        # Return out of function without producing the reports
        return
    
    # Confirm the date for which the report is required
    report_date = input("Please confirm the date required for the report in the format 01 0ct 2019: ")
    
    #### Generate `task_overview.txt` report
    # Calculate the measurements
    # Read in tasks
    with open(tasks_file) as f:
        tasks_import = f.read()
        
    # Let us split the task list into tasks and also store its length in another variable.
    # `task_list` stores the task strings, `task_count` is the total number of tasks
    task_list = re.split(task_split_pattern, tasks_import)
    task_count = len(task_list)
    
    # Form a list object of tasks, each of which is represented as a list
    split_tasks = [re.split(sub_split_pattern, task) for task in task_list]
    
    # Create a sub-list for completed tasks
    completed_task_list = [task for task in split_tasks if task[5].lower() == "yes"]
    
    # Create a sub-list for incomplete tasks
    incomplete_task_list = [task for task in split_tasks if task[5].lower() == "no"]
    
    # Create a sub-list for incomplete and overdue tasks
    overdue_task_list = [task for task in split_tasks if (task[5].lower() == "no") and
                         (compare_dates(report_date, task[4]) == 1)]
    
    # Calculate percentage of tasks that are incomplete
    proportion_incomplete = 100 * len(incomplete_task_list) / task_count
    proportion_overdue = 100 * len(overdue_task_list) / task_count
    
    # Format the report
    report_string = \
    f"""
Report date: {report_date}
    
The total number of tasks that have been generated and tracked using 
task_manager.py is {task_count}.
* The total number of completed tasks is {len(completed_task_list)}.
* The total number of uncompleted tasks is {len(incomplete_task_list)}.
* The total number of tasks that have not been completed and that are overdue is {len(overdue_task_list)}.
* The percentage of tasks that are incomplete is {proportion_incomplete:.1f}%.
* The percentage of tasks that are overdue is {proportion_overdue:.1f}%.
    """
    # Write the report to file:
    with open(task_reports, "w") as f:
        f.write(report_string)
        
    # Notify user of file output OK:
    print_line()
    print(f"{task_reports} generated OK")
    print_line()
    
    # Print to screen, followed by horizontal line.
    print(report_string)
    
    #### Generate `user_overview.txt` report
    # Write first line of text file at `user_reports` with date
    with open(user_reports, "w") as f:
        f.write(f"Report date: {report_date} \n")
    
    # Iterate per user
    for user in user_logins:
        # Write first lines for user:
        with open(user_reports, "a") as f:
            f.write(f"\nUser: {user} \n")
            f.write("=" * 30)
            f.write("\n")
            
        # Initialise counting variables: 
        allocated_count = 0 # For counting tasks allocated to the user
        completed_count = 0 # To count the number of completed tasks
        incomplete_count = 0 # To count the numbre of tasks that are not complete
        overdue_count = 0 # To count the number of overdue tasks
                
        for task in split_tasks:
            if task[0] != user:
                # Skip over if not allocated to user
                continue
            else:
                # Calculate the measurements
                # Add to count of tasks allocated
                allocated_count += 1
                # Complete and incomplete tasks
                if task[5].lower() == "yes":
                    completed_count += 1
                else:
                    incomplete_count += 1
                    # Also count overdue, which follows from incomplete
                    if compare_dates(report_date, task[4]) == 1:
                        overdue_count += 1
                        
        # Calculate percentages
        percent_allocated = 100 * allocated_count / task_count
        percent_completed = 0 if allocated_count == 0 else 100 * \
            completed_count/allocated_count
        percent_incomplete = 100 - percent_completed
        percent_overdue = 0 if allocated_count == 0 else 100 * \
            overdue_count/allocated_count
    
        # Format the report and write to file per user:
        with open(user_reports, "a") as f:
            f.write(f"Total tasks assigned: {allocated_count}\n")
            f.write(f"Proportion of tasks is {percent_allocated:.1f}%\n")
            f.write("Proportion of allocated tasks that have been completed: " +
                    f"{percent_completed:.1f}%\n")
            f.write("Proportion of allocated tasks that have not been completed: " +
                    f"{percent_incomplete:.1f}%\n")
            f.write("Proportion of allocated tasks that have not been completed and " + 
                    "are overdue: " + f"{percent_overdue:.1f}%\n")
            
    print_line()
    print(f"{user_reports} generated OK")
    print_line()
    
    # Print the generated file back to screen, then a horizontal line
    with open(user_reports, "r") as f:
        print(f.read())
    print_line()
    
def get_basic_stats():            
            
    print_line()
    """Prints basic statistics (numbers of users and tasks) to the screen.
    """

    if entered_username != "admin":
        # Notify user that they do not have the credentials to use this 
        # option.
        print ("This task may only be performed by user 'admin'")
        
        # Print horizontal line for clarity, then blank line
        print_line()
        # Return to main program
        return

    # Let us obtain the number of tasks, by reading in the task file, splitting 
    # to task strings and printing the number of task strings to screen:
    with open(tasks_file, "r") as f:
        tasks_import = f.read()
    task_list = re.split(task_split_pattern,tasks_import)
    print("The total number of tasks is", len(task_list))
    
    # Let us repeat this for the number of users, splitting by line and printing 
    # the number of users to screen.
    with open(user_file, "r") as f:
        users_import = f.read()
    # Let us split this into a list of user-password pairs
    user_pairs = [item.split(", ") for item in users_import.split('\n')]
    # Let us print a count to screen:
    print("The number of users registered is", len(user_pairs))
    
    # Print line at end for clarity, and also consistency with other sections.
    print_line()    

#====Login Section====
# Read in user names and passwords
# Let us hard-code the filename for re-use at various points in the program
# and ease of changing later.
user_file = "user.txt"

# Let us repeat this for the tasks file.
tasks_file = "tasks.txt"

#   Let us access the file `user.txt` and read in as a string, closing the 
# file automatically by using a `with` statement.
with open(user_file, "r") as f:
    users_import = f.read()
# Let us split this into a list of user-password pairs
user_pairs = [item.split(", ") for item in users_import.split('\n')]

# Let us now split the pairs and store all pairs in a dictionary object
user_logins = {pair[0] : pair[1] for pair in user_pairs}

# Ask for user name and password.
# Ask for username first, and check that it is a valid username.
while True:
    entered_username = input("Please enter your username: ")
    # Confirm that a valid username has been entered
    if entered_username not in user_logins:
        # Report username not found, and delete from memory to avoid confusion.
        print("User not recognised. Please try again")
        del(entered_username)
        continue
    # Leave loop if username is validated
    break
    
while True:
    entered_password = input("Please enter your password: ")
    
    # Check password, remain in loop until the correct password is provided.
    if entered_password != user_logins[entered_username]:
        print("Wrong password. Please try again")
        continue
    # Leave loop if password is correct
    break

# Print blank lines with a horizontal line in between for clarity

print_line()
               
# Beginning of main program loop
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user (admin only)
a - Adding a task
va - View all tasks
vm - view my task
st - View basic statistics (admin only)
gr - Generate reports (admin only)
e - Exit
: ''').lower()

    if menu == 'r':
        # Call function `reg_user` to register user
        reg_user()

    elif menu == 'a':
        # Call the add task function (defined above as `add_task`)         
        add_task()
        
    elif menu == 'va':
        # Call the view all function(defined above as `view_all`)
        view_all()

    elif menu == 'vm':   
        # Call the 'view mine' function (defined above as `view_mine`)
        view_mine()
    
    elif menu == 'gr':
        # Call the 'get reports' function (defined above as `get_reports`)
        get_reports()
    
    elif menu == 'st':
        # Call the 'get reports' function (defined above as `get_basic_stats`)
        get_basic_stats()
    
    elif menu == 'e':
        # Exit the program
        print_line()
        print('Goodbye!!!')
        print_line()
        break # Leave program loop.

    else:
        print_line()
        print("You have made a wrong choice, Please Try again")
        print_line()