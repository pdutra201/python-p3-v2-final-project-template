
# Category and Task CLI Project

This Python command-line project allows you to manage categories and tasks using a simple text-based interface. It utilizes SQLite for data storage and includes features for adding, listing, updating, and deleting tasks and categories.

## Features
0. Exit the program
1. Adds a new task
2. Lists all the tasks regardless of category
3. Adds a new category
4. Lists all of the categories
5. Changes the status of a task to complete
6. Filters the tasks by a entered due date
7. Shows the tasks under a specific category
8. Displays all the tasks due today
9. Deletes a category and cascade deletes the corresponding tasks 
10. Updates a task due date

## Database Schema
	•	Categories Table:
	  •	Category_ID (Primary Key)
  	•	name
	•	Tasks Table:
  	•	Task_ID (Primary Key)
  	•	name
	  •	Description
  	•	Due_date
	  •	Status (e.g., incomplete, complete)
	  •	CategoryID (Foreign Key referencing Categories)
