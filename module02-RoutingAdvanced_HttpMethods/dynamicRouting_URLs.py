from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "Hello World !!"


# |--------> Basic Dynamic Route
@app.route("/student/<student_id>")
def student(student_id):
    return f"Student ID: {student_id}"

# |--------> Multiple Dynamic Parameters
@app.route("/student/<int:student_id>/subject/<subject>")
def student_subject(student_id, subject):
    return (
        f"Student ID: {student_id}, "
        f"Subject: {subject}"
    )

if __name__ == "__main__":
    app.run(debug=True)

