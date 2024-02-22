import os
from datetime import datetime, date
from tabulate import tabulate

DATETIME_STRING_FORMAT = "%d-%m-%Y"

def create_user_file_if_not_found():
    """Crea el archivo user.txt si no existe."""
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")


def read_users_file():
    """Lee el contenido del archivo user.txt y devuelve un diccionario de usuarios y contraseñas."""
    
    username_password = {}

    with open("user.txt", 'r') as user_file:
        for line in user_file:
            username, password = line.strip().split(';')
            username_password[username] = password
    return username_password


def initial_line():
    print("*-" * 20)


def initial_loggin(user, password):
    """Realiza el proceso de inicio de sesión."""
    
    logged_in = False

    # Leer el archivo de usuarios y contraseñas
    username_password = read_users_file()  

    if user in username_password:
        if username_password[user] == password:
            print("\nInicio de sesión exitoso!\n")
            logged_in = True
        else:
            print("Incorrect password.")
    else:
        print("User doesn't exist or incorrect password.")

    return logged_in


def validate_alpha_data_entry(alpha_data):
    """Valida la entrada de datos."""
    while True:
        if not alpha_data:
            print("Please enter data.")
        elif not alpha_data.replace(" ", "").replace("-", "").isalpha():
            print("Please enter only alpha characters. "
                  f"Could contain spaces or hyphens as well.")
        else:
            return True
        alpha_data = input("Try again: ")


def validate_data_entry(data):
    """Valida la entrada de datos."""
    while True:
        if not data:
            data = input("Plese entry valid data: ")
        else:
            return True


def display_main_menu():
    """Muestra el menú principal."""
    options = [
        ["r", "Register a user"],
        ["a", "Add a task"],
        ["va", "View all tasks"],
        ["vm", "View my tasks"],
        ["ds", "Display statistics"],
        ["e", "Exit"]
    ]
            
    print(tabulate(options, headers=["Option", "Description"], tablefmt="grid"))


def registration_user_option(new_user, username_password):
    """Registra un nuevo usuario."""
    while new_user in username_password:
        print("\nUser already exists.\n")
        new_user = input("Please enter a different username: ")
        validate_alpha_data_entry(new_user)

    new_password = input("New Password: ")
    validate_data_entry(new_password)
    confirm_password = input("Confirm Password: ")
    validate_data_entry(confirm_password)

    if new_password == confirm_password:
        print("New user added successfully")
        username_password[new_user] = new_password
        add_new_user_to_user_file(username_password)


def create_user_pass_dictionary():
    """Crea un diccionario de usuarios y contraseñas."""
    username_password = read_users_file()  # Obtener usuarios y contraseñas del archivo
    return username_password


def add_new_user_to_user_file(username_password):
    """Agrega un nuevo usuario al archivo user.txt."""
    with open("user.txt", "w") as out_file:
        user_data = []
        for k in username_password:
            user_data.append(f"{k};{username_password[k]}")
        out_file.write("\n".join(user_data))


def read_tasks_file():
    """Lee el contenido del archivo tasks.txt."""
    try:
        with open("tasks.txt", 'r+') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t.split(";") for t in task_data if t]  # Convertir cada línea en una lista de campos separados por ";"
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos
        with open("tasks.txt", 'w') as task_file:
            task_data = []

    return task_data


def create_task_list(task_data):
    """Crea una lista de tareas a partir de los datos del archivo."""
    task_list = []
    for i, task_components in enumerate(task_data, start=1):  # Utilizamos enumerate para obtener el índice
        curr_t = {}
        curr_t['number'] = i  # Asigna el número de tarea como el valor del contador 'i'
        curr_t['username'] = task_components[1]
        curr_t['title'] = task_components[2]
        curr_t['description'] = task_components[3]
        curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[6] == "Yes" else False
        task_list.append(curr_t)
    return task_list



def assign_task_to_user(username):
    """Asigna una tarea a un usuario."""
    username_password = read_users_file()  # Leer los usuarios del archivo

    while username not in username_password:
        print("user doesn't exist.")
        username = input("Please enter a valid user: ")


def validate_if_username_registered(task_username, username_password):
    """Valida si el nombre de usuario está registrado."""
    while True:
        if task_username in username_password.keys():
            return task_username
        else:
            print("User does not exist.")

        task_username = input("Please enter a username already registered: ")


def add_new_task_to_task_list(task_list, task_username, task_title, task_description, due_date_time, curr_date):
    """Agrega una nueva tarea a la lista de tareas."""
    task_number = len(task_list) + 1  # Obtén el número de tarea como el siguiente número en la secuencia

    new_task = {
        "number": task_number,  # Se añade el número de tarea al diccionario
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list.append(new_task)
    print("peter")
    print(task_list)
    return task_list


def write_new_task_to_tasks_file(task_list):
    """Agrega el task_list al archivo tasks.txt."""
    with open("tasks.txt", "w+") as task_file:
        for task in task_list:
            task_data = [
                task['number'],  # Número de tarea consecutivo
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DATETIME_STRING_FORMAT),
                task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task['completed'] else "No"
            ]
            task_file.write(";".join(task_data) + "\n")
            print(f"Task {task_data[0]} successfully added to output file tasks.txt")



