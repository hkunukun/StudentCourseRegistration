from flask import Flask, render_template, request

app = Flask(__name__)

courses = [
    {"id": 1, "name": "Python Programming"},
    {"id": 2, "name": "Web Development"},
    {"id": 3, "name": "Machine Learning"}
]

students = []
enrollments = []


@app.route("/")
def home():
    return render_template("index.html", courses=courses)


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            message = "Please enter both name and email."
        elif any(s["email"].lower() == email.lower() for s in students):
            message = "This email is already registered."
        else:
            students.append({
                "id": len(students) + 1,
                "name": name,
                "email": email
            })
            message = "Student registered successfully!"

    return render_template(
        "register.html",
        students=students,
        message=message
    )


@app.route("/enroll", methods=["GET", "POST"])
def enroll():
    message = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        course_id = request.form.get("course_id", "")

        student = next(
            (s for s in students if s["email"].lower() == email.lower()),
            None
        )
        course = next(
            (c for c in courses if str(c["id"]) == course_id),
            None
        )

        if not student or not course:
            message = "Please select a valid student and course."
        elif any(
            e["student_id"] == student["id"]
            and e["course_id"] == course["id"]
            for e in enrollments
        ):
            message = "This student is already enrolled in this course."
        else:
            enrollments.append({
                "student_id": student["id"],
                "student_name": student["name"],
                "course_id": course["id"],
                "course_name": course["name"]
            })
            message = "Course enrollment successful!"

    return render_template(
        "enroll.html",
        students=students,
        courses=courses,
        enrollments=enrollments,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
