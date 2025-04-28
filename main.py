from file_organizer.organizer import organize_folder
from task_manager.manager import add_task, view_tasks, delete_task

def main():
    while True:
        print("\n--- Smart Automation System ---")
        print("1. Organize Files")
        print("2. Add New Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            path = input("Enter the full path of the folder to organize: ")
            organize_folder(path)

        elif choice == '2':
            task_name = input("Enter task name: ")
            priority = int(input("Enter task priority (1=High, 5=Low): "))
            add_task(task_name, priority)

        elif choice == '3':
            view_tasks()

        elif choice == '4':
            task_name = input("Enter task name to delete: ")
            delete_task(task_name)

        elif choice == '5':
            print("Thank you for using Smart Automation System!")
            break

        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
