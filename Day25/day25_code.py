# Challenge -  Build a Pydantic model for a user profile with fields for name, email, and age, including validation for email format and age range (18–100)

from pydantic import BaseModel, EmailStr, validator

class UserProfile(BaseModel):
    name: str
    email: EmailStr
    age: int

    @validator('age')
    def validate_age(cls, value):
        if not 18 <= value <= 100:
            raise ValueError('Age must be between 18 and 100')
        return value

    def display(self):
        print("Valid User Profile:")
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

# Example
user = UserProfile(name="Sakhi", email="schatterjee14759@gmail.com", age=24)
print(user.display())
