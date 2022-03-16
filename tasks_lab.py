
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task["description"])

# uncompleted_tasks()

def completed_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task["description"])

# completed_tasks()

def task_descriptions():
    for task in tasks:
        print(task["description"])

# task_descriptions()

def long_tasks():
    for task in tasks:
        if task["time_taken"] >= 30:
            print(task["description"])

# long_tasks()

def given_description():
    for task in tasks:
        if task["description"] == "Walk Dog":
            print(task["description"])

    # for task in tasks:
    #     if task["description"] == "Cat":
    #         print(task["description"])
    # else:
    #     print("nope. no task")

# given_description()

### Extension
def update_task():
    input_description = input("Give the task description you wish to mark as completed \n")
    for task in tasks:
        if input_description == task["description"]:
                task["completed"] = True
                print(task)

# update_task()

def add_task():
    input_descripton = input("Describe the task \n")
    input_completed = input("Have you completed the task? \n")
    input_time_taken = input("How long did the task take? \n")
    new_task = {
        "description": input_descripton, 
        "completed": input_completed, 
        "time_taken": input_time_taken
    }
    tasks.append(new_task)
    print(tasks)

add_task()

### Further Extensions

# option = ""
# while option != "q":
#     print("Menu:")
#     print("1: Display All Tasks")
#     print("2: Display Uncompleted Tasks")
#     print("3: Display Completed Tasks")
#     print("4: Mark Task as Complete")
#     print("5: Get Tasks Which Take Longer Than a Given Time")
#     print("6: Find Task by Description")
#     print("7: Add a new Task to list")
#     print("M or m: Display this menu")
#     print("Q or q: Quit")
#     option = input("What would you like to do? \n")
