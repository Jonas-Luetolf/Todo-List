# ToDo-List
**Copyright (c) Jonas Lütolf 2022** <br>
**License: MIT**<br>
**E-Mail: jonas-luetolf@outlook.com**

## dependencies
- python3.10

## build dependencies
- [cx-freeze](https://github.com/marcelotduarte/cx_Freeze)

## Commands
- **show ```list name```** The command shows the selected List. If the list does not exist, it will be created.
- **add-task ```list name```** If the selected list exists it will add the task, else it will create the list and add the task to this list.
- **delete-task ```list name``` ```taskname```** The command deletes the selected Task.

## Flags
- **--state/-s** ```0/1``` (Optional at show) selects the state default: both
- **--folder/-f** ```path to folder``` (Optional at show and add task) selects the folder default: ~/.todo-list/
