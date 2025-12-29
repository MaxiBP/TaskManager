import json
from datetime import datetime
ejecucion = True

# Persists tasks by saving tasks[] onto the json file
def saveTasks():
    with open("tasks.json", "w", encoding= "utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
  
# Loads tasks from the json file to the array tasks      
def loadTasks():
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
        
def currentDate():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def printTasks():
    print(f"{' ':<3} {'STATE':<12} {'TASK':<30} {'DATE'}")
    print("-" * 60)
    for i, task in enumerate(tasks):
        state = "done" if task['done'] else "in progress"
        print(f"{i + 1:<1}. {state:<12} {task['task']:<30} ({task['date']})")

def getTasks():
    if len(tasks) == 0:
        print("Aún no hay ninguna tarea, si tenes alguna agregala apretando 2")
    else:
        printTasks()
        
def addTask():
    taskText = input("Agregá la tarea: ").strip()
    
    newTask = {
        "task": taskText,
        "done": False,
        "date": currentDate()
        
    }
    
    tasks.append(newTask)
    saveTasks()
    print("tarea agregada, si queres verla apreta 1")
    
def setDone():
    if len(tasks) == 0:
        print("No hay tareas")
        return

    printTasks()
    try:
        num = int(input("Qué tarea marcar como hecha? "))
        tasks[num - 1]["done"] = True
        saveTasks()
        print("Tarea marcada como hecha")
    except (ValueError, IndexError):
        print("Número inválido")

    
def deleteTask():
    if len(tasks) == 0:
        print("No hay tareas para borrar")
        return

    try:
        tareaRemove = int(input("Que tarea quiere eliminar? "))
        del tasks[tareaRemove - 1]
        saveTasks()
        print("tarea eliminada correctamente")
    except (ValueError, IndexError):
        print("invalid number")
    printTasks()
    
    
loadTasks()
while ejecucion:
    print("\n --- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como hecha")
    print("4. Eliminar tarea")
    print("5. Salir")
    
    eleccion = input("Elegí una opción: ")
    
    if eleccion == "1":
        getTasks()
                
    elif eleccion == "2":
        addTask()
    
    elif eleccion == "3":
        setDone()
    
    elif eleccion == "4":
        deleteTask()
        
    elif eleccion == "5":
        ejecucion = False
        print("chau!")
    
    else:
        print("opcion invalida")
