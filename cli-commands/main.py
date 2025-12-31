import argparse
from core.task_service import add_task, set_done, delete_task, print_tasks
from core.task_repository import save_tasks, load_tasks
from datetime import datetime

def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

            
def run():
    tasks = load_tasks()
    
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # add task
    parser_add = subparsers.add_parser("add", help="Add tasks")
    parser_add.add_argument("task")
    
    # list tasks
    subparsers.add_parser("list", help="List all tasks")
    
    # set done
    parser_done = subparsers.add_parser("done", help="Set task as done by index")
    parser_done.add_argument("index", type=int)
    
    # delete task
    parser_delete = subparsers.add_parser("delete",help="delete task by index")
    parser_delete.add_argument("index", type=int)
    
    args = parser.parse_args()
    
    if args.command == "add":
        new_task = add_task(args.task, current_date())
        tasks.append(new_task)
        save_tasks(tasks)
    
    elif args.command == "list":
        print_tasks(tasks)
    
    elif args.command == "done":
        try:
            set_done(tasks, args.index - 1)
            save_tasks(tasks)
            print("task done")
        except ValueError as e:
            print(f"Error: {e}")
        
    elif args.command == "delete":
        try:
            delete_task(tasks, args.index - 1)
            save_tasks(tasks)
            print("Tarea eliminada")
        except ValueError as e:
            print(f"Error: {e}")

        
    else:
        parser.print_help()