def create_tasks_file_if_not_found():
    """Crea el archivo tasks.txt si no existe."""
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass


def write_new_task_in_output_file(task_list):
    """Abre el archivo de salida para escribir la nueva tarea."""
    with open("tasks.txt", "a+") as task_file:
        for t in task_list:
            t_number = str(t['number'])

            str_attrs = [
                t_number,
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_file.write(";".join(str_attrs) + "\n")
    print("Task successfully added.")


def view_all_tasks_option(task_list):
    """Muestra todas las tareas en task_list."""
    if not task_list:
        print("No tasks available.")
        return

    print("\nAll Tasks:\n")
    for task in task_list:
        print("------------------------------")
        task_number = task.get('number') or task.get('task_number')  # Intenta obtener el número de tarea
        if task_number is not None:
            print(f"Task number:\t\t{task_number}")  # Imprimimos el número de tarea si está presente
        else:
            print("Task number:\t\tN/A")  # O imprime "N/A" si no está presente
        print(f"Username:\t\t{task['username']}")
        print(f"Title:\t\t\t{task['title']}")
        print(f"Description:\t\t{task['description']}")
        print(f"Due Date:\t\t{task['due_date']}")
        print(f"Assigned Date:\t\t{task['assigned_date']}")
        print(f"Completed:\t\t{'Yes' if task['completed'] else 'No'}")



def view_my_tasks_option(curr_user):
    """Visualiza las tareas del usuario actual."""
    
    # Leer los datos de las tareas del archivo
    task_data = read_tasks_file()
    print(task_data)
    # Crear una lista de tareas a partir de los datos leídos
    task_list = create_task_list(task_data)
    print(task_list)

    # Variable para rastrear si se encontraron tareas asignadas al usuario actual
    found_tasks = False

    # Lista para almacenar las tareas del usuario actual
    my_task_list = []
    print(my_task_list)

    # Mostrar las tareas del usuario actual
    initial_line()
    print("Your tasks:")
    for i, task in enumerate(task_list, start=1):
        if task['username'] == curr_user:
            found_tasks = True
            initial_line()
            print(f"Task number:\t\t{task['number']}")  # Imprimimos el número de tarea
            print(f"Task assigned to:\t {task['username']}")
            print(f"Task title:\t\t {task['title']}")
            print(f"Task description:\t {task['description']}")
            print(f"Date assigned:\t\t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Due date:\t\t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Completed: \t\t{'Yes' if task['completed'] else ' No'}")
            print()
            # Agregar la tarea a la lista de tareas del usuario actual
            task['task_number'] = i
            my_task_list.append(task)

    # Si no se encontraron tareas asignadas al usuario actual, mostrar un mensaje
    if not found_tasks:
        print("No tasks assigned to you.")

    print(my_task_list)
    # Devolver la lista de tareas del usuario actual
    return my_task_list


def validate_if_task_number_in_my_task_list(specific_task, my_task_list):
    """Valida si el número de tarea especificado está en la lista de tareas."""
    for task in my_task_list:
        if str(task.get('task_number')) == specific_task:
            return True
    return False


def validate_my_task_status(specific_task, my_task_list):
    """Valida el estado de la tarea."""
    for task in my_task_list:
        if str(task.get('task_number')) == specific_task:
            if not task['completed']:
                return True  # La tarea no está completada
            else:
                print("Task completed. Can't be edited.")
                return False  # La tarea está completada
    return False  # Tarea no encontrada



def display_edit_or_complete():
    options = [
        ["eu",  "\tEdit username"],
        ["ed",  "\tEdit due date"],
        ["ct",  "\tComplete task"],    
        ["e",   "\tExit"]
    ]
            
    print(tabulate(options, headers=["Opcion", "Description"], tablefmt="grid"))


def edit_task(task_list, specific_task):
    # Buscar la tarea específica en la lista de tareas
    for i, task in enumerate (task_list, start=1):
        if str(task.get('task_number')) == specific_task:
            print("Task found:")
            print(f"Assigned to: {task['username']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Completed: {'Yes' if task['completed'] else 'No'}")
            print()

            edit_option = input("What would you like to edit? \n"
                                "u \tfor username\n"
                                "s \tfor status \n"
                                "dd \tfor due date.\n").lower()
            validate_alpha_data_entry(edit_option)

            if task['completed'] == True:
                print("Task status is completed. It can't be edited.")
                display_main_menu()
                break

            if edit_option == "u":
                edit_username = input("Which user would you like to re-assing the task? ")
                new_username = validate_if_username_registered(edit_username, username_password)
                # Llamada a la función para validar si el nuevo usuario existe
                if new_username in read_users_file():
                    task['username'] = new_username
                    print("Username updated successfully.")
                    print(task)
                    display_main_menu()
                else:
                    print("Username does not exist.")
                    display_main_menu()
                    break
            
            elif edit_option == "s":
                task['completed'] = True
                print("Task status changed to Completed.")
                print(task)
                display_main_menu()

            elif edit_option == "dd":
                if task['due_date'] > datetime.now():
                    new_task_due_date = input("Please enter new due date (DD-MM-YYYY): ")
                    validate_data_entry(new_task_due_date)
                    task['due_date'] = new_task_due_date
                    print(task)
                    display_main_menu()
                else:
                    print("Task overdue. Due date can't be edited.")
                    display_main_menu()
                    break


def complete_task(task_list, specific_task):
    # Buscar la tarea específica en la lista de tareas
    for task in task_list:
        if str(task.get('task_number')) == specific_task:
            task['completed'] = True
            print("Task status changed to Completed.")
            break
    else:
        print("Task not found.")


def write_task_list_to_file(task_list):
    """Escribe la lista de tareas en el archivo tasks.txt."""
    with open("tasks.txt", "w") as task_file:
        for task in task_list:
            task_file.write(f"{task['username']};{task['title']};{task['description']};"
                            f"{task['due_date'].strftime(DATETIME_STRING_FORMAT)};"
                            f"{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)};"
                            f"{'Yes' if task['completed'] else 'No'}\n")
    print("Tasks updated successfully.")


def display_stats_option():      
    """Muestra las estadísticas."""
    if menu == 'ds' and curr_user == 'admin': 
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    


def exit_option():
    if menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


def main():

    create_user_file_if_not_found()
    username_password = create_user_pass_dictionary()
    print(username_password)

    task_data = read_tasks_file()  
    print(task_data)
    task_list = create_task_list(task_data)
    print("TRES")
    print(task_list)

    DATETIME_STRING_FORMAT = "%d-%m-%Y"

    while True:
        
        initial_line()
        print("\nPlease LOGIN\n")
        curr_user = input("Username: ")
        validate_data_entry(curr_user)
        curr_pass = input("Password: ")
        validate_data_entry(curr_pass)

        if initial_loggin(curr_user, curr_pass) == False:
            print("Verify your data and try again.")
            break

        while True:
            display_main_menu()
            user_option = input("Select an option from the main menu: ").lower()
            validate_data_entry(user_option)

            if user_option == "r":
                new_username = input("New Username: ")
                validate_alpha_data_entry(new_username)
                registration_user_option(new_username, username_password)

            elif user_option == "a":
                # missing task number
                task_username = input("Name of person assigned to task: ")
                validated_username = validate_if_username_registered(task_username, username_password) 
                task_title = input("Title of Task: ")
                validate_data_entry(task_title)
                task_description = input("Description of Task: ")
                validate_data_entry(task_description)
                task_due_date = input("Due date of task (DD-MM-YYYY): ")
                validate_data_entry(task_due_date)
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                curr_date = date.today()
                #new_date = curr_date.strftime('%d-%m-%Y')
                #corregir la longitud de la siguiente linea
                
                add_new_task_to_task_list(task_list, validated_username, task_title, task_description, due_date_time, curr_date)
                
                write_new_task_to_tasks_file(task_list)

            elif user_option == "va":
                view_all_tasks_option(task_list)

            if user_option == "vm":
                my_task_list = view_my_tasks_option(curr_user)

                specific_task = input("\nWould you like to select any of your tasks "
                                    "by task number? Enter the task number, "
                                    "or -1 to go back to Main Menu: \n")

                if specific_task == "-1":
                    display_main_menu()
                else:
                    specific_task = str(specific_task)  # Converts to string.
                    if validate_if_task_number_in_my_task_list(specific_task, my_task_list):
                        if validate_my_task_status(specific_task, my_task_list):
                            display_edit_or_complete()
                            user_option = input("Select an option: ").lower()
                            validate_data_entry(user_option)
                            #change et to eu
                            if user_option == "eu":
                                edit_task(task_list, specific_task)  # Calls the function to edit the task.
                            #change ct to ed
                            elif user_option == "ed":
                                edit_due_date(task_list, specific_task)  # Calls the function to Complete the task.
                            elif user_option == "ct":
                                complete_task(task_list, specific_task)  # Calls the function to Complete the task.
                        else:
                            print("Task already completed. Cannot be edited.")
                    else:
                        print("Invalid task number.")

                write_task_list_to_file(task_list)  # Updates the file tasks.txt

                #display_stats_option()
                #exit_option
                        

if __name__ == "__main__":
    main()
