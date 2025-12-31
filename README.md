# Task Manager CLI – Python
My first Self-made Python project!

This is a simple application that allows users to list, add, and delete tasks.
All tasks are automatically saved to a tasks.json file, ensuring persistence between sessions. 

## Two versions of the same application: 
- *cli-menu* which has a simple interface that runs on  a terminal.
- *cli-commands* runs purely on commands and has no interface.

## Functionalities
- Add task
- List all tasks
- Set task as completed
- Delete task

## Tecnologies
- Python 3
- JSON
- argparse
- datetime

## Running the application
### in root directory: use the command below to start the cli-menu application
```bash
python -m cli-menu
```
### in root directory: use the command below to start the cli-commands application
```bash
python -m cli-menu
```
#### availible commands
``` bash
python -m cli_commands list
```
```bash
python -m cli_commands done <index>
```
```bash
python -m cli_commands delete <index>
```


