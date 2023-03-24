# Readme

## Description

A program for smaller organisations to help manage tasks assigned to each member of the team, with more features than Capstone Task 2. It should contain logic that can determine if a task is overdue, based on the current date and the due date of the task.

## Specification

A python script that does the following:

* Logs in a user, whose username and password are stored in the file `user.txt`

* Enables a logged-in user to add a task, view all tasks or view tasks assigned to themselves.

* Allows an administrator to register a new user. This is achieved by treating the user `admin` as the only administrator.

* Enable the administrator to view the total number of registered users and the total number of tasks, in a user-friendly manner.

* To produce reports `task_overview.txt` and `user_overview.txt` for the administrator, as described below:
  
  * `task_overview.txt` is to contain the total number of tasks, the numbers of completed and uncompleted tasks, and the number of uncompleted tasks that are overdue.
  
  * `user_overview.txt` is to contain the numbers of users registered and tasks recorded. For each user it is to contain the number of tasks and the percentage of total tasks assigned to that user and also the percentages of tasks assigned that are completed, uncompleted (regardless of due date) and both uncompleted and overdue.

These are to be accesible from a central menu. The program is to run in a loop until broken. The program is to call functions in order to perform these tasks.

## Usage

#### To Start the Program

This program requires Python 3 to be installed, the current version is available at [Download Python | Python.org](https://www.python.org/downloads/).

The program may be started from the command line as `python task_manager.py`. As it contains an indefinite loop, it may also be run by clicking on the icon for `task_manager.py` once python is installed and if it is the default program for `.py` files. Alternatively `task_manager.py` may be opened with Python once the latter is installed.

The menu option `e` (exit) may be used to leave via the main menu, or `CTRL+C` if necessary to leave from another point in the program. If invoked by clicking an icon, the window may be closed using `x` in the right hand corner as an alternative to `CTRL+C`.

#### To Use the Program

###### Menu Options

*Available to all users:*

* `a` - add task
* `va` - View all tasks. This displays all tasks.
* `vm` - Enables the logged-in user to view their assigned tasks. This displays the tasks that are assigned to the user.
* `e` - Exit the program

*Available to user **admin** only:*

* `r` - register (add) user. This prompts the user to enter their desired username and password.
* `st` - Get basic statistics (counts of total users and total tasks).
* `gr` - Generate basic reports.

###### To edit the associated data

To perform other changes to information stored, the files `user.txt` and `tasks.txt` may be edited directly. The data is stored in plain-text as follows:

* `user.txt` - contains `username, password` separated by a comma and one or more spaces. User records are separated by one or more new line (`\n`) characters.

* `tasks.txt` - contains `user(to which task is assigned), task title, task description, date assigned, date due, task completed?`, separated by separated by a comma and one or more adjacent spaces. Task records are separated by one or more new line (`\n`) characters.
