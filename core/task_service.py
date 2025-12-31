def print_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet! press 2 to add a new task")
    else:
        print(f"{' ':<3} {'STATE':<12} {'TASK':<30} {'DATE'}")
        print("-" * 60)
        for i, task in enumerate(tasks):
            state = "done" if task['done'] else "pendant"
            print(f"{i + 1:<1}. {state:<12} {task['task']:<30} ({task['date']})")

def add_task(text, date):
    return {
        "task": text,
        "done": False,
        "date": date
    }

def set_done(tasks, index):
    if index < 0 or index >= len(tasks):
        raise ValueError("La tarea no existe")
    tasks[index]["done"] = True


def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        raise ValueError("La tarea no existe")
    del tasks[index]
