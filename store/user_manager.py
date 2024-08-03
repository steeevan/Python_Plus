import hashlib
from store.customer import Customer
from store.admin import Admin

class UserManager:
    def __init__(self) -> None:
        self.users = {}    # dictionary to store users

    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self,user_id,name,email,password,user_type="Custimer"):
        if email in self.users:
            raise ValueError("User Already Exists")
        hashed_password = self.hash_password(password)
        if user_type == "Customer":
            user = Customer(user_id,name,email,hashed_password)
        elif user_type == "Admin":
            user = Admin(user_id,name,email,hashed_password)
        else:
            raise ValueError("Invalid user type")

        self.users[email] = user
        return user
    
    def authenticate_user(self,email,password):
        hashed_password = self.hash_password(password)
        user = self.users.get(email)
        if user and user.password == hashed_password:
            return user
        else:
            raise ValueError("Invalid email or password")
        


