import tkinter as tk
import tkinter.messagebox
import pickle

main_window = tk.Tk()
main_window.title("My ToDo App")

main_window.resizable(height=False, width=False)

def add_task():
    task = entry_task.get()
    if task != "":
         tasks_listbox.insert(tkinter.END, task)
         entry_task.delete(0, tkinter .END)

    else:
     tkinter.messagebox.showwarning(title="Warning!" , message= "You must enter a task")

def delete_task():
     try:
           task_index = tasks_listbox.curselection()[0]
           tasks_listbox.delete(task_index)

     except:
           tkinter.messagebox.showwarning(title="Warning!" , message= "You must select a task first")


def load_tasks():
     try:
          tasks = pickle.load(open("tasks.dat" , "rb"))
          tasks_listbox.delete(0, tkinter.END)
          for task in tasks:
           tasks_listbox.insert(tkinter.END, task)

     except:
          tkinter.messagebox.showwarning(title="Warning!" , message= "No data file found")


def save_tasks():
     tasks  = tasks_listbox.get(0, tasks_listbox.size())
     pickle.dump(tasks, open("tasks.dat" , "wb"))

lists_frame = tk.Frame(master=main_window, width=250, height=400)
lists_frame.pack(fill=tk.Y, side=tk.LEFT)
lists_frame.pack_propagate(0)
task_frame = tk.Frame(master=main_window, width=250, height=400)
task_frame.pack(fill=tk.Y, side=tk.LEFT)
task_frame.pack_propagate(0)

controls_frame = tk.Frame(master=main_window, width=250)
controls_frame.pack()

list_title_label = tk.Label(text="My todo Lists", master=lists_frame)
list_title_todo = tk.Label(text="My tasks", master=task_frame)
controls_title_label = tk.Label(text="controls", master=controls_frame)

list_title_label.pack()
list_title_todo.pack()
controls_title_label.pack()

lists_listbox = tk.Listbox(lists_frame, height=10, width=50)

lists_listbox.pack()

tasks_listbox = tk.Listbox(task_frame, height=10, width=50)
tasks_listbox.pack()

scrollbar_tasks = tkinter.Scrollbar(task_frame)
scrollbar_lists = tk.Scrollbar(lists_frame)

scrollbar_tasks.pack(side=tkinter .RIGHT, fill=tkinter .Y)
scrollbar_lists.pack(side=tkinter .RIGHT, fill=tkinter .Y)

entry_task = tkinter.Entry(main_window, width=50)
entry_task.pack()

button_add_task = tkinter.Button (main_window, text="Add task" , width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button (main_window, text="Delete task" , width=48, command= delete_task)
button_delete_task.pack()

button_save_tasks = tkinter.Button (main_window, text="Save tasks" , width=48, command=save_tasks)
button_save_tasks.pack()

button_load_tasks = tkinter.Button (main_window, text="Load tasks" , width=48, command=load_tasks)
button_load_tasks.pack()
main_window.mainloop()
