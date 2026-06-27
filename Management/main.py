import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"student" : [], "teacher": []}

if Path(database).exists():
    with open(database,'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent=4)


class Persons(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False

class Student(Persons):

    def get_roles(self):
        return "student"
    
    def register(self):
        name = input("tell your name :-")
        age = int(input("Tell your age :- "))
        email = input("Tell your email :-")
        roll_no = (input("Tell your roll number :- "))

        if not Persons.validate_email(email):
            print("invalid Email")
            return
        
        for i in data ['student']:
            if i['roll_no'] == roll_no:
                print("student already exist")

        data['student'].append({
            "name" : name,
            "age" : age,
            "email": email,
            "roll_no" :roll_no,
            "grade" : {}            
        })
        save()
        print (f"student {name} registered")

    
    def show_details(self):
        pass

    def add_grade(self):
        roll_no = input("tell the roll no :- ")
        subject = input("subject :- ")
        marks = float(input("Marks :- "))

        for i in data['student']:
            if i["roll_no"] == roll_no :
                i['grade'] [subject] = marks 
                save()
                print("grade added successfully")
                return
            print("student no found")

    

class Teacher(Persons):
    def get_roles(self):
        return "Teacher"
    
    def register(self):
        name = input("tell your name :-")
        age = int(input("Tell your age :- "))
        email = input("Tell your email :-")
        subject = input("subject :- ")
        emp_id = (input("Tell your emp id  :- "))

        if not Persons.validate_email(email):
            print("invalid Email")
            return
        
        for i in data ['teacher']:
            if i['emp_id'] == emp_id:
                print("teacher already exist")
                return
            
        data['teacher'].append({
            "name" : name,
            "age" : age,
            "email": email,
            "subject" : subject,
            "emp_id" : emp_id,
            "grade" : {}            
        })
        save()
        print (f"Teacher {name } register")

    def show_details(self):
        pass
    



stud = Student()
tech = Teacher()


print("press 1 to register a student")
print("press 2 to register a Teacher")
print("press 3 to add grades")
print("press 4 to show a student details")
print("press 5 to register a details")


choice = int(input("Please tell your choice :-"))

if choice == 1:
    stud.register()

elif choice == 2:
    tech.register()

elif choice == 3:
    stud.add_grade()
