import tkinter

import tkinter.messagebox

import pickle

root = tkinter.Tk()
root.title("My To-Do List")

def add_task():
    task = entry_task.get()
    if task != "":
         listbox_task.insert(tkinter.END, task)
         entry_task.delete(0, tkinter .END)

    else:
     tkinter.messagebox.showwarning(title="Warning!" , message= "You must enter a task")

def delete_task():
     try:
           task_index = listbox_task.curselection()[0]
           listbox_task.delete(task_index)

     except:
           tkinter.messagebox.showwarning(title="Warning!" , message= "You must select a task first")


def load_tasks():
     try:
          tasks = pickle.load(open("tasks.dat" , "rb"))
          listbox_task.delete(0, tkinter.END)
          for task in tasks:
           listbox_task.insert(tkinter.END, task)

     except:
          tkinter.messagebox.showwarning(title="Warning!" , message= "No data file found")


def save_tasks():
     tasks  = listbox_task.get(0, listbox_task.size())
     pickle.dump(tasks, open("tasks.dat" , "wb"))

#Create GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_task = tkinter.Listbox(frame_tasks, height = 10, width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter .RIGHT, fill=tkinter .Y)

listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button (root, text="Add task" , width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button (root, text="Delete task" , width=48, command= delete_task)
button_delete_task.pack()

button_save_tasks = tkinter.Button (root, text="Save tasks" , width=48, command=save_tasks)
button_save_tasks.pack()

button_load_tasks = tkinter.Button (root, text="Load tasks" , width=48, command=load_tasks)
button_load_tasks.pack()




root.mainloop()