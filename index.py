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