import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        # Create a frame for the listbox
        self.listbox_frame = tk.Frame(self.root)
        self.listbox_frame.pack(padx=10,pady=5)

        # Create a listbox to display the tasks
        self.task_listbox = tk.Listbox(self.listbox_frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame for the entry and buttons
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack()

        # Create an entry to input new tasks
        self.task_entry = tk.Entry(self.entry_frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        # Create an add button to add tasks
        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.TOP,pady=5)

        # Create a delete button to delete tasks
        self.delete_button = tk.Button(self.entry_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.TOP,pady=5)

        # Create an edit button to edit tasks
        self.edit_button = tk.Button(self.entry_frame, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(side=tk.TOP,pady=5)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create a file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.exit_editor)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)


    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if len(selected_task_index) > 0:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if len(selected_task_index) == 1:  # Only one item is selected
            original_task = self.tasks[selected_task_index[0]]
            edited_task = simpledialog.askstring("Task Editor", "Enter the new task details:") or ""
            if edited_task != "":
                self.tasks[selected_task_index[0]] = edited_task
                self.update_task_listbox()


    def exit_editor(self):
        if messagebox.askokcancel("Quit?", "Do you want to quit?"):
            self.root.destroy()

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()