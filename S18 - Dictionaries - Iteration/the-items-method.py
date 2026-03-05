college_courses = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstein"
}

for course, professor in college_courses.items():
    print(f"The course {course} is being taught by {professor}.")

for _, professor in college_courses.items():
    print(f"The next professor is {professor}")