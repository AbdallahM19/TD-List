#!/usr/bin/python3
""" To Do List App """

tasks = []

def add_task(task):
    """ Add a task to the list. """
    tasks.append(task)
    print("Adding '{}' to the task list.".format(task))

def remove_task(task):
    """ Remove a specified task from the list. """
    if task in tasks:
        tasks.remove(task)
        print("Removing '{}' from the task list.".format(task))
    else:
        print("Task ('{}') is not found in Tasks-List".format(task))

def print_tasks(tasks):
    """Print out my tasks."""
    print("My tasks are:")
    for i, task in enumerate(tasks, 1):
        print("{}. {}".format(i, task))

def td_list_app():
    """ Main function for the To-do list application. """
    print("Welcome to your Task Manager app!")
    while True:
        print("*"*20)
        print("1. Add task to your list")
        print("2. Remove task from the list")
        print("3. Print all tasks")
        print("5. Exit from the app-list")
        print("*"*20)
        i = input("Enter the number to choose: ")
        if i == "1":
            print("=> '{}'. Add task to your list".format(i))
            file = input("Enter your Task, please: ")
            if file not in tasks:
                add_task(file)
            else:
                print("Task '{}' already exists in your task list".format(file))
        elif i == "2":
            print("=> '{}'. Remove task from the list".format(i))
            file = input("Enter your Task, please: ")
            remove_task(file)
        elif i == "3":
            print("=> '{}'. Print all tasks".format(i))
            print("-"*25)
            print_tasks(tasks)
            print("-"*25)
        elif i.lower == "quit" or i.lower == "esc" or i == "5":
            print("=> '{}'. Exit from the app-list".format(i))
            print("Exiting the Task Manager app. Goodbye!")
            break
        else:
            print("This '{}' command is invalid.".format(i))
            break


if __name__ == "__main__":
    td_list_app()
