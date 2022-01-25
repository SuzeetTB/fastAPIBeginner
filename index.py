from operator import gt
from typing import Optional
from unicodedata import name
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "+2"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


'''
    Student Model requires all data but for update we need selective so UpdateModel GIves us that facility

'''


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# Root API


@app.get("/")
def index():
    return {"Message": "API is Working"}

# Fun as QueryParams
# http://127.0.0.1:8000/sum?args1=1&args2=4


@app.get("/sum")
def sum(args1: int, args2: int):
    sum = args1 + args2
    return {"SUM": sum}

# Read API


@app.get("/get_all_students")
def get_student():
    return students

# gt, lt, ge, le, comperators
# Path params
# http://127.0.0.1:8000/get_student/3


@app.get("/get_student/{student_id}")
def get_student(student_id: int = Path(None, description="ID of the Student to view", gt=0, lt=9)):
    return students[student_id]

# Query params
# http://127.0.0.1:8000/get_by_name?name=john


@app.get("/get_by_name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Message": "Data NOt found"}

# Combining query params and path parmas
# @app.get("/get_by_name/{student_id}")
# def get_student(*, student_id: int, name: Optional[str] = None, test: int):


#Req.boady and post
# make a class using BaseMOdel
@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    students[student_id] = student
    return students[student_id]

# UPDATE


@app.put("/update_student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student Does not Exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student Does not Exist"}
    del students[student_id]

    return {
        "message": "Student Deleted",
        "students": students
    }
