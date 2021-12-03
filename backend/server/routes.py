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
    request_data = request.get_json()
    usn = request_data["usn"]
    password =  request_data["password"]
    user = Student.query.filter_by(usn=usn).first()
    print(user) 
   # return jsonify(True)
    if user == None:
        return jsonify({"message": "auth unsuccessful"})
    if user.password == password:
        return jsonify({"message": "auth successful","deviceID": user.deviceID})
    else:
        return jsonify({"message": "auth unsuccessful"})