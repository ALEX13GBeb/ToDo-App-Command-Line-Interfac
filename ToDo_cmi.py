# Import read, write, append functions
import Modules.functions

# Print Options
print("What would you like to do?\n"
              "1. Add\n"
              "2. See Todo List\n"
              "3. See Complete Todo List\n"
              "4. Edit\n"
              "5. Remove\n"
              "6. Complete\n"
              "7. Options\n"   
              "8. Exit")


# App closes only when you choose to
while True:

    # Choose what to do
    mode = input("Choose Mode: ").lower().strip()


    match mode:


        case "1" | "add":

            Todo = input("Write down a Todo: ").lower().strip().capitalize()

            # Abandon Action
            if Todo == "Back":
                pass

            Modules.functions.append_file(Todo+"\n", filepath="Text Files/todos.txt")


        case "2" | "see todo list":

            # Get the current to do list
            file_todo_list= Modules.functions.read_file(filepath="Text Files/todos.txt")

            if len(file_todo_list)==0:
                print("You don't have any Todos")

            else:
                for i in range(len(file_todo_list)):
                    print(f"{i+1}. {file_todo_list[i]}".strip("\n"))


        case "3" | "see complete todo list":

            # Get the current complete to do list
            file_complete_list = Modules.functions.read_file(filepath="Text Files/complete_todos.txt")

            if len(file_complete_list) == 0:
                print("You don't have any Completed Todos")

            else:
                for i in range(len(file_complete_list)):
                    print(f"{i + 1}. {file_complete_list[i]}".strip("\n"))


        case "4" | "edit":


            # Get the current to do list
            todo_list= Modules.functions.read_file(filepath="Text Files/todos.txt")


            if len(todo_list)!=0:

                while True:

                    edited = input("What Todo would you like to edit?:").lower().strip().capitalize()
                    edited_string=edited+"\n"

                    # Abandon Action
                    if edited=="Back":
                        break


                    #If edited is a string
                    if edited_string in todo_list:
                        replacement = input("Your replacement:")
                        index=todo_list.index(edited_string)
                        todo_list[index]=replacement.lower().strip().capitalize() + "\n"
                        print("Todo Edited")
                        break

                    # If edited is a number
                    elif edited.isdigit():

                        try:
                            edited_index = int(edited) - 1  # Convert to zero-based index
                            if 0 <= edited_index < len(todo_list):
                                replacement = input("Your replacement: ").lower().strip().capitalize()
                                todo_list[edited_index] = replacement + "\n"
                                print("Todo Edited")
                                break

                        except (ValueError, IndexError):
                            print("Invalid input. Please enter a valid Todo item or number.")

                # Update to do list
                Modules.functions.write_file(todo_list, filepath="Text Files/todos.txt")

            else:
                print("You don't have any Todos to edit")
                continue


        case "5" | "remove":

            # Get the current to do list
            todo_list = Modules.functions.read_file(filepath="Text Files/todos.txt")

            if len(todo_list)!=0:

                while True:

                    removed = input("What Todo would you like to remove?:").lower().strip().capitalize()+"\n"

                    # Abandon Action
                    if removed=="Back\n":
                        break

                    # If removed is a string
                    if removed in todo_list:
                        todo_list.remove(removed)
                        print("Todo Removed")

                        break

                    # Cleare the whole list
                    elif removed=="Clear\n":
                        todo_list=[]
                        print("Todo Cleared")

                        break

                    # If removed is a number
                    else:
                        try:
                            removed = int(removed)
                            todo_list.pop(removed - 1)
                            print("Todo Removed")

                            break

                        except (ValueError, IndexError):
                            print("Invalid input. Please enter a valid Todo item or number.")

                # Update to do list
                Modules.functions.write_file(todo_list, filepath="Text Files/todos.txt")

            else:
                print("You don't have any Todos to remove")
                continue




        case "6" | "complete":

            # Get the current to do list
            todo_list = Modules.functions.read_file(filepath="Text Files/todos.txt")

            if (len(todo_list))!=0:

                while True:


                    complete = input("What Todo would you like to add to the complete list?:").lower().strip().capitalize() + "\n"

                    # Abandon Action
                    if complete=="Back":
                        break


                    if complete in todo_list:

                        todo_list.remove(complete)
                        # Update the complete to do list
                        Modules.functions.append_file(complete, filepath="Text Files/complete_todos.txt")
                        print("Todo Completed")

                        break

                    elif complete == "Clear\n":

                        # Update the complete to do list
                        Modules.functions.append_file(todo_list, filepath="Text Files/complete_todos.txt")

                        todo_list = []
                        print("Completed ALL todos")

                        break

                    else:

                        try:

                            complete = int(complete)
                            # Update the complete to do list
                            Modules.functions.append_file(todo_list[complete - 1], filepath="Text Files/complete_todos.txt")
                            todo_list.pop(complete - 1)

                            print("Todo Completed")

                            break

                        except (ValueError, IndexError):
                            print("Invalid input. Please enter a valid Todo item or number.")

                # Update the to do list
                Modules.functions.write_file(todo_list, filepath="Text Files/todos.txt")

            else:
                print("No available Todos to complete")
                continue


        case "7" | "options":

            print("What would you like to do?\n"
                  "1. Add\n"
                  "2. See Todo List\n"
                  "3. See Complete Todo List\n"
                  "4. Edit\n"
                  "5. Remove\n"
                  "6. Complete\n"
                  "7. Exit")


        case "8" | "exit":
            print("=====EXITING=====")
            break


        case _:
            print("Invalid mode selected.")
