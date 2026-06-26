import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"student" : [], "teacher": []}

if Path(database).exists():
    with open(database,'r') as f:
        content = f.read
        if content:
            data = json.loads(content)




print("press 1 to register a student")
print("press 2 to register a Teacher")
print("press 3 to add grades")
print("press 4 to show a student details")
print("press 5 to register a details")


choice = int(input("Please tell your choice :-"))

if choice == 1:
    pass

