#!/usr/bin/python3
""" To Do List App """

import time
import json

"""################################################"""
"""########### Functions To-Do List App ###########"""
"""################################################"""

def arrange_tasks():
    tasks.sort(key=lambda x: x.get('alarm_time', ''))
    

def is_valid_time(time_str):
    """Check if the time string is a valid time."""
    try:
        time.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def add_task(task, alarm_time=None):
    """ Add a task to the list. """
    if alarm_time:
        if len(alarm_time) == 4 and alarm_time.isdigit():
            alarm_time = ":".join([alarm_time[:2], alarm_time[2:]])
        elif " " in alarm_time:
            alarm_time = ":".join([alarm_time[0:2], alarm_time[3:]])
        else:
            print(f"Invalid ({alarm_time}).")
        if alarm_time[2] == ":":
            if not is_valid_time(alarm_time):
                print("Invalid time format. Please enter a valid time in {} format.".format(alarm_time))
                return
            tasks.append({"task": task, "alarm_time": alarm_time})
            print("Setting an alarm for '{}' => [{}]".format(task, alarm_time))
    else:
        tasks.append({"task": task, "alarm_time": alarm_time})
        print("Adding '{}' to the task list.".format(task))
    save_task()

def remove_task(task):
    """ Remove a specified task from the list. """
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            print("Removing '{}' from the task list.".format(task))
            save_task()
            break
    else:
        print("Task ('{}') is not found in Tasks-List".format(task))

def display_tasks(tasks):
    """Print out my tasks."""
    print("My tasks are:")
    for i, task in enumerate(tasks, 1):
        print("{}. {} -> [{}]".format(i, task['task'], task['alarm_time']))

def set_alarm(task, alarm_time):
    """Set an alarm for a specific task."""
    for i in tasks:
        if i["task"] == task:
            i["alarm_time"] = alarm_time
            print("Alarm set for task '{}' => [{}]".format(task, alarm_time))
            save_task()
            break
        else:
            print("Task ('{}') is not found in Tasks-List".format(task))

def save_task():
    """Save Tasks to a file."""
    with open('list-Tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_task():
    """Load Tasks from a file."""
    try:
        with open("list-Tasks.json", "r")as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

"""#####################################"""
"""########### Main Function ###########"""
"""#####################################"""

tasks = load_task()

def td_list_app():
    """ Main function for the To-do list application. """
    print("Welcome to your Task Manager app!")

    while True:
        print("*"*20)
        print("1. Add task to your list")
        print("2. Remove task from the list")
        print("3. Print all tasks")
        print("4. Set alarm for a task")
        print("5. Arrange Tasks")
        print("6. Exit from the app-list")
        print("*"*20)
    
        i = input("Enter the number to choose: ")

        if i == "1":
            print("=> '{}'. Add task to your list".format(i))
            file = input("Enter your Task, please: ")
            existing_tasks = [t["task"] for t in tasks]
            if file not in existing_tasks:
                alarm_choice = input("Do you want to set an alarm for this task? (y/n): ")
                if alarm_choice.lower() in ["y", "yes"]:
                    alarm_time = input("Enter alarm time for task (e.g. '22:44'): ")
                    add_task(file, alarm_time)
                else:
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
            display_tasks(tasks)
            print("-"*25)

        elif i == "4":
            print("=> '{}'. Set alarm for a task".format(i))
            file = input("Enter your Task, please: ")
            alarm_time = input("Enter the alarm time (e.g., '14:30'): ")
            set_alarm(file, alarm_time)

        elif i == '5':
            arrange_tasks()
            display_tasks(tasks)

        elif i.lower() in ["quit", "esc", "6", "exit"]:
            print("=> '{}'. Exit from the app-list".format(i))
            print("Exiting the Task Manager app. Goodbye!")
            break

        else:
            print("This '{}' command is invalid.".format(i))


"""############################"""
"""########### Test ###########"""
"""############################"""

if __name__ == "__main__":
    td_list_app()
