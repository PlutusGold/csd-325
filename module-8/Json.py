#Dario Gomez Assignment 8.2 CSD325 4/18/25

import json

def main():
    student_list = load_json()
    if student_list is None:
        return
    print("Orignal Student List:")
    print_student_list(student_list)
    student_list = add_student(student_list)
    print("Updated Student List:")
    print_student_list(student_list)
    save_updated_list_to_json(student_list)
    print("Exiting Program")

def load_json():
    try:
        with open('student.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print('student.json file not found')


def print_student_list(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")


def add_student(student_list):
    new_student = {
        "F_Name": "Dario",
        "L_Name": "Gomez",
        "Student_ID": 78910,
        "Email": "Dario.Gomez@bellevue.com"
    }
    student_list.append(new_student)
    return student_list
def save_updated_list_to_json(student_list):
    try:
        with open('student.json', 'w') as json_file:
            json.dump(student_list, json_file, indent=4)
        print("student.json file was updated.")
    except Exception as f:
        print(f'Error updating JSON file: {f}')


if __name__ == '__main__':
    main()