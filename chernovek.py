from abc import ABC, abstractmethod
import random
import string
import json

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def take_exam(self, questions):
        pass

class Teacher(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self._students = []

    @property
    def students(self):
        with open(self.filename, "r") as f:
            data = json.loads(f.read())
        return data

    @students.setter
    def students(self, students_list):
        if isinstance(students_list, list):
            self._students = students_list
        else:
            print("Invalid input. Please provide a list of students.")
        
    def save_to_json(self, filename):
        self.filename = filename
        with open(self.filename, "w") as f:
            f.write(json.dumps(self._students))

    def add_student(self, student, filename):
        self._students.append(student)
        self.save_to_json(filename)

        
        
    def create_exam(self):
        # Code to create an exam
        pass

    def take_exam(self):
        symbols = string.ascii_letters + string.digits + string.punctuation
        print([random.choice(symbols) for _ in range(8)])
    
    

class Student(Person):
    def __init__(self, ID, email):
        super().__init__(ID, email)
        self.exam_result = None
    

        


    def take_exam(self, questions):
        # Code to take the exam
        pass

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def set_text(self, text):
        self.text = text

    def set_options(self, options):
        self.options = options

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer

class ExamError(Exception):
    pass

class LoginError(Exception):
    pass

class Exam:
    def __init__(self):
        self.questions = []
    
    def add_question(self, question):
        if not isinstance(question, Question):
            raise ExamError("Invalid question type")
        self.questions.append(question)

    def create_exam(self):
        if len(self.questions) == 0:
            raise ExamError("No questions added to the exam")
        # Code to create the exam


def main():
    Our_exam = Exam()
    print("""-------------------------------------
Welcome to the Exam System!")
"Are you a teacher or a student?""")
    user_type = input("""
-------Who are you?-------
1. Teacher
2. Student
Your choice: """)

    if user_type == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        teacher = Teacher(name, email)
        print("""You are now logged in as a teacher. 
\t === You can ===:
1. Add students that will pass exam
2. Create exam""")
        
        #adding student
        choiceof_teacher = input("choose one (1/2): ")
        if choiceof_teacher == "1":
            while True:
                student_id = input("Enter student's name (type 'done' to finish): ")
                if student_id.lower() == 'done':
                    break
                student_email = input("Enter student's email: ")
                student = [student_id, student_email]
                teacher.add_student(student, "{}".format(name))
        #if you are a student
        elif choiceof_teacher == "2":
            while True:
                question = Question("", "", "")
                question.set_text(input("Your question(type 'done' to finish): "))
                if question.text.lower() == "done":
                    break
                question.set_options({"a": input("A options: "),
                            "b": input("B options: "),
                            "c": input("C options: "),
                            "d": input("D options: ")})
                question.set_correct_answer(input("the correct option: "))
                Our_exam.add_question(question)


    #for student
    elif user_type == '2':
        Teacher_name = input("Your teacher: ")
        ID = input("Enter your ID: ")
        try:
            with open(Teacher_name, "r") as f:
                data = json.loads(f.read())
                
                if ID in (i[0] for i in data):    
                                        
                    print("Access granted. You can take the exam now.")
                    
                else:
                    print("Permission denied. You are not registered with this teacher.")
                        
        except FileNotFoundError:
            print("==> Teacher hasn't been founded <==")
            
        
        
    else:
        print("Invalid user type. Please choose 'teacher' or 'student'.")

if __name__ == "__main__":           
    main()
