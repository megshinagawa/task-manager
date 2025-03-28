from config import STATUS_DICT
from database import create_database
from input_validation import is_valid_date
from task import Task
from task_operations import (
    add_task,
    view_all_tasks,
    view_task_details,
    update_task_status,
    delete_task
)

def display_menu():
    """Display the main menu options"""
    print("\n===== TASK MANAGER =====")
    print("1. Add task")
    print("2. View all incomplete tasks")
    print("3. View all tasks")
    print("4. View task details")
    print("5. Update task status")
    print("6. Delete a task")
    print("0. Exit")
    return input("Enter your choice (0-6): ")

def get_task_details():
    """Get task details from user input"""
    title = input("Enter task title (required): ")
    description = input("Enter task description: ")

    category = input("Enter category: ")
    if category == "":
        category = 'inbox'
    
    priority = input("Enter priority: ")
    if priority == "":
        priority = 0
    else:
        priority = int(priority)

    action_date = input("Enter action date (YYYY-MM-DD): ")
    if action_date and not is_valid_date(action_date):
        print("Invalid date format. Action date set to None.")
        action_date = None

    deadline = input("Enter deadline (YYYY-MM-DD): ")
    if deadline and not is_valid_date(deadline):
        print("Invalid date format. Deadline set to None.")
        deadline = None

    status = input("Enter status: ")
    if status not in STATUS_DICT.keys():
        print("Invalid status. Status set to 'pending'.")
        status = 'pending'
    
    estimated_duration = input("Enter estimated duration in minutes: ")
    if estimated_duration == "":
        estimated_duration = 0
    else:
        estimated_duration = int(estimated_duration)

    return title, description, category, priority, action_date, deadline, status, estimated_duration

def run_app():
    """Run the task manager app"""
    create_database()

    while True:
        choice = display_menu()

        if choice == "0":
            print("Thank you for using Task Manager. Goodbye!")
            break

        elif choice == "1":
            title, description, category, priority, action_date, deadline, status, estimated_duration = get_task_details()
            task = Task(title, description, category, priority, action_date, deadline, status, estimated_duration)
            add_task(task)

        elif choice == "2":
            view_all_tasks(show_completed=False)
            
        elif choice == "3":
            view_all_tasks(show_completed=True)
            
        elif choice == "4":
            task_id = input("Enter task ID: ")
            if task_id.isdigit():
                view_task_details(int(task_id))
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "5":
            task_id = input("Enter task ID to update: ")
            new_status = input("Enter updated status: ")
            if task_id.isdigit():
                update_task_status(int(task_id), new_status)
            else:
                print("Invalid ID. Please enter a number.")
                
        elif choice == "6":
            task_id = input("Enter task ID to delete: ")
            if task_id.isdigit():
                delete_task(int(task_id))
            else:
                print("Invalid ID. Please enter a number.")
                
        else:
            print("Invalid choice. Please try again.")
