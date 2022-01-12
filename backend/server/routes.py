from server import app
from flask.globals import request
from flask.json import jsonify
from server.models import Attendance, AttendanceSchema, Session, SessionSchema, Student, StudentSchema, Teacher
from server import db

attendanceSchema = AttendanceSchema()
sessionSchema = SessionSchema()
studentSchema = StudentSchema()



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
    #print(user)
    print(request_data)
   # return jsonify(True)
    if user == None:
        return jsonify({"message": "auth unsuccessful" })
    if user.password == password:
        sid = user.sID
        return jsonify({"message": "auth successful", "sid":sid , "name": user.name})
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
        return jsonify({"message": "auth successful" ,"name": user.name, "tid": user.tID })
    else:
        return jsonify({"message": "auth unsuccessful"})

@app.route("/signupteacher" , methods= ["POST"])
def signupteacher():
    request_data = request.get_json()
    usn = request_data["usn"]
    name =  request_data["name"]
    password =  request_data["password"]
    user = Teacher(usn=usn, name=name, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "signed up"})

@app.route("/signupstudent" , methods= ["POST"])
def signupstudent():
    request_data = request.get_json()
    usn = request_data["usn"]
    name =  request_data["name"]
    password =  request_data["password"]
    subjectCodes = request_data["subjectCodes"]
    user = Student(subjectCodes=subjectCodes,usn=usn, name=name, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "signed up"})


@app.route("/createSession" , methods= ["POST"])
def createSession():
    request_data = request.get_json()
    subjectCode = request_data["subjectCode"] #which subject OS ADA
    classCode =  request_data["classCode"]    #which class 3A 5D
    timeInterval =  request_data["timeInterval"]
    tid =  request_data["tid"]
    date =  request_data["date"]
    session = Session(tid=tid,subjectCode=subjectCode, classCode=classCode, timeInterval=timeInterval,date=date)
    db.session.add(session)
    db.session.commit()
    return jsonify({"message": "created session", "sessionID": session.sessionID })


    

@app.route("/getAllSessionTeacher" , methods= ["POST"])
def getAllSessionTeacher():
    request_data = request.get_json()
    tid = request_data["tid"]
    sessions = Session.query.filter_by(tid=tid).all()
    print(sessions)
    return jsonify({"sessions":  [sessionSchema.dump(i) for i in sessions] })

@app.route("/getSessionDetails" , methods= ["POST"])
def getSessionDetails():
    request_data = request.get_json()
    sessionID = request_data["sessionID"]
    session = Session.query.filter_by(sessionID = sessionID).first()
    attendances = Attendance.query.filter_by(sessionID=sessionID).all()
    sids = [attendanceSchema.dump(i)["sID"] for i in attendances]
    print(sids)
    detailsOfAllStudents = []
    for i in sids:
        detailsOfAllStudents.append(Student.query.filter_by(sID=i).first())
    #print([attendanceSchema.dump(i) for i in attendances])
    return jsonify({"date": session.date , "classCode": session.classCode, "subjectCode":session.subjectCode, "timeInterval":session.timeInterval , "date":session.date ,"status": session.disabled, "attended": [studentSchema.dump(i) for i in detailsOfAllStudents ] })

@app.route("/getAttendance" , methods= ["POST"])
def getAttendance():
    request_data = request.get_json()
    sID = request_data["sID"]
    student=Student.query.filter_by(sID=sID).first()
    classEnrolled = student.subjectCodes.split(",")
    print(classEnrolled)
    d = {}

    for i in classEnrolled:
        x =  Session.query.filter_by(subjectCode=i).all()
        d[i] = {
            "conducted" : len(x),
            "conductedsessionIDs": [ sessionSchema.dump(i)["sessionID"] for i in x],
        }
    attendanceOfStudent = [ int(attendanceSchema.dump(i)["sessionID"]) for i in Attendance.query.filter_by(sID=sID).all()]
    print(attendanceOfStudent)
    for i in classEnrolled:
        sessionIDs = d[i]["conductedsessionIDs"]
        d[i] = {**d[i], "attended": len(list(set(attendanceOfStudent).intersection(sessionIDs)))} 
    print(d)
    return jsonify({"data": d})
    

@app.route("/punchAttendance" , methods= ["POST"])
def punchAttendance():
    request_data = request.get_json()
    print(request_data)
    sID = request_data["sID"]
    sessionID = request_data["sessionID"]
    print(sessionID)
    sess = Session.query.filter_by(sessionID = sessionID).first()
    if sess.disabled != 1:
        att = Attendance(sID=sID, sessionID=sessionID)
        db.session.add(att)
        db.session.commit()
        return jsonify({"message" : "added attendance"})
    else:
        return jsonify({"message": "something went wrong"})

@app.route("/disableAttendance" , methods= ["POST"])
def disableAttendance():
    request_data = request.get_json()
    print(request_data)
    sessionID = request_data["sessionID"]
    print(sessionID)
    sess = Session.query.filter_by(sessionID = sessionID).first()
    if sess.disabled == 1:
        sess.disabled = 0
        db.session.commit()
        
        return jsonify({"message": "enabled"})
    else:
        sess.disabled = 1
        db.session.commit()
        return jsonify({"message": "disabled"})
        
    