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

def print_tasks(task):
    """print out my tasks"""

    if task:
        print("My tasks are: {}".format(task))
