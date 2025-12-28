import json
ejecucion = True

def saveTasks():
    with open("tasks.json", "w", encoding= "utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
        
def loadTasks():
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def printTareas():
    for i, tarea in enumerate(tasks):
        print(f"{i + 1}. {tarea}")

def verTareas():
    if len(tasks) == 0:
        print("Aún no hay ninguna tarea, si tenes alguna agregala apretando 2")
    else:
        printTareas()
        
def agregarTarea():
    tareaNueva = input("Agregá la tarea: ")
    tasks.append(tareaNueva)
    saveTasks()
    print("tarea agregada, si queres verla apreta 1")
    
def eliminarTarea():
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
    printTareas()
    
    
loadTasks()
while ejecucion:
    print("\n --- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    eleccion = input("Elegí una opción: ")
    
    if eleccion == "1":
        verTareas()
                
    elif eleccion == "2":
        agregarTarea()
    
    elif eleccion == "3":
        eliminarTarea()
        
    elif eleccion == "4":
        ejecucion = False
        print("chau!")
    
    else:
        print("opcion invalida")
