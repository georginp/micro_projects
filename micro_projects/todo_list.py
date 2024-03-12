def main_menu():
    print()
    print("===== To-Do List Menu =====")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. View all tasks")
    print("4. Quit")
    print()


def add_task(tasks):
    print()
    task = input("Enter a task description: ")
    tasks.append({"task_description": task, "completed_status": False})
    print(f"Task '{task}' added successfully!")
    print()


def mark_task_completed(tasks):
    if tasks:
        view_all_tasks(tasks)
        task_index = int(input("Enter the index of the task to mark as completed: "))
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed_status"] = True
            print(f"Task '{tasks[task_index]['task_description']}' marked as completed!")
        else:
            print("Please enter a valid index that can be found in the list!")
        print()
    else:
        print("Please first add tasks to the list!")


def view_all_tasks(tasks):
    if tasks:
        print("===== Tasks =====")
        for index, task in enumerate(tasks):
            status = "[X]" if task["completed_status"] else "[]"
            print(f"{index}. {status} {task['task_description']}")
    else:
        print("Please first add tasks to the list!")


def main():
    tasks = []
    while True:
        main_menu()

        choice = input(("Enter your choice (1-4): "))

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_completed(tasks)
        elif choice == "3":
            view_all_tasks(tasks)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Not a valid choice. Please select a valid option (1-4)")


if __name__ == "__main__":
    main()
