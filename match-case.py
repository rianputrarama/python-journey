todos = []

while True:
    action = input("Type add, show, edit, delete and exit : ")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo.capitalize())
        case 'show':
            for (i, item) in enumerate(todos, start=1):
                item = item.title()
                row = f"{i}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number - 1
            new_todo = input('Enter new todo : ')
            todos[number] = new_todo
        case 'delete':
            number = int(input("Number of the todo to delete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("you entered an unknown command")

print("bye!")