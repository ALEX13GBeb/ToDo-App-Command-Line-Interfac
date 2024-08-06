# ToDo-App-Command-Line-Interface
My First Project - A Simple To-Do Tracking App 
This project is a simple To-Do tracking application that can be accessed via the command line interface (CLI).

Usage:
------
OBS: The app is not case-sensitive.
      Extra white space at the beginning or the end of an input variable doesn't affect the program.
      Make sure you spelled correctly tho.

1. Run the script.

2. You will be presented with the following options:
   1. Add
   2. See Todo List
   3. See Complete Todo List
   4. Edit
   5. Remove
   6. Complete
   7. Options
   8. Exit

3. Enter the number or command corresponding to the action you want to perform. The commands are case-insensitive.

4. Actions:
   - Add:
     - Prompts you to write down a new to-do item. Type the item and press Enter. 
     - If you want to cancel, type "Back" and press Enter.

   - See Todo List:
     - Displays the current list of to-do items. If the list is empty, it notifies you.

   - See Complete Todo List:
     - Displays the current list of completed to-do items. If the list is empty, it notifies you.

   - Edit:
     - Prompts you to enter the to-do item or its number that you want to edit.
     - If you want to cancel, type "Back" and press Enter.
     - If you enter a valid item or number, you will be prompted to enter the replacement text.

   - Remove:
     - Prompts you to enter the to-do item or its number that you want to remove.
     - If you want to cancel, type "Back" and press Enter.
     - If you want to remove all items, type "Clear" and press Enter.
     - If you enter a valid item or number, it will be removed from the list.

   - Complete:
     - Prompts you to enter the to-do item or its number that you want to mark as complete.
     - If you want to cancel, type "Back" and press Enter.
     - If you want to mark all items as complete, type "Clear" and press Enter.
     - If you enter a valid item or number, it will be moved from the to-do list to the completed list.

   - Options:
     - Displays the menu options again.

   - Exit:
     - Exits the application.

5. The application will continue to run until you select the "Exit" option.
