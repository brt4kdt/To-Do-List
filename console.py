import main
import datetime

console_manager = main.ToDoList()
user_input = 6
command_choices = ['Task Manager Menu:', 'Add Task',
                   'Remove Task', 'Mark Task as Done',
                   'Add Subtask', 'Set Deadline',
                   'Print Tasks', 'Exit']


def print_menu():
    for i, choice in enumerate(command_choices):
        if i == 0:
            print(choice)
        else:
            print(f'    {i}. {choice}')

print_menu()

while True:
    try:
        user_input = int(input("Enter a number: "))

    except ValueError:
        # If ValueError occurs, print an error message and continue the loop
        print("Please enter a valid number.")
    #
    # finally:

    if user_input == 1:
        title = input("Enter task title: ")
        deadline = input("Enter task deadline (YYYY-MM-DD): ")
        if deadline:
            deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
        console_manager.add_tasks(title, deadline)
        print_menu()

    elif user_input == 2:
        console_manager.print_tasks()
        index = int(input("Enter task number to remove: ")) - 1
        console_manager.delete_task(index)
        print_menu()

    elif user_input == 3:
        console_manager.print_tasks()
        index = int(input("Enter task number to mark as done: ")) - 1
        console_manager.mark_as_done(index)
        print_menu()

    elif user_input == 4:
        console_manager.print_tasks()
        index = int(input("Enter task number to add subtask: ")) - 1
        subtask_title = input("Enter subtask title: ")
        console_manager.add_subtasks(index, subtask_title)
        print_menu()

    elif user_input == 5:
        console_manager.print_tasks()
        index = int(input("Enter task number to set deadline: ")) - 1
        deadline = input("Enter new deadline (YYYY-MM-DD): ")
        if deadline:
            deadline = datetime.datetime.strptime(deadline, '%Y-%m-%d').date()
            console_manager.change_deadline(index, deadline)
            print_menu()

    elif user_input == 6:
        console_manager.print_tasks()

    elif user_input == 7:
        console_manager.save_to_file()
        print("Exiting Task Manager. Your tasks have been saved.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
