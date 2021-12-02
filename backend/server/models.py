from server import db

class Student(db.Model):
    sID = db.Column(db.Integer, primary_key = True)
    usn = db.Column(db.String(20), unique = True, nullable=False)
    deviceID = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    classID = db.Column(db.String(60), nullable=False)
    attendance = db.relationship("Attendance",backref="student")
    def __repr__(self) -> str:
        return f"User('{self.usn}','{self.deviceID}','{self.classID}')"

class Attendance(db.Model):
    aID = db.Column(db.Integer, primary_key= True)
    sID = db.Column(db.String(10), db.ForeignKey("student.sID"))
    sessionID = db.Column(db.String(20),unique = True, nullable= False)
    status = db.Column(db.String(20) ,default="pending")
    xcord  = db.Column(db.Integer)
    ycord  = db.Column(db.Integer)
    courseCode = db.Column(db.String(100))

class ClassCourse(db.Model):
    classID = db.Column(db.String(60), primary_key = True)
    subName = db.Column(db.String(100))
    courseCode = db.Column(db.String(100), unique=True)
