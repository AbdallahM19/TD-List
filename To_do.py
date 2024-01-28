#!/user/bin/python3

add_task = __import__('TD-List').add_task
remove_task = __import__('TD-List').remove_task
print_tasks = __import__('TD-List').print_tasks
task = input("Enter Task:")
add_task(task)
print_tasks(task)
remove_task(task)
