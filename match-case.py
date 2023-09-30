todos = []

while True:
    action = input("Type add, show and exit : ")

    match action:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo.capitalize())
        case 'show':
            print(todos)
        case 'exit':
            break

print("bye!")