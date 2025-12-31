from core.task_service import add_task, set_done, delete_task, print_tasks
from core.task_repository import save_tasks, load_tasks
from datetime import datetime
       
def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

        
def create_task(tasks):
    task_text = input("Add task: ").strip()
    
    new_task = add_task(task_text, current_date())
    
    tasks.append(new_task)
    save_tasks(tasks)
    print("task added! press 1 to see it")
    
def mark_done(tasks):
    if len(tasks) == 0:
        print("no tasks to set!")
        return

    print_tasks(tasks)
    try:
        num = int(input("Which task have you completed?"))
        set_done(tasks, num - 1)
        save_tasks(tasks)
        print("Congrats! task done")
    except (ValueError, IndexError):
        print("The task doesn't exists :(")

    
def del_task(tasks):
    if len(tasks) == 0:
        print("No tasks left to delete")
        return

    print_tasks(tasks)
    try:
        tarea_remove = int(input("which task you want to delete? "))
        delete_task(tasks, tarea_remove - 1)
        save_tasks(tasks)
        print("task deleted!")
    except (ValueError, IndexError):
        print("The task doesn't exists :(")
    
    
def run():
    ejecucion = True
    tasks =load_tasks()
    while ejecucion:
        print("\n --- TASK MANAGER ---")
        print("1. List tasks")
        print("2. Add a Task")
        print("3. Set done")
        print("4. Delete task")
        print("5. Leave")
        
        eleccion = input("Choose an option: ")
        
        if eleccion == "1":
            print_tasks(tasks)
                    
        elif eleccion == "2":
            create_task(tasks)
        
        elif eleccion == "3":
            mark_done(tasks)
        
        elif eleccion == "4":
            del_task(tasks)
            
        elif eleccion == "5":
            ejecucion = False
            print("Bye!")
        
        else:
            print("We don't have that option... yet")
