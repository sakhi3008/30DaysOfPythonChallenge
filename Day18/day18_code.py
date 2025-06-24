#Challenge - Enforce a naming convention with a metaclass

class NamingConventionMeta(type):
    def __new__(cls, name, bases, class_dict):
        if not name[0].isupper():
            raise ValueError(f"Class name '{name}' must start with an uppercase letter.")
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=NamingConventionMeta):
    def progress(self):
        return "Challenge complete: My class follows the rules!"
 
             
# Test
obj = MyClass()
print(obj.progress())
