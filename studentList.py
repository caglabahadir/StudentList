import json
from typing import Any
from dataclasses import dataclass
studentModel= []
@dataclass
class Student:
    StudentNo: int
    Name: str
    Surname: str
    DepartmentNo: int
    @staticmethod
    def from_dict(obj: Any) -> 'Student':
        _StudentNo = int(obj.get("StudentNo"))
        _Name = str(obj.get("Name"))
        _Surname = str(obj.get("Surname"))
        _DepartmentNo = int(obj.get("DepartmentNo"))
        return Student(_StudentNo, _Name, _Surname, _DepartmentNo)

searchWord = input("aranacak kelimeyi giriniz:")
jsonFile = open("Student.Json", "r")

file = jsonFile.read()

studentFile = json.loads(file)
for i in studentFile:
    studentModel.append(Student.from_dict(i))

for j in studentModel:
    if (j.Name).upper() == searchWord.upper() :
        print(j)
    elif (j.Surname).upper() == searchWord.upper() :
        print(j)
