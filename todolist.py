import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg='grey')

        self.tasks = []

        self.frame = tk.Frame(self.root, bg='grey')
        self.frame.pack(pady=10)

        self.label_task_list = tk.Label(self.frame, text="Your Task", bg='grey')
        self.label_task_list.grid(row=0, column=0, padx=10)

        self.label_time_list = tk.Label(self.frame, text="Your Time", bg='grey')
        self.label_time_list.grid(row=0, column=1, padx=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, padx=10)

        self.time_listbox = tk.Listbox(self.frame, width=20, height=15)
        self.time_listbox.grid(row=1, column=1, padx=10)

        self.label_task = tk.Label(self.root, text="Enter Task:", bg='grey')
        self.label_task.pack(pady=5)

        self.entry_task = tk.Entry(self.root, width=40)
        self.entry_task.pack(pady=5)

        self.label_time = tk.Label(self.root, text="Enter Time:", bg='grey')
        self.label_time.pack(pady=5)

        self.entry_time = tk.Entry(self.root, width=10)
        self.entry_time.pack(pady=5)

        self.button_add_task = tk.Button(self.root, text="Add Task", command=self.addtask)
        self.button_add_task.pack(pady=5)

        self.button_remove_task = tk.Button(self.root, text="Remove Selected Task", command=self.removetask)
        self.button_remove_task.pack(pady=5)

    def addtask(self):
        task = self.entry_task.get()
        time = self.entry_time.get()
        if task != "" and time != "":
            self.tasks.append((task, time))
            self.updatetasklistbox()
            self.entry_task.delete(0, tk.END)
            self.entry_time.delete(0, tk.END)
            messagebox.showinfo("Success", "Your task has been added.")
        else:
            messagebox.showwarning("Warning", "You must enter both a task and a time.")

    def removetask(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.updatetasklistbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def updatetasklistbox(self):
        self.task_listbox.delete(0, tk.END)
        self.time_listbox.delete(0, tk.END)
        for task, time in self.tasks:
            self.task_listbox.insert(tk.END, task)
            self.time_listbox.insert(tk.END, time)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoList(root)
    root.mainloop()
