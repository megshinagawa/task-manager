import datetime
from config import DATE_FORMAT

def is_valid_date(date_str):
    """Validate if a string is in the correct date format."""
    try:
        datetime.datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False
