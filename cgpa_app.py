import streamlit as st

## Grade dictionary
grade_points = {
    "O": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "P": 0
}

if "courses" not in st.session_state:
    st.session_state["courses"] = []

if "editing_index" not in st.session_state:
    st.session_state["editing_index"] = -1

def add_or_edit_course(course_credit, course_grade):
    course_info = {"credit": course_credit, "grade": course_grade}
    if st.session_state.editing_index >= 0:
        st.session_state.courses[st.session_state.editing_index] = course_info
        st.session_state.editing_index = -1
    else:
        st.session_state.courses.append(course_info)
## Clear func 
def clear_courses():
    st.session_state.courses = []
## GPA calculator
def calculate_cgpa():
    total_points = sum(grade_points[course["grade"]] * course["credit"] for course in st.session_state.courses)
    total_credits = sum(course["credit"] for course in st.session_state.courses)
    if total_credits == 0:
        return 0
    return total_points / total_credits

st.title("📘 CGPA Calculator")
st.markdown("Enter your course credits and grades to calculate your CGPA!")
st.write("### Add or Edit Course Details")

credit, grade = st.columns(2)
course_credit = credit.number_input("Course Credit", min_value=1, max_value=10, value=3)
course_grade = grade.selectbox("Course Grade", options=list(grade_points.keys()))

## BUTTONS FOR CALCULATING AND CLEARING AND ADDING 
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Add Course" if st.session_state.editing_index == -1 else "Update Course"):
        add_or_edit_course(course_credit, course_grade)
    if st.button("Clear All"):
        clear_courses()

with col2:
    if st.button("Calculate CGPA"):
        cgpa = calculate_cgpa()
        st.success(f"**Your CGPA:** {cgpa:.2f}")

st.write("### 📋 Course List")
st.write("Below are the courses you've added. Click 'Edit' to modify.")

for i, course in enumerate(st.session_state.courses):
    st.write(f"Course {i+1}: **Credit:** {course['credit']} | **Grade:** {course['grade']}")
    if st.button(f"Edit Course {i+1}", key=f"edit_{i}"):
        st.session_state.editing_index = i
        course_credit = course["credit"]
        course_grade = course["grade"]

### CSS STYLING
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 4px;
        padding: 8px 16px;
        margin: 4px 2px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)
