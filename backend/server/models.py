from server import db

class Student(db.Model):
    sID = db.Column(db.Integer, primary_key = True)
    usn = db.Column(db.String(20), unique = True, nullable=False)
    name = db.Column(db.String(50), unique = True, nullable=False)
    # deviceID = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    classCode = db.Column(db.String(60), nullable=False)
    subjectCodes = db.Column(db.String(60), nullable=False)
    #attendance = db.relationship("Attendance",backref="student")

class Teacher(db.Model):
    tID = db.Column(db.Integer, primary_key = True)
    usn = db.Column(db.String(20), unique = True, nullable=False)
    name = db.Column(db.String(50), unique = True, nullable=False)
    # deviceID = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Attendance(db.Model):
    aID = db.Column(db.Integer, primary_key= True)
    sID = db.Column(db.String(10))
    sessionID = db.Column(db.String(20),unique = True, nullable= False)
    # xcord  = db.Column(db.Integer)
    # ycord  = db.Column(db.Integer)

class Session(db.Model):

    tid = db.Column(db.Integer )
    sessionID = db.Column(db.Integer, primary_key= True)
    classCode = db.Column(db.String(10))
    subjectCode = db.Column(db.String(20),unique = True, nullable= False)
    timeInterval = db.Column(db.String(100))
    date = db.Column(db.String(100))
    # status = db.Column(db.String(20) ,default="pending")
    # xcord  = db.Column(db.Integer)
    # ycord  = db.Column(db.Integer)

# class ClassCourse(db.Model):
#     classID = db.Column(db.String(60), primary_key = True)
#     subName = db.Column(db.String(100))
#     courseCode = db.Column(db.String(100), unique=True)
