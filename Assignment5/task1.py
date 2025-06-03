student_marks = {
    "Yaswanth": 88,
    "Sravika": 91,
    "Koushik": 76,
    "Kartheek": 84,
    "Vamsi": 68,
    "Mani": 95,
    "Kavya": 73,
}

name = input("Enter the student's name: ")
marks = student_marks.get(name)
print(f"{name}'s marks: {marks}" if marks else "Student not found.")
