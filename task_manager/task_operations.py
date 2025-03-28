from database import get_connection
from config import STATUS_DICT
from task import Task

def add_task(task: Task):
    """Add new task to the database"""
    conn = get_connection()
    cursor = conn.cursor()

    # Insert the new task using the Task object data 
    cursor.execute('''
    INSERT INTO tasks (title, description, category, priority, action_date, 
    deadline, status, estimated_duration, real_duration, last_updated, created_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (task.title, task.description, task.category, task.priority, task.action_date,
          task.deadline, task.status, task.estimated_duration, task.real_duration, task.last_updated, task.created_at))
    
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    # Update the task with its new ID
    task.task_id = task_id
    
    print(f"Task '{task.title}' added successfully with ID {task_id}.")
    return task


def view_all_tasks(show_completed=False):
    """Display all tasks, with the option to show or hide completed tasks"""
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks"
    if not show_completed:
        query += " WHERE status != 'completed'"
    query += " ORDER BY action_date ASC"

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print('No tasks found.')
        return []
    
    # Convert database rows to Task objects 
    tasks = [Task.from_db_row(row) for row in rows]

    print("\n===== TASKS ======")
    for task in tasks: 
        print(task)

    return tasks

def view_task_details(task_id):
    """Display detailed information about a specific task"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()

    # Convert database row to Task object
    task = Task.from_db_row(row)

    if not task:
        print(f"No task found with ID {task_id}.")
        return None
    
    print("\n===== TASK DETAILS =====")
    print(f"ID: {task.task_id}")
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"CategoryL {task.category}")
    print(f"Priority: {task.priority}")
    print(f"Do Date: {task.action_date or 'Not set'}")
    print(f"Deadline: {task.deadline or 'Not set'}")
    print(f"Status: {task.status}")
    print(f"Estimated Duration: {task.estimated_duration}")
    print(f"Real Duration: {task.real_duration}")
    print(f"Updated: {task.last_updated}")
    print(f"Created: {task.created_at}")

    return task


def update_task_status(task_id, new_status):
    """Updates the task status"""
    conn = get_connection()
    cursor = conn.cursor()

    # Check validity of the new status
    if new_status not in STATUS_DICT.keys():
        print(f"'{new_status}' is nota a valid status.")
        return False
    
    # Check if the task exists and get it
    cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        print(f"No task found with ID {task_id}.")
        return False
    
    # Convert to Task object and update status 
    task = Task.from_db_row(row)
    task.status = new_status

    # Update the task in the database 
    cursor.execute("UPDATE tasks SET status = ? WHERE task_id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

    print(f"Task {task_id} status updated to {new_status}.")
    return True


def delete_task(task_id):
    """Delete a task from the database"""
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the task exists 
    cursor.execute("SELECT task_id FROM tasks WHERE id = ?", (task_id,))
    if not cursor.fetchone():
        conn.close()
        print(f"No task found with ID {task_id}.")
        return False
    
    # Delete the task
    cursor.execute("DELETE FROM tasks WHERE task_id = ?", (task_id,))
    conn.commit()
    conn.close()

    print(f"Task {task_id} deleted successfully.")
    return True
