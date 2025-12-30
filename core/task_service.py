def add_task(text, date):
    return {
        "task": text,
        "done": False,
        "date": date
    }

def set_done(tasks, index):
    tasks[index]["done"] = True

def delete_task(tasks, index):
    del tasks[index]
