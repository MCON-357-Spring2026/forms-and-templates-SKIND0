from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None
    name = ""
    grade = ""

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        # TODO:
        # 1. Validate name
        # 2. Validate grade is number
        # 3. Validate grade range 0–100
        # 4. Add to students list as dictionary
        # 5. Redirect to /students
        if not name or name.strip() == "":
            error = "Name cannot be empty"
        else:
            try:
                grade = float(grade)
                if grade < 0 or grade > 100:
                    error = "Grade must be between 0 and 100"
                else:
                    students.append({"name": name, "grade": grade})
                    return redirect(url_for("display_students"))
            except ValueError:
                error = "Grade must be a number"

    return render_template("add.html", error=error, name=name, grade=grade)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    # - average grade
    # - highest grade
    # - lowest grade
    if len(students) == 0:
        return render_template("summary.html", no_students=True)

    total = len(students)
    average = sum(student["grade"] for student in students) / total
    highest = max(student["grade"] for student in students)
    lowest = min(student["grade"] for student in students)

    return render_template("summary.html", total=total, average=average, highest=highest, lowest=lowest)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
