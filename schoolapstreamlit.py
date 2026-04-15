import streamlit as st


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} - GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "Average GPA: 0"
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


if "students" not in st.session_state:
    st.session_state.students = {
        "Spongebob": Student("Spongebob", 3.2),
        "Patrick": Student("Patrick", 2.0),
        "Sandy": Student("Sandy", 4.0),
    }

st.title("Student Manager 🎓")

menu = st.radio("Choose an option:", ["Look up a student", "Add a new student"])

if menu == "Look up a student":
    name = st.text_input("Enter student name")

    if st.button("Search"):
        if name in st.session_state.students:
            st.success(st.session_state.students[name].get_info())
        else:
            st.error(f"No student named '{name}' found.")

elif menu == "Add a new student":
    name = st.text_input("Student name")
    gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.1)

    if st.button("Add Student"):
        st.session_state.students[name] = Student(name, gpa)
        st.success(f"{name} has been added!")

st.divider()
st.subheader("Class Stats")
st.write(Student.get_count())
st.write(Student.get_average_gpa())