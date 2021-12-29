from server import app
from flask.globals import request
from flask.json import jsonify
from server.models import Student, Teacher 


@app.route("/" , methods= ["GET"])
def home():
    d = {"message": "Attendify Server Online"}
    return jsonify(d)

@app.route("/loginstudent" , methods= ["POST"])
def loginstudent():
    request_data = request.get_json()
    usn = request_data["usn"]
    password =  request_data["password"]
    user = Student.query.filter_by(usn=usn).first()
    print(user) 
   # return jsonify(True)
    if user == None:
        return jsonify({"message": "auth unsuccessful"})
    if user.password == password:
        return jsonify({"message": "auth successful"})
    else:
        return jsonify({"message": "auth unsuccessful"})


@app.route("/loginteacher" , methods= ["POST"])
def loginteacher():
    request_data = request.get_json()
    usn = request_data["usn"]
    password =  request_data["password"]
    user = Teacher.query.filter_by(usn=usn).first()
    print(user)
   # return jsonify(True)
    if user == None:
        return jsonify({"message": "auth unsuccessful"})
    if user.password == password:
        return jsonify({"message": "auth successful"})
    else:
        return jsonify({"message": "auth unsuccessful"})


@app.route("/createSession" , methods= ["POST"])
def createSession():
    request_data = request.get_json()
    subjectCode = request_data["subjectCode"]
    classCode =  request_data["classCode"]
    timing =  request_data["timing"]
    date =  request_data["date"]
    
    