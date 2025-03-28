import datetime
from config import DATETIME_FORMAT, STATUS_DICT

class Task:
    """Class representing a task in the task manager"""
    
    def __init__(self, title, description="", category='inbox', priority=0, action_date=None, 
                deadline=None, status='pending', estimated_duration=0, real_duration=0, 
                last_updated=None, created_at=None, task_id=None):
        """Initialize a new Task object."""
        self.task_id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.action_date = action_date
        self.deadline = deadline
        self.status = status
        self.estimated_duration = estimated_duration
        self.real_duration = real_duration
        self.last_updated = last_updated or datetime.datetime.now().strftime(DATETIME_FORMAT)
        self.created_at = created_at or datetime.datetime.now().strftime(DATETIME_FORMAT)
    
    def __str__(self):
        """Return a string representation of the task"""
        status_symbol = STATUS_DICT[self.status]
        action = f"({self.action_date})" if self.action_date else ""
        deadline_str = f"〆 {self.deadline}" if self.deadline else ""
        return f"{self.task_id}. [{status_symbol}] {self.title} {action} {deadline_str}"
    
    def update_status(self, new_status):
        """Change the task status"""
        self.status = new_status
        return self
    
    def to_dict(self):
        """Convert the task to a dictionary for database operations"""
        return {
            'task_id': self.task_id,
            'title':self.title,
            'description': self.description,
            'category': self.category,
            'priority': self.priority,
            'action_date': self.action_date,
            'deadline': self.deadline,
            'status': self.status,
            'estimated_duration': self.estimated_duration,
            'real_duration': self.real_duration,
            'last_updated': self.last_updated,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_db_row(cls, row):
        """Create a Task object from a database row"""
        if not row:
            return None
            
        task_id, title, description, category, priority, action_date, deadline, status, estimated_duration, real_duration, last_updated, created_at = row
        return cls(
            title=title,
            description=description,
            category=category,
            priority=priority,
            action_date=action_date,
            deadline=deadline,
            status=status,
            estimated_duration=estimated_duration,
            real_duration=real_duration,
            last_updated=last_updated,
            created_at=created_at,
            task_id=task_id
        )