from core.task_service import add_task, set_done, delete_task
from core.task_repository import save_tasks, load_tasks
from datetime import datetime
       
def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def print_tasks(tasks):
    print(f"{' ':<3} {'STATE':<12} {'TASK':<30} {'DATE'}")
    print("-" * 60)
    for i, task in enumerate(tasks):
        state = "done" if task['done'] else "in progress"
        print(f"{i + 1:<1}. {state:<12} {task['task']:<30} ({task['date']})")

def get_tasks(tasks):
    if len(tasks) == 0:
        print("Aún no hay ninguna tarea, si tenes alguna agregala apretando 2")
    else:
        print_tasks(tasks)
        
def create_task(tasks):
    task_text = input("Agregá la tarea: ").strip()
    
    new_task = add_task(task_text, current_date())
    
    tasks.append(new_task)
    save_tasks(tasks)
    print("tarea agregada, si queres verla apreta 1")
    
def mark_done(tasks):
    if len(tasks) == 0:
        print("No hay tareas")
        return

    print_tasks(tasks)
    try:
        num = int(input("Qué tarea marcar como hecha? "))
        set_done(tasks, num - 1)
        save_tasks(tasks)
        print("Tarea marcada como hecha")
    except (ValueError, IndexError):
        print("Número inválido")

    
def del_task(tasks):
    if len(tasks) == 0:
        print("No hay tareas para borrar")
        return

    try:
        tarea_remove = int(input("Que tarea quiere eliminar? "))
        delete_task(tasks, tarea_remove - 1)
        save_tasks(tasks)
        print("tarea eliminada correctamente")
    except (ValueError, IndexError):
        print("invalid number")
    print_tasks(tasks)
    
def run():
    ejecucion = True
    tasks =load_tasks()
    while ejecucion:
        print("\n --- GESTOR DE TAREAS ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como hecha")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        eleccion = input("Elegí una opción: ")
        
        if eleccion == "1":
            get_tasks(tasks)
                    
        elif eleccion == "2":
            create_task(tasks)
        
        elif eleccion == "3":
            mark_done(tasks)
        
        elif eleccion == "4":
            del_task(tasks)
            
        elif eleccion == "5":
            ejecucion = False
            print("chau!")
        
        else:
            print("opcion invalida")
