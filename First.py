class Course:
    def _init_(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def _str_(self):
        return f"{self.course_code}: {self.course_name} ({self.credits} credits)"


class Student:
    def _init_(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"Student {self.name} is enrolled in the following courses:")
        for course in self.courses:
            print(course)


class Campus:
    def _init_(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)


# Example Usage:
math_course = Course("MATH101", "Introduction to Mathematics", 3)
physics_course = Course("PHYS201", "Physics for Scientists", 4)

alice = Student(1, "Alice")
bob = Student(2, "Bob")

campus = Campus("Example University")
campus.add_course(math_course)
campus.add_course(physics_course)
campus.add_student(alice)
campus.add_student(bob)

alice.enroll(math_course)
bob.enroll(physics_course)

alice.display_courses()
bob.display_courses()
