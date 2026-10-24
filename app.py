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


if __name__ == "__main__":
    app.run(debug=True)
