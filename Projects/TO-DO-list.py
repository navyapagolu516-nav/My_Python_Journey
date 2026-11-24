class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append({'task':task, 'completed':False})
        print(f"Task added successfully")

    def mark_completed(self,task):
        for i in self.tasks:
            if i["task"] == task:
                i["completed"] = True
                return print(f"Task marked as completed!")
            
        else:
            print(f"Task not found in the list!")

    def remove_task(self,task):
        for i in self.tasks:
            if i["task"] == task:
                self.tasks.remove(i)
                return print(f"Task removed successfully")
        else:
            print(f"Task not found in the list!")

    def display_tasks(self):
        if self.tasks:
            for index, i in enumerate(self.tasks, start=1):
                status = "Completed" if i["completed"] else "Not Completed"
                print(f"{index}. {i['task']} - {status}")
        else:
            print("No tasks available!")

    def exit(self):
        print("Exiting...")
        


# # task = input("Enter Tasks: ")

# todo_list.add_task("Learn Python")
# todo_list.add_task("Practice Django")
# todo_list.add_task("Build API")
# todo_list.mark_completed("Build API")
# print(todo_list.tasks)

def main():
    todo_list = TodoList()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")
            continue

        if choice == 1:
            task = input("Enter task to add:")
            todo_list.add_task(task)
        elif choice == 2:
            task = input("Enter task to remove:")
            todo_list.remove_task(task)
        elif choice == 3:
            task = input("Enter task to mark as completed:")
            todo_list.mark_completed(task)
        elif choice == 4:
            todo_list.display_tasks()
        elif choice == 5:
            todo_list.exit()
            break
        else:
            print("Invalid choice! Please select 1-5.")
    
main()

    