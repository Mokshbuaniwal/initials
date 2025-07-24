todo = []

while True:
    task = input("Add a task (or type 'done' to finish): ")
    if task == "done":
        break
    todo.append(task)

print("Your To-Do List:")
for i, task in enumerate(todo, 1):
    print(f"{i}. {task}")
