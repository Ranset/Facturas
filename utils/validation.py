import re

class Validation():
    def __init__(self) -> None:
        pass


    def is_valid_email(self, email):
        pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
        return re.match(pattern, email) is not None
    
    def is_valid_password(self, password):
        if len(password) < 8:
            return False
        
        if not any(char.isdigit() for char in password):
            return False
        
        if not re.search("[@!#$%^&*()<>?/\|}{:]", password):
            return False
        
        return True