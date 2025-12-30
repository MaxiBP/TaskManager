import json
import os

FILE_PATH = "tasks.json"

# Loads tasks from the json file to the array tasks
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read().strip()

        if content == "":
            return []

        return json.loads(content)

# Persists tasks by saving tasks[] onto the json file
def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding= "utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
  