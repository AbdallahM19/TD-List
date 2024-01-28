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

def print_tasks():
    """Print out my tasks."""
    print("My tasks are:")
    for i, task in enumerate(tasks, 1):
        print("{}. {}".format(i, task))

def td_list_app():
    """ Main function for the To-do list application. """
    print("Welcome to your Task Manager app!")
    while True:
        print("\n-------------------------\n")
        print_tasks()
        print("\n-------------------------\n")
        file = input("Enter your Task, please !!: ")
        if file not in tasks:
            print("1. Add task to your list")
            print("2. Remove task from the list")
            print("5. Exit from the app-list")
            i = input("Enter the number to choose: ")
            if i  == "1":
                add_task(file)
            elif i == "2":
                remove_task(file)
            elif i.lower in ["quit", "esc", "5"]:
                print("Exiting the Task Manager app. Goodbye!")
                break
            else:
                print("This '{}' command is invalid.".format(i))
        else:
            print("Task '{}' already exists in your task list".format(file))

"""test app"""
if __name__ == "__main__":
    td_list_app()
