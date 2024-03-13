import os
import json

class Todo:
    def __init__(self):
        self.todos = []
        self.load_todos()

    def load_todos(self):
        if os.path.exists('todos.json'):
            with open('todos.json', 'r') as f:
                self.todos = json.load(f)

    def save_todos(self):
        with open('todos.json', 'w') as f:
            json.dump(self.todos, f, indent=4)

    def add_todo(self, title, description):
        new_todo = {
            'title': title,
            'description': description,
            'completed': False,
            'due_date': None
        }
        self.todos.append(new_todo)
        self.save_todos()

    def remove_todo(self, title):
        global_index = None
        for i, todo in enumerate(self.todos):
            if todo['title'] == title:
                global_index = i
                break
        if global_index is not None:
            self.todos.pop(global_index)
            self.save_todos()

    def complete_todo(self, title, completed=True):
        for todo in self.todos:
            if todo['title'] == title:
                todo['completed'] = completed
                self.save_todos()
                break

    def print_todos(self):
        for todo in self.todos:
            print(f"{todo['title']}-{todo['description']} - {'Completed' if todo['completed'] else 'Not Completed'}")

    def edit_todos(self, index, title=None, description=None, due_date=None, completed=None):
        if 0 <= index < len(self.todos):
            todo = self.todos[index]
            if title:
                todo['title'] = title
            if description:
                todo['description'] = description
            if completed is not None:
                todo['completed'] = completed
            self.save_todos()
        else:
            print("Invalid index")

def main():
    todo_app = Todo()
    while True:
        print("\n1. Add Todo")
        print("2. Remove Todo")
        print("3. Complete Todo")
        print("4. Print Todos")
        print("5. Edit todos")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter todo title: ")
            description = input("Enter todo description: ")
            todo_app.add_todo(title, description)
        elif choice == '2':
            title = input("Enter todo title to remove: ")
            todo_app.remove_todo(title)
        elif choice == '3':
            title = input("Enter todo title to mark as completed: ")
            completed = input("Enter completed status: ")
            todo_app.complete_todo(title, completed)
        elif choice == '4':
            todo_app.print_todos()
        elif choice == '5':
            index = int(input('Enter todo index: '))
            title = input('Enter new todo title: ')
            description = input('Enter new todo description: ')
            todo_app.edit_todos(index, title, description)
        elif choice == '6':
             break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()