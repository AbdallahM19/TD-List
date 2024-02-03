#!/usr/bin/python3
""" To Do List App """

import time
import json
from datetime import datetime, timedelta
import winsound

"""################################################"""
"""########### Functions To-Do List App ###########"""
"""################################################"""

def arrange_tasks():
    print("Do you want to sort it:")
    print("1- By alarm time?")
    print("2- A to Z?")
    print("3- Z to A?")
    i = input("Choose one: ")
    if i == '1':
        tasks_with_alarm = [task for task in tasks if 'alarm_time' in task and task['alarm_time'] is not None]
        tasks_without_alarm = [task for task in tasks if 'alarm_time' not in task or task['alarm_time'] is None]

        sorted_tasks = sorted(tasks_with_alarm, key=lambda x: x.get('alarm_time', ''))
        sorted_tasks += tasks_without_alarm

        display_tasks(sorted_tasks)
    if i == '2':
        sorted_tasks_az = sorted(tasks, key=lambda x: x.get('task', '').lower())
        display_tasks(sorted_tasks_az)
    if i == '3':
        
        sorted_tasks_za = sorted(tasks, key=lambda x: x.get('task', '').lower(), reverse=True)
        display_tasks(sorted_tasks_za)

def is_valid_time(time_str):
    """Check if the time string is a valid time."""
    try:
        time.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def check_alarms():
    current_time = datetime.now().strftime("%H:%M")
    for task in tasks:
        alarm_time = task.get('alarm_time')
        if alarm_time and is_valid_time(alarm_time) and alarm_time == current_time:
            print(f"Alert: It's time for task '{task['task']}' at {alarm_time}!")
            play_alert_sound() 


def play_alert_sound():
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def alarm_time_is_vaild(alarm_time):
    if len(alarm_time) == 4 and alarm_time.isdigit():
        return ":".join([alarm_time[:2], alarm_time[2:]])
    elif " " in alarm_time:
        return ":".join([alarm_time[0:2], alarm_time[3:]])
    elif alarm_time[2] == ":":
        return alarm_time
    else:
        print(f"Invalid ({alarm_time}).")
        return alarm_time

def add_task(task, alarm_time=None):
    """ Add a task to the list. """
    if alarm_time:
        alarm_time = alarm_time_is_vaild(alarm_time)
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
    if alarm_time:
        alarm_time = alarm_time_is_vaild(alarm_time)
        if not is_valid_time(alarm_time):
            print("Invalid time format. Please enter a valid time in {} format.".format(alarm_time))
            alarm_time = input("please provide valide time: ")
    else:
        print("Alarm time not provided. Please provide a valid alarm time.")
        return
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

