import tabulate
from datetime import datetime
import os
import sys
import json
import time

#Welcome the  user
def welcome_user():
    print("Welcome to your Personal Task Manager")
    print("let's streamline your productivity and achieve your goals. \n")


#Structure Task Manager
#organize task with details eg priority,status,deadline
#Task structure

task=[]
#add simple task
def initialize_task():
    task.append({"Title": "Complete python project","priority":"High", "status":"pending","deadline":"2025-01-30"})
    
#Adding and Viewing Tasks
#add a new task
def add_task(title,priority,status,deadline):
        task.append({"Title":title,"Priority":priority,"Status":status,"Deadline":deadline})
        print("Task added successfully!\n")

#Updating Task status
#view all tasks
def view_task():
    from tabulate import tabulate
    print(tabulate(task,headers="keys",tablefmt="grid"))
    
    
    #update task status
def update_status(task_index,new_status):
    try:
        tasks[task_index]["Status"]=new_status
        print("Task status updated!\n")
    except IndexError:
        print("Invalid task index.\n")
        
#Deleting completed Task
    #delete completed task
def delete_completed_task():
    global tasks
    tasks=[task for task in task if task["status"] !="Completed"]
    print("Completed tasks deleted! \n")
    
#Intergrating the components
#main function

def main():
    welcome_user()
    initialize_task()
    
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task status")
        print("4. Delete completed status")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice =="1":
            view_task()
        elif choice=="2":
            title=input("Enter task title: ").strip()
            priority=input("Enter the priority (High\Meduim\Low): ").strip()
            status=input("Enter status (Pending\In progress\Completed): ").strip()
            deadline=input("Enter deadline (YYYY-MM-DD): ").strip()
            add_task(title,priority,status,deadline)
        elif choice =="3":
            task_index=int(input("Enter task index to update: ").strip())
            new_status=input("Enter new status : ").strip()
            update_status(task_index,new_status)
        elif choice =="4":
            delete_completed_task()
        elif choice=="5":
            print("Exiting Task manager.stay productive ")
            break
        else:
            print("Invalid choice.please try again .\n")
if __name__ == "__main__":
    main()