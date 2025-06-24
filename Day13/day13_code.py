#Challenge - Implement a stack with push, pop, and peek

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Current Stack:", self.stack)

# Testing the Stack
my_stack = Stack()

my_stack.push("www.google.com")
my_stack.push("www.github.com")
my_stack.push("www.linkedin.com")

print("Current Page:", my_stack.peek())   
print("Go Back:", my_stack.pop())         
print("Now on:", my_stack.peek())         
