from server import app
from flask.globals import request
from flask.json import jsonify

from server.models import Student 


@app.route("/" , methods= ["GET"])
def home():
    d = {"message": "Attendify Server Online"}
    return jsonify(d)

@app.route("/login" , methods= ["POST"])
def login():
    usn = request.form.get("usn")
    password = request.form.get("password")
    user = Student.query.filter_by(usn=usn).first()
    if user.password == password:
        return jsonify({"message": "auth successful"})
    else:
        return jsonify({"message": "auth unsuccessful", "deviceID": user.deviceID})

