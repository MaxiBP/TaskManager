from colorama import Fore, Back, Style

def print_tasks(tasks):
    
    if len(tasks) == 0:
        print(Fore.RED +"No tasks yet! press 2 to add a new task"+ Style.RESET_ALL)
    else:
        print(Fore.CYAN)
        print(f"{' ':<3} {'STATE':<12} {'TASK':<30} {'DATE'}")
        print("-" * 60)
        print(Style.RESET_ALL)
        for i, task in enumerate(tasks):
            state_text = "done" if task['done'] else "pendant"
            state_padding = f"{state_text:<12}"
            
            color = Fore.GREEN if task['done'] else Fore.YELLOW
            
            print(
                f"{i + 1:<1}. "
                f"{color}{state_padding}{Style.RESET_ALL} "
                f"{Fore.LIGHTCYAN_EX}{Style.DIM}{task['task']:<30} "
                f"({task['date']}){Style.RESET_ALL}"
            )

def add_task(text, date):
    return {
        "task": text,
        "done": False,
        "date": date
    }

def set_done(tasks, index):
    if index < 0 or index >= len(tasks):
        raise ValueError(Fore.RED +"Task doesn't exists"+ Style.RESET_ALL)
    tasks[index]["done"] = True


def delete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        raise ValueError(Fore.RED +"Task doesn't exists"+ Style.RESET_ALL)
    del tasks[index]
