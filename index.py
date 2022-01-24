from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "+2"
    }
}
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
# gt, lt, ge, le, comperators


@app.get("/get_student/{student_id}")
def get_student(student_id: int = Path(None, description="ID of the Student to view")):
    return students[student_id]
