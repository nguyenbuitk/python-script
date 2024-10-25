import functions
import FreeSimpleGUI as sg

sg.theme("Black")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_todo = [todo.strip('\n') for todo in functions.get_todos()]
list_box = sg.Listbox(values=list_todo, key='todos', enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# when click event is execute, there will be two values, todo=InputText, todos=ListBox

window = sg.Window('My To-Do App', 
                   layout = [
                       [label], 
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    
    print("event: ", event)
    print("values: ", values)
    match event:
        case "Add":
            # write to file (have '\n')
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            
            # show on UI (don't have '\n')
            todos = [todo.strip('\n') for todo in todos]
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0] + '\n'
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                todos = [todo.strip('\n') for todo in todos]
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 15))
        
        case "Complete":
            try:
                todo_to_complete = values['todos'][0] + '\n'
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                todos = [todo.strip('\n') for todo in todos]
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 15))
        
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()