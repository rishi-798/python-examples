#class Point:
 #   def __init__(self, x, y):

    #    def draw(self):
   #         print("draw")

#point = Point(1,2)
#print(point.x)

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"



student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

students = {
    "Spongebob": student1,
    "Patrick": student2,
    "Sandy": student3
}


while True:
    print("\nWhat do you want to do?")
    print("1 - Look up a student")
    print("2 - Add a new student")
    print("3 - Quit")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print(students[name].get_info())
        else:
            print(f"No student named '{name}' found.")

    elif choice == "2":
        name = input("Enter the new student's name: ")
        gpa = float(input("Enter their GPA (e.g. 3.5): "))
        students[name] = Student(name, gpa)
        print(f"{name} has been added!")

    elif choice == "3":
        break
