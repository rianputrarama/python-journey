todos = []

while True:
    action = input("Type add, show and exit : ")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo.capitalize())
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:
            print("you entered an unknown command")

print("bye!